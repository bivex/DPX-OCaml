"""OCaml module dependency extractor: raw source -> per-compilation-unit dependency facts.

Implements a fast regex/token-scanner pipeline (no full AST) so that projects
with hundreds of files stay well under the performance budget. For every
compilation unit (``.ml`` paired with its optional ``.mli``) it extracts:

* ``open`` / ``open!`` and ``include`` directives (with usage counts),
* functor applications (``module M = F (Arg)``),
* qualified references (``Module.ident`` / ``Module.Type.sub``),
* nested submodule declarations,
* the interface contract: abstract vs concrete exported type declarations.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from pydantic import BaseModel, Field

_OPEN_RE = re.compile(r"\bopen\s*!\s*([A-Z][A-Za-z0-9_'.]*)|\bopen\s+([A-Z][A-Za-z0-9_'.]*)")
_INCLUDE_RE = re.compile(r"\binclude\s+([A-Z][A-Za-z0-9_'.]*)")
_FUNCTOR_APP_RE = re.compile(
    r"\bmodule\s+(?:rec\s+)?([A-Z][A-Za-z0-9_']*)\s*(?::[^=\n]+)?=\s*([A-Z][A-Za-z0-9_'.]*)\s*\(([^()]*)\)"
)
_QUALIFIED_RE = re.compile(
    r"\b([A-Z][A-Za-z0-9_']*(?:\.[A-Z][A-Za-z0-9_']*)+)\b"
    r"|"
    r"\b([A-Z][A-Za-z0-9_']*)\s*\.\s*(?:[a-z_]|[({\[])"
)
_LOCAL_MODULE_RE = re.compile(
    r"\bmodule(?:\s*%\s*[a-z0-9_.]+)?\s+(?:rec\s+)?(?:type\s+)?([A-Z][A-Za-z0-9_']*)"
)
_LOCAL_AND_MODULE_RE = re.compile(r"\band\s+([A-Z][A-Za-z0-9_']*)\s*(?::\s*[^=\n]+)?(?:=|:)")
_FUNCTOR_HEAD_RE = re.compile(
    r"\b(?:module(?:\s*%\s*[a-z0-9_.]+)?\s+(?:rec\s+)?[A-Z][A-Za-z0-9_']*|\bfunctor)\s*"
)
_PARAM_START_RE = re.compile(r"\(\s*([A-Z][A-Za-z0-9_']*)\s*:")
_SUBMODULE_RE = re.compile(
    r"\bmodule\s+(?:rec\s+)?([A-Z][A-Za-z0-9_']*)\s*(?:\([^)]*\)\s*)?(?::\s*[^=\n]+)?(?:=|:)\s*(?:struct|sig|functor)"
)
_TYPE_RE = re.compile(r"\btype\s+(?:rec\s+)?(?:'[^=\s]+\s+)*\(?\s*(?:'[^=\s]+\s*,\s*)*\)?\s*([a-z_][A-Za-z0-9_']*)")
_DECL_END_RE = re.compile(r"\n\s*(?:type|let|module|val|open|include|exception|and|end|class)\b|;;|\Z")

#: Uppercase identifiers that are OCaml keywords / builtins, never module references.
_NON_MODULE_UPPER = {"Module", "Some", "Assert"}


class ModuleDependencyInfo(BaseModel):
    """Dependency facts about one OCaml compilation unit (.ml + optional .mli)."""

    file_path: str
    module_name: str
    loc: int = 0
    has_interface: bool = False
    is_interface_only: bool = False
    opens: dict[str, int] = Field(default_factory=dict)
    includes: dict[str, int] = Field(default_factory=dict)
    functor_apps: list[tuple[str, str]] = Field(default_factory=list)
    qualified_refs: dict[str, int] = Field(default_factory=dict)
    submodules: list[str] = Field(default_factory=list)
    local_modules: list[str] = Field(default_factory=list)
    exported_types: int = 0
    abstract_types: int = 0
    defines_type_t: bool = False


class ModuleDependencyExtractor:
    """Extracts module-level dependency facts from raw OCaml sources."""

    def extract(self, sources: dict[str, str]) -> dict[str, ModuleDependencyInfo]:
        """Merge .ml/.mli pairs and extract dependencies per compilation unit.

        Returns a mapping keyed by the unit's ``.ml`` path (real for implementation
        units, virtual for interface-only ones) to its dependency info.
        """
        by_unit: dict[str, dict[str, str]] = {}
        for file_path in sorted(sources):
            path = Path(file_path)
            if path.suffix not in {".ml", ".mli"}:
                continue
            if not re.match(r"^[A-Za-z0-9_']+$", path.stem):
                continue
            unit_key = str(path.with_suffix(".ml"))
            by_unit.setdefault(unit_key, {})[path.suffix] = sources[file_path]

        infos: dict[str, ModuleDependencyInfo] = {}
        for unit_key, parts in by_unit.items():
            infos[unit_key] = self._extract_unit(unit_key, parts)
        return infos

    # ------------------------------------------------------------------
    # Unit-level extraction
    # ------------------------------------------------------------------

    def _extract_unit(self, unit_key: str, parts: dict[str, str]) -> ModuleDependencyInfo:
        impl = parts.get(".ml")
        intf = parts.get(".mli")
        path = Path(unit_key)
        module_name = self.module_name_of(path.stem)

        info = ModuleDependencyInfo(
            file_path=str(path.with_suffix(".mli")) if impl is None else unit_key,
            module_name=module_name,
            has_interface=intf is not None,
            is_interface_only=impl is None,
        )

        loc_source = impl if impl is not None else (intf or "")
        info.loc = self.count_loc(loc_source)

        opens: Counter[str] = Counter()
        includes: Counter[str] = Counter()
        refs: Counter[str] = Counter()
        functor_apps: list[tuple[str, str]] = []
        submodules: list[str] = []
        local_mods: set[str] = set()

        for raw in (impl, intf):
            if raw is None:
                continue
            text = strip_comments_and_strings(raw)
            opens.update(self._find_opens(text))
            includes.update(self._find_includes(text))
            refs.update(self._find_qualified_refs(text))
            functor_apps.extend(self._find_functor_apps(text))
            submodules.extend(self._find_submodules(text))
            for m in _LOCAL_MODULE_RE.finditer(text):
                local_mods.add(m.group(1))
            for m in _LOCAL_AND_MODULE_RE.finditer(text):
                local_mods.add(m.group(1))
            for p in self._find_functor_params(text):
                local_mods.add(p)

        # The interface (when present) defines the exported type contract.
        interface_text = strip_comments_and_strings(intf if intf is not None else (impl or ""))
        info.exported_types, info.abstract_types = self._count_type_declarations(interface_text)
        info.defines_type_t = bool(
            re.search(r"\btype\s+(?:rec\s+)?(?:'[^=\s]+\s+)*t\b(?!\w)", interface_text)
        )

        info.opens = dict(opens)
        info.includes = dict(includes)
        info.qualified_refs = dict(refs)
        info.functor_apps = sorted(set(functor_apps))
        info.submodules = sorted(set(submodules))
        info.local_modules = sorted(local_mods)
        return info

    # ------------------------------------------------------------------
    # Individual extractors
    # ------------------------------------------------------------------

    def _find_opens(self, text: str) -> Counter[str]:
        found: Counter[str] = Counter()
        for m in _OPEN_RE.finditer(text):
            target = m.group(1) or m.group(2)
            if target:
                found[target] += 1
        return found

    def _find_includes(self, text: str) -> Counter[str]:
        found: Counter[str] = Counter()
        for m in _INCLUDE_RE.finditer(text):
            found[m.group(1)] += 1
        return found

    def _find_qualified_refs(self, text: str) -> Counter[str]:
        found: Counter[str] = Counter()
        for m in _QUALIFIED_RE.finditer(text):
            ident = m.group(1) or m.group(2)
            if ident and ident.split(".")[0] not in _NON_MODULE_UPPER:
                found[ident] += 1
        return found

    def _find_functor_apps(self, text: str) -> list[tuple[str, str]]:
        """Extract ``(functor, argument)`` pairs from ``module M = F (Arg)`` bindings."""
        apps: list[tuple[str, str]] = []
        for m in _FUNCTOR_APP_RE.finditer(text):
            functor, args_raw = m.group(2), m.group(3)
            if args_raw.strip().startswith("struct"):
                continue  # inline anonymous struct argument
            for arg in re.findall(r"\b([A-Z][A-Za-z0-9_'.]*)\b", args_raw):
                apps.append((functor, arg))
        return apps

    def _find_submodules(self, text: str) -> list[str]:
        return [m.group(1) for m in _SUBMODULE_RE.finditer(text)]

    @staticmethod
    def _skip_matching_paren(text: str, start: int) -> int:
        """Given start pointing at '(', return index immediately after the matching ')'."""
        depth = 0
        i = start
        n = len(text)
        while i < n:
            c = text[i]
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    return i + 1
            i += 1
        return n

    def _find_functor_params(self, text: str) -> list[str]:
        """Extract all formal module parameters from functor definitions and types.

        Handles multi-parameter functors (e.g. ``module M (A : SA) (B : SB) =``)
        and functor type expressions (e.g. ``functor (A : SA) ->``).
        """
        params: list[str] = []
        n = len(text)
        for m in _FUNCTOR_HEAD_RE.finditer(text):
            pos = m.end()
            while pos < n:
                while pos < n and text[pos].isspace():
                    pos += 1
                if pos < n and text[pos] == "(":
                    pm = _PARAM_START_RE.match(text, pos)
                    if pm:
                        params.append(pm.group(1))
                    pos = self._skip_matching_paren(text, pos)
                else:
                    break
        return params

    def _count_type_declarations(self, text: str) -> tuple[int, int]:
        """Count (total, abstract) type declarations; abstract = no ``=`` in the decl region."""
        total = abstract = 0
        for m in _TYPE_RE.finditer(text):
            prefix = text[max(0, m.start() - 8) : m.start()]
            if prefix.rstrip().endswith("module"):
                continue  # skip ``module type X``
            total += 1
            end_m = _DECL_END_RE.search(text, m.end())
            region = text[m.end() : end_m.start() if end_m else len(text)]
            if "=" not in region:
                abstract += 1
        return total, abstract

    @staticmethod
    def module_name_of(stem: str) -> str:
        """OCaml module name of a file stem: first letter uppercased, rest preserved."""
        return stem[:1].upper() + stem[1:] if stem else stem

    @staticmethod
    def count_loc(source: str) -> int:
        """Non-blank lines of code."""
        return sum(1 for line in source.splitlines() if line.strip())


from pattern_detector.domain.rules.base import strip_comments_and_strings
