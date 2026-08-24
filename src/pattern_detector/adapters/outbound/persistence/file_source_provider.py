"""File-system based OCaml source code provider."""

from __future__ import annotations

import os
from pathlib import Path

from pattern_detector.ports.outbound import SourceProviderPort


class FileSourceProvider(SourceProviderPort):
    """Recursively retrieves OCaml source code files (.ml, .mli) from disk."""

    def get_sources(self, target_path: str, extensions: list[str] | None = None) -> dict[str, str]:
        exts = extensions or [".ml", ".mli"]
        target = Path(target_path).resolve()
        sources: dict[str, str] = {}

        if target.is_file():
            if any(str(target).endswith(ext) for ext in exts):
                sources[str(target)] = self._read_file(target)
            return sources

        if target.is_dir():
            for root, _, files in os.walk(target):
                if "/_build/" in root or "/.git/" in root or "/_opam/" in root or "/node_modules/" in root:
                    continue
                for file in files:
                    if any(file.endswith(ext) for ext in exts):
                        full_path = Path(root) / file
                        sources[str(full_path)] = self._read_file(full_path)

        return sources

    def _read_file(self, path: Path) -> str:
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            return ""
