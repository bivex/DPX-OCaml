"""Application service building the normalized ``architecture.json`` snapshot.

Combines the three analysis pipelines of DPX into a single JSON document that
the interactive Architecture Viewer (and any external tooling) consumes:

* **Architecture scan** (``ScanArchitectureUseCase``) — module graph with
  Dune-wrap-aware ids, layers, cycles, Martin metrics, architecture issues and
  per-edge ``file:line:col`` evidence (``EdgeLocation``).
* **Pattern scan** (``ParserPort`` + ``DetectorPort``) — the 25 design-pattern
  and safety-rule detections, joined to modules by source file.
* **Code model entities** — exported types and functions per module (with
  cyclomatic complexity), for the Module Detail inspector.

The snapshot is a plain JSON-serializable dict (schema versioned) — no domain
objects leak into the presentation layer.
"""

from __future__ import annotations

import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from pattern_detector.domain.architecture.models import ArchitectureScanResult
from pattern_detector.domain.code_model import ModuleModel
from pattern_detector.domain.detection import Detection
from pattern_detector.ports.inbound import DetectorPort, ScanOptions
from pattern_detector.ports.inbound.arch_scanner_port import (
    ArchScanOptions,
    ScanArchitectureUseCase,
)
from pattern_detector.ports.outbound import ParserPort, SourceProviderPort

#: Cap on entities (types + functions) serialised per module.
MAX_ENTITIES_PER_MODULE = 300

#: Cap on locations listed per edge in the snapshot.
MAX_LOCATIONS_PER_EDGE = 50


