"""S-expression parser for Dune build manifests (dune / dune-project files).

Implements DuneManifestParserPort: discovers every dune file under a project
root, parses the S-expression syntax (nested lists, quoted strings, ``;``
comments) and extracts the build topology — libraries, executables, inter-library
dependencies and wrapping mode.
"""

from __future__ import annotations

import os
from pathlib import Path

from pattern_detector.ports.outbound.dune_parser_port import (
    DuneExecutableStanza,
    DuneLibraryStanza,
    DuneManifest,
    DuneManifestParserPort,
    DuneProjectInfo,
    DuneProjectTree,
)

#: Directories that never contain project sources.
SKIP_DIRS = {"_build", ".git", ".hg", ".svn", "node_modules", "_opam", "_esy", ".venv", "venv", "__pycache__"}


class SExpressionError(ValueError):
    """Raised when a dune file contains malformed S-expression syntax."""


#: A parsed S-expression node: either a quoted/unquoted atom or a nested list.
type Sexp = str | list[Sexp]


def tokenize(text: str) -> list[str]:
    """Tokenize dune S-expression text: parens, atoms, and quoted strings."""
    tokens: list[str] = []
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch in " \t\r\n":
            i += 1
        elif ch == ";":  # comment until end of line
            while i < n and text[i] != "\n":
                i += 1
        elif ch in "()":
            tokens.append(ch)
            i += 1
        elif ch == '"':  # quoted string atom (may contain spaces/escapes)
            j = i + 1
            while j < n:
                if text[j] == "\\":
                    j += 2
                    continue
                if text[j] == '"':
                    break
                j += 1
            tokens.append(text[i : j + 1])
            i = j + 1
        elif ch == "#" and i + 1 < n and text[i + 1] == '"':  # #"..."# quoted atom
            j = text.find('"#', i + 2)
            j = n if j == -1 else j + 2
            tokens.append(text[i:j])
            i = j
        else:  # bare atom
            j = i
            while j < n and text[j] not in " \t\r\n();":
                j += 1
            tokens.append(text[i:j])
            i = j
    return tokens


def parse_sexp(text: str) -> list[list[Sexp]]:
    """Parse dune S-expression text into a list of top-level stanzas (nested lists)."""
    tokens = tokenize(text)
    pos = 0

    def parse_list(depth: int) -> list[Sexp]:
        nonlocal pos
        result: list[Sexp] = []
        while pos < len(tokens):
            tok = tokens[pos]
            if tok == "(":
                pos += 1
                result.append(parse_list(depth + 1))
            elif tok == ")":
                pos += 1
                if depth == 0:
                    raise SExpressionError("unbalanced ')' in dune file")
                return result
            else:
                result.append(tok)
                pos += 1
        if depth != 0:
            raise SExpressionError("unbalanced '(' in dune file")
        return result

    forms = parse_list(0)
    return [f for f in forms if isinstance(f, list)]


def _unquote(atom: str) -> str:
    if len(atom) >= 2 and atom[0] == '"' and atom[-1] == '"':
        return atom[1:-1]
    if atom.startswith('#"') and atom.endswith('"#'):
        return atom[2:-2]
    return atom


def _field_atoms(stanza: list[Sexp], field: str) -> list[str]:
    """All string atoms of the first ``(field ...)`` sub-list of a stanza."""
    for item in stanza:
        if isinstance(item, list) and item and item[0] == field:
            return [_unquote(a) for a in item[1:] if isinstance(a, str)]
    return []


def _field_atom(stanza: list[Sexp], field: str) -> str | None:
    atoms = _field_atoms(stanza, field)
    return atoms[0] if atoms else None


def _library_deps(stanza: list[Sexp]) -> list[str]:
    """Deps of ``(libraries ...)``: plain atoms plus ``(select ...)`` source libraries.

    ``(select <target>.ml from (lib_a -> a.ml) (lib_b -> b.ml))`` picks the first
    available source library, so every listed source library is a dependency —
    the generated target file is not.
    """
    deps: list[str] = []
    for item in stanza:
        if isinstance(item, list) and item and item[0] == "libraries":
            for entry in item[1:]:
                if isinstance(entry, str):
                    deps.append(_unquote(entry))
                elif isinstance(entry, list) and entry and entry[0] == "select":
                    in_from = False
                    for part in entry[1:]:
                        if isinstance(part, str) and part == "from":
                            in_from = True
                        elif (
                            isinstance(part, list) and in_from and part and isinstance(part[0], str)
                        ):
                            # (lib_a -> a.ml): the condition library is the dep.
                            deps.append(_unquote(part[0]))
    return deps


