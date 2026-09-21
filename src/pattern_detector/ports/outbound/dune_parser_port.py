"""Outbound (driven) port: parsing Dune build manifests (dune / dune-project)."""

from __future__ import annotations

from typing import Protocol

from pydantic import BaseModel, Field


class DuneLibraryStanza(BaseModel):
    """A ``(library ...)`` stanza discovered in a dune file."""

    name: str
    public_name: str | None = None
    libraries: list[str] = Field(default_factory=list)
    wrapped: bool = True
    directory: str = ""


class DuneExecutableStanza(BaseModel):
    """An ``(executable ...)`` / ``(executables ...)`` stanza discovered in a dune file."""

    names: list[str] = Field(default_factory=list)
    public_names: list[str] = Field(default_factory=list)
    libraries: list[str] = Field(default_factory=list)
    directory: str = ""


class DuneManifest(BaseModel):
    """All buildable stanzas declared by one dune file (one directory)."""

    path: str
    directory: str
    libraries: list[DuneLibraryStanza] = Field(default_factory=list)
    executables: list[DuneExecutableStanza] = Field(default_factory=list)


class DuneProjectInfo(BaseModel):
    """Metadata extracted from the root dune-project file."""

    path: str = ""
    lang_version: str = ""
    packages: list[str] = Field(default_factory=list)
    project_name: str = ""


class DuneProjectTree(BaseModel):
    """Aggregated Dune build context of an OCaml project."""

    project_root: str
    dune_project: DuneProjectInfo | None = None
    manifests: list[DuneManifest] = Field(default_factory=list)

    @property
    def libraries(self) -> list[DuneLibraryStanza]:
        """All library stanzas across the project."""
        return [lib for m in self.manifests for lib in m.libraries]

    @property
    def local_library_names(self) -> set[str]:
        """Internal (dune ``name``) identifiers of every local library."""
        return {lib.name for lib in self.libraries}

    def library_for_file(self, file_path: str) -> DuneLibraryStanza | None:
        """Find the library stanza owning a given source file (by directory containment)."""
        for lib in self.libraries:
            if file_path.startswith(lib.directory):
                return lib
        return None

    def external_dependencies(self) -> dict[str, list[str]]:
        """Map each local library to its non-local (opam) dependencies."""
        local = self.local_library_names
        external: dict[str, list[str]] = {}
        for lib in self.libraries:
            deps = sorted({d for d in lib.libraries if d not in local})
            if deps:
                external[lib.name] = deps
        return external


class DuneManifestParserPort(Protocol):
    """Port for parsing dune / dune-project S-expression manifests into DuneProjectTree."""

    def parse_project(self, project_root: str) -> DuneProjectTree:
        ...