class ViewerSnapshotService:
    """Builds the normalized viewer snapshot (``architecture.json``) for a project."""

    SCHEMA_VERSION = "1.0.0"

    def __init__(
        self,
        arch_service: ScanArchitectureUseCase,
        source_provider: SourceProviderPort,
        parser: ParserPort,
        detector: DetectorPort,
    ) -> None:
        self._arch_service = arch_service
        self._source_provider = source_provider
        self._parser = parser
        self._detector = detector

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def build_snapshot(
        self,
        path: str,
        exclude_dirs: list[str] | None = None,
        include_patterns: bool = True,
    ) -> dict[str, Any]:
        """Produce the full JSON-ready snapshot dict for the project at ``path``."""
        t0 = time.perf_counter()
        root = Path(path).resolve()
        excludes = exclude_dirs or []

        arch = self._arch_service.scan_architecture(
            str(root), ArchScanOptions(exclude_dirs=excludes)
        )

        findings_by_file: dict[str, list[dict[str, Any]]] = {}
        entities_by_file: dict[str, dict[str, Any]] = {}
        if include_patterns:
            sources = self._source_provider.get_sources(
                str(root), extensions=[".ml", ".mli"], exclude_dirs=excludes
            )
            model = self._parser.parse_sources(sources)
            for detection in self._detector.detect_patterns(model, ScanOptions()):
                entry = self._finding_entry(detection)
                findings_by_file.setdefault(entry["file_abs"], []).append(entry)
            for mod in model.modules.values():
                file_key = str(Path(mod.file_path).resolve())
                entities_by_file[file_key] = self._entities_entry(mod)

        return self._assemble(root, arch, findings_by_file, entities_by_file, t0)

    # ------------------------------------------------------------------
    # Assembly
    # ------------------------------------------------------------------

    def _assemble(
        self,
        root: Path,
        arch: ArchitectureScanResult,
        findings_by_file: dict[str, list[dict[str, Any]]],
        entities_by_file: dict[str, dict[str, Any]],
        t0: float,
    ) -> dict[str, Any]:
        rel = self._relativizer(root)

        modules: list[dict[str, Any]] = []
        findings_total = 0
        for node_id in sorted(arch.graph.nodes):
            node = arch.graph.nodes[node_id]
            unit_keys = self._unit_keys(node.file_path)
            findings = sorted(
                (f for k in unit_keys for f in findings_by_file.get(k, [])),
                key=lambda f: (f["line"], f["column"], f["pattern"]),
            )
            for f in findings:
                f["node"] = node_id
                f["file"] = rel(f["file"])
            findings_total += len(findings)

            entities: dict[str, Any] = next(
                (entities_by_file[k] for k in unit_keys if k in entities_by_file),
                {"types": [], "functions": []},
            )

            entry: dict[str, Any] = {
                "id": node_id,
                "name": node.name,
                "file": rel(node.file_path),
                "loc": node.loc,
                "library": node.dune_library,
                "layer": node.layer.value,
                "has_interface": node.has_interface,
                "is_entry": node.is_entry,
                "is_abstract": node.is_abstract,
                "exported_types": node.exported_types,
                "abstract_types": node.abstract_types,
                "submodules": node.submodules,
                "cycle_id": node.cycle_id,
                "dir": rel(str(Path(node.file_path).parent)),
                "findings": [
                    {k: v for k, v in f.items() if k != "file_abs"} for f in findings
                ],
                "entities": entities,
            }
            if node.metrics is not None:
                entry["metrics"] = {
                    "ca": node.metrics.ca,
                    "ce": node.metrics.ce,
                    "instability": round(node.metrics.instability, 4),
                    "abstractness": round(node.metrics.abstractness, 4),
                    "distance": round(node.metrics.main_sequence_distance, 4),
                    "zone": node.metrics.zone,
                }
            modules.append(entry)

        edges: list[dict[str, Any]] = []
        for edge in sorted(arch.graph.edges, key=lambda e: (e.source, e.target)):
            edges.append(
                {
                    "source": edge.source,
                    "target": edge.target,
                    "kind": edge.kind.value,
                    "weight": edge.weight,
                    "cross_library": edge.cross_library,
                    "cross_layer": edge.cross_layer,
                    "locations": [
                        {
                            "file": rel(loc.file),
                            "line": loc.line,
                            "column": loc.column,
                            "occurrence": loc.occurrence,
                        }
                        for loc in edge.locations[:MAX_LOCATIONS_PER_EDGE]
                    ],
                }
            )

        return {
            "schema_version": self.SCHEMA_VERSION,
            "project": {
                "name": root.name,
                "path": str(root),
                "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),
                "has_dune_manifest": arch.has_dune_manifest,
            },
            "summary": {
                "files": arch.files_scanned,
                "modules": len(modules),
                "edges": len(edges),
                "cycles": len(arch.cycles),
                "issues": len(arch.issues),
                "findings": findings_total,
                "elapsed_seconds": round(time.perf_counter() - t0, 3),
            },
            "libraries": self._libraries(arch),
            "external_deps": sorted(arch.graph.external_deps),
            "modules": modules,
            "edges": edges,
            "cycles": [
                {"id": c.cycle_id, "members": c.members, "cross_library": c.cross_library}
                for c in arch.cycles
            ],
            "issues": [
                {
                    "severity": i.severity.value,
                    "kind": i.kind.value,
                    "subject": i.subject,
                    "message": i.message,
                    "related": i.related,
                }
                for i in arch.issues
            ],
        }

    def _libraries(self, arch: ArchitectureScanResult) -> list[dict[str, Any]]:
        """Per-Dune-library rollup derived from the graph nodes."""
        rollup: dict[str, dict[str, Any]] = {}
        for node in arch.graph.nodes.values():
            if not node.dune_library:
                continue
            lib = rollup.setdefault(
                node.dune_library, {"name": node.dune_library, "modules": 0, "loc": 0}
            )
            lib["modules"] += 1
            lib["loc"] += node.loc
        for name, lib in rollup.items():
            lib["depends_on"] = arch.graph.library_deps.get(name, [])
        return [rollup[name] for name in sorted(rollup)]

    # ------------------------------------------------------------------
    # Pattern findings & entities
    # ------------------------------------------------------------------

    @staticmethod
    def _finding_entry(detection: Detection) -> dict[str, Any]:
        loc = detection.primary_location
        return {
            "pattern": detection.pattern_type.value,
            "category": detection.pattern_category.value,
            "target": detection.target_name,
            "target_kind": detection.target_kind,
            "confidence": round(detection.confidence.score, 4),
            "level": detection.level.value,
            "message": detection.summary,
            "file": loc.file_path if loc else "",
            "line": loc.line if loc else 1,
            "column": loc.column if loc else 1,
            "file_abs": str(Path(loc.file_path).resolve()) if loc else "",
        }

    @staticmethod
    def _entities_entry(mod: ModuleModel) -> dict[str, Any]:
        """Types + functions of one CodeModel module, nested ones qualified."""
        types: list[dict[str, Any]] = []
        functions: list[dict[str, Any]] = []

        def walk(module: ModuleModel, prefix: str) -> None:
            for t in module.types.values():
                kinds = [
                    k
                    for k, flag in (
                        ("record", t.is_record),
                        ("variant", t.is_variant),
                        ("gadt", t.is_gadt),
                        ("poly_variant", t.is_polymorphic_variant),
                    )
                    if flag
                ]
                types.append(
                    {
                        "name": f"{prefix}{t.name}",
                        "kind": "+".join(kinds) if kinds else ("abstract" if t.is_abstract else "concrete"),
                        "abstract": t.is_abstract,
                        "line": t.location.line if t.location else 1,
                    }
                )
            for fn in module.functions.values():
                functions.append(
                    {
                        "name": f"{prefix}{fn.name}",
                        "arity": fn.arity,
                        "complexity": fn.cyclomatic_complexity,
                        "raises": fn.has_raise,
                        "line": fn.location.line if fn.location else 1,
                    }
                )
            for sub in module.submodules.values():
                walk(sub, f"{prefix}{sub.name}.")

        walk(mod, "")
        types.sort(key=lambda t: (t["line"], t["name"]))
        functions.sort(key=lambda f: (f["line"], f["name"]))
        return {
            "types": types[:MAX_ENTITIES_PER_MODULE],
            "functions": functions[: MAX_ENTITIES_PER_MODULE - min(len(types), MAX_ENTITIES_PER_MODULE)],
        }

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

    @staticmethod
    def _unit_keys(file_path: str) -> set[str]:
        """Join keys of one compilation unit: its own path plus the .ml/.mli sibling.

        Findings and entities may reference either side of the unit pair while
        the graph node carries only one canonical path, so both spellings map
        to the same module.
        """
        path = Path(file_path)
        keys = {str(path.resolve())}
        if path.suffix in {".ml", ".mli"}:
            keys.add(str(path.with_suffix(".ml").resolve()))
            keys.add(str(path.with_suffix(".mli").resolve()))
        return keys

    @staticmethod
    def _relativizer(root: Path):
        """File path formatter: repo-relative (posix) when under the project root."""

        def rel(path: str) -> str:
            try:
                return Path(path).resolve().relative_to(root).as_posix()
            except ValueError:
                return Path(path).as_posix()

        return rel