class DuneManifestParser(DuneManifestParserPort):
    """Filesystem-driven Dune manifest parser producing a DuneProjectTree."""

    def parse_project(self, project_root: str) -> DuneProjectTree:
        root = Path(project_root).resolve()
        tree = DuneProjectTree(project_root=str(root))

        if not root.is_dir():
            return tree

        dune_project_path = root / "dune-project"
        if dune_project_path.is_file():
            tree.dune_project = self._parse_dune_project(dune_project_path)

        default_wrapped = True
        if tree.dune_project is not None and tree.dune_project.lang_version:
            default_wrapped = self._project_default_wrapped(root)

        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
            if "dune" not in filenames:
                continue
            manifest_path = Path(dirpath) / "dune"
            try:
                stanzas = parse_sexp(manifest_path.read_text(encoding="utf-8", errors="replace"))
            except (SExpressionError, OSError):
                continue  # graceful fallback: skip broken/foreign dune files
            tree.manifests.append(self._build_manifest(manifest_path, stanzas, default_wrapped))

        return tree

    # ------------------------------------------------------------------
    # Stanza extraction
    # ------------------------------------------------------------------

    def _build_manifest(
        self, path: Path, stanzas: list[list[Sexp]], default_wrapped: bool
    ) -> DuneManifest:
        directory = str(path.parent)
        manifest = DuneManifest(path=str(path), directory=directory)

        include_subdirs: str | None = None
        for stanza in stanzas:
            if stanza and stanza[0] == "include_subdirs" and len(stanza) > 1 and isinstance(stanza[1], str):
                include_subdirs = _unquote(stanza[1])

        for stanza in stanzas:
            head = stanza[0] if stanza else ""
            if head == "library":
                public_name = _field_atom(stanza, "public_name")
                name = _field_atom(stanza, "name") or public_name
                if not name:
                    continue
                wrapped_field = _field_atom(stanza, "wrapped")
                wrapped = default_wrapped if wrapped_field is None else wrapped_field != "false"
                manifest.libraries.append(
                    DuneLibraryStanza(
                        name=name,
                        public_name=_field_atom(stanza, "public_name"),
                        libraries=_library_deps(stanza),
                        wrapped=wrapped,
                        directory=directory,
                        include_subdirs=include_subdirs,
                    )
                )
            elif head in ("executable", "test"):
                manifest.executables.append(
                    DuneExecutableStanza(
                        names=[_field_atom(stanza, "name") or ""],
                        libraries=_library_deps(stanza),
                        directory=directory,
                    )
                )
            elif head in ("executables", "tests"):
                manifest.executables.append(
                    DuneExecutableStanza(
                        names=_field_atoms(stanza, "names"),
                        libraries=_library_deps(stanza),
                        directory=directory,
                    )
                )
        return manifest

    def _parse_dune_project(self, path: Path) -> DuneProjectInfo:
        info = DuneProjectInfo(path=str(path))
        try:
            stanzas = parse_sexp(path.read_text(encoding="utf-8", errors="replace"))
        except (SExpressionError, OSError):
            return info

        for stanza in stanzas:
            head = stanza[0] if stanza else ""
            if head == "lang" and len(stanza) >= 3 and stanza[1] == "dune":
                version = stanza[2]
                if isinstance(version, str):
                    info.lang_version = _unquote(version)
            elif head == "package":
                pkg = _field_atom(stanza, "name")
                if pkg:
                    info.packages.append(pkg)
            elif head == "name":
                if len(stanza) > 1 and isinstance(stanza[1], str):
                    info.project_name = _unquote(stanza[1])
        return info

    def _project_default_wrapped(self, root: Path) -> bool:
        """Read ``(library (default_wrapped false))` from dune-project when present."""
        path = root / "dune-project"
        try:
            stanzas = parse_sexp(path.read_text(encoding="utf-8", errors="replace"))
        except (SExpressionError, OSError):
            return True
        for stanza in stanzas:
            if stanza and stanza[0] == "library" and _field_atom(stanza, "default_wrapped") == "false":
                return False
        return True
