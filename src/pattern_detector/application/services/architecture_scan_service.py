"""Application service orchestrating the architecture & dependency graph scan.

Pipeline (implements ScanArchitectureUseCase):

1. Collect ``.ml``/``.mli`` sources through SourceProviderPort.
2. Parse the Dune build topology through DuneManifestParserPort.
3. Extract per-compilation-unit dependency facts (open/include/functor/ref).
4. Build the ComponentGraph: Dune-wrap-aware module ids, layer classification.
5. Analyse: Tarjan cycles, Martin metrics, architecture issues.
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Protocol

from pattern_detector.domain.architecture.cycle_detector import detect_cycles
from pattern_detector.domain.architecture.metrics import ModuleMetrics, attach_metrics
from pattern_detector.domain.architecture.models import (
    FORBIDDEN_LAYER_DEPENDENCIES,
    ArchEdge,
    ArchIssue,
    ArchIssueKind,
    ArchitectureScanResult,
    ComponentGraph,
    CycleGroup,
    EdgeKind,
    IssueSeverity,
    ModuleNode,
    infer_layer,
    layer_label,
)
from pattern_detector.ports.inbound.arch_scanner_port import (
    ArchScanOptions,
    ScanArchitectureUseCase,
)
from pattern_detector.ports.outbound import SourceProviderPort
from pattern_detector.ports.outbound.dune_parser_port import (
    DuneLibraryStanza,
    DuneManifestParserPort,
    DuneProjectTree,
)

if TYPE_CHECKING:
    from pattern_detector.adapters.outbound.parsers.module_dep_extractor import (
        ModuleDependencyInfo,
    )


class ModuleFactsExtractorPort(Protocol):
    """Consumer-side port: raw OCaml sources -> per-compilation-unit dependency facts."""

    def extract(self, sources: dict[str, str]) -> dict[str, ModuleDependencyInfo]: ...


class _ResolutionIndex:
    """Lookup structures implementing Dune module-path resolution semantics."""

    def __init__(self, nodes: dict[str, ModuleNode]) -> None:
        self.nodes = nodes
        self.wrap_prefixes: dict[str, str] = {}  # "Arch_domain" -> library name
        self.siblings: dict[str, dict[str, str]] = {}  # library name -> module -> node id
        self.top_level_ids: dict[str, str] = {}  # bare name -> id (unwrapped / dune-less)
        self.wrapped_by_name: dict[str, list[str]] = {}  # bare name -> wrapped ids

    def register(self, node_id: str, module_name: str, library: str, wrapped: bool) -> None:
        if wrapped:
            self.wrapped_by_name.setdefault(module_name, []).append(node_id)
            self.siblings.setdefault(library, {})[module_name] = node_id
            self.wrap_prefixes[node_id.rsplit(".", 1)[0]] = library
        else:
            self.top_level_ids.setdefault(module_name, node_id)

    def resolve(self, target_name: str, source_lib: str) -> str | None:
        """Resolve a raw reference from ``source_lib`` to a graph node id, or None."""
        parts = target_name.split(".")
        head = parts[0]

        # Explicit cross-library path: ``Arch_infra.Db`` / ``Arch_infra.Db.query``.
        if len(parts) >= 2 and head in self.wrap_prefixes:
            candidate = f"{head}.{parts[1]}"
            return candidate if candidate in self.nodes else None

        # Sibling module inside the same wrapped library (``open Types``).
        sibling = self.siblings.get(source_lib, {}).get(head)
        if sibling is not None:
            return sibling

        # Bare module of an unwrapped library / dune-less project.
        if head in self.top_level_ids:
            return self.top_level_ids[head]

        # Unique wrapped module with this name anywhere in the project.
        matches = [nid for nid in self.wrapped_by_name.get(head, []) if nid in self.nodes]
        if len(matches) == 1:
            return matches[0]
        return None


class ArchitectureScanService(ScanArchitectureUseCase):
    """End-to-end architecture scanning orchestrator for Dune/OCaml projects."""

    #: Issue detection thresholds.
    GOD_MODULE_LOC = 400
    HUB_MODULE_CE = 15
    INTERFACE_BYPASS_CA = 3

    _KIND_PRIORITY: ClassVar[dict[EdgeKind, int]] = {
        EdgeKind.OPEN: 3,
        EdgeKind.INCLUDE: 2,
        EdgeKind.FUNCTOR_APPLICATION: 1,
        EdgeKind.QUALIFIED_REFERENCE: 0,
    }

    def __init__(
        self,
        source_provider: SourceProviderPort,
        dune_parser: DuneManifestParserPort,
        extractor: ModuleFactsExtractorPort,
    ) -> None:
        self._source_provider = source_provider
        self._dune_parser = dune_parser
        self._extractor = extractor

    def scan_architecture(self, path: str, options: ArchScanOptions | None = None) -> ArchitectureScanResult:
        options = options or ArchScanOptions()
        t0 = time.perf_counter()

        root = Path(path).resolve()
        sources = self._source_provider.get_sources(
            path,
            extensions=[".ml", ".mli"],
            exclude_dirs=options.exclude_dirs,
        )
        tree = self._dune_parser.parse_project(str(root))
        units = self._extractor.extract(sources)

        graph = self._build_graph(root, tree, units)
        cycles = detect_cycles(graph)
        self._mark_cycles(graph, cycles)
        metrics = attach_metrics(graph)
        issues = self._collect_issues(graph, cycles, metrics)

        return ArchitectureScanResult(
            project_path=str(root),
            has_dune_manifest=bool(tree.manifests or tree.dune_project),
            files_scanned=len(sources),
            modules_count=len(graph.nodes),
            edges_count=len(graph.edges),
            elapsed_seconds=round(time.perf_counter() - t0, 3),
            graph=graph,
            cycles=cycles,
            issues=issues,
        )

    # ------------------------------------------------------------------
    # Graph construction
    # ------------------------------------------------------------------

    def _build_graph(
        self,
        root: Path,
        tree: DuneProjectTree,
        units: dict[str, ModuleDependencyInfo],
    ) -> ComponentGraph:
        graph = ComponentGraph(project_path=str(root))
        index = _ResolutionIndex(graph.nodes)
        entry_modules = self._entry_modules(tree)
        node_id_by_unit: dict[str, str] = {}

        # Pass 1: create nodes with Dune-wrap-aware ids.
        for unit_key, info in units.items():
            lib = tree.library_for_file(info.file_path)
            wrap = self._wrap_prefix(lib) if lib is not None and lib.wrapped else ""

            module = info.module_name
            node_id = f"{wrap}.{module}" if wrap else module
            if not wrap and lib is not None and node_id in graph.nodes:
                # Unwrapped collision between libraries: qualify with the wrap name.
                node_id = f"{self._wrap_prefix(lib)}.{module}"

            graph.nodes[node_id] = ModuleNode(
                id=node_id,
                name=module,
                file_path=info.file_path,
                loc=info.loc,
                dune_library=lib.name if lib is not None else "",
                layer=infer_layer(self._relative_parts(root, info.file_path), module),
                has_interface=info.has_interface,
                is_entry=self._is_entry(info.file_path, module, entry_modules),
                is_abstract=info.has_interface and info.abstract_types > 0,
                exported_types=info.exported_types,
                abstract_types=info.abstract_types,
                submodules=info.submodules,
            )
            node_id_by_unit[unit_key] = node_id
            index.register(node_id, module, lib.name if lib is not None else "", bool(wrap))

        # Pass 2: resolve references and emit one aggregated edge per module pair.
        pending: dict[tuple[str, str], tuple[EdgeKind, int]] = {}
        for unit_key, info in units.items():
            source_id = node_id_by_unit[unit_key]
            source_lib = graph.nodes[source_id].dune_library

            wants: list[tuple[str, EdgeKind, int]] = []
            wants.extend((t, EdgeKind.OPEN, w) for t, w in info.opens.items())
            wants.extend((t, EdgeKind.INCLUDE, w) for t, w in info.includes.items())
            wants.extend((t, EdgeKind.QUALIFIED_REFERENCE, w) for t, w in info.qualified_refs.items())
            for functor, argument in info.functor_apps:
                wants.append((functor, EdgeKind.FUNCTOR_APPLICATION, 1))
                wants.append((argument, EdgeKind.FUNCTOR_APPLICATION, 1))

            for target_name, kind, weight in wants:
                target_id = index.resolve(target_name, source_lib)
                if target_id is None or target_id == source_id:
                    continue  # stdlib / unresolved / self-reference
                self._accumulate(pending, source_id, target_id, kind, weight)

        for (source_id, target_id), (kind, weight) in pending.items():
            source_lib = graph.nodes[source_id].dune_library
            target_lib = graph.nodes[target_id].dune_library
            graph.edges.append(
                ArchEdge(
                    source=source_id,
                    target=target_id,
                    kind=kind,
                    weight=weight,
                    cross_library=bool(source_lib) and bool(target_lib) and source_lib != target_lib,
                    cross_layer=graph.nodes[source_id].layer != graph.nodes[target_id].layer,
                )
            )

        local_names = tree.local_library_names
        graph.library_deps = {
            lib.name: [d for d in lib.libraries if d in local_names]
            for lib in tree.libraries
            if any(d in local_names for d in lib.libraries)
        }
        graph.external_deps = tree.external_dependencies()
        return graph

    def _accumulate(
        self,
        pending: dict[tuple[str, str], tuple[EdgeKind, int]],
        source: str,
        target: str,
        kind: EdgeKind,
        weight: int,
    ) -> None:
        existing = pending.get((source, target))
        if existing is None:
            pending[(source, target)] = (kind, weight)
            return
        best_kind, total = existing
        if self._KIND_PRIORITY[kind] > self._KIND_PRIORITY[best_kind]:
            best_kind = kind
        pending[(source, target)] = (best_kind, total + weight)

    # ------------------------------------------------------------------
    # Analysis helpers
    # ------------------------------------------------------------------

    def _mark_cycles(self, graph: ComponentGraph, cycles: list[CycleGroup]) -> None:
        for group in cycles:
            for member in group.members:
                if member in graph.nodes:
                    graph.nodes[member].cycle_id = group.cycle_id

    def _collect_issues(
        self,
        graph: ComponentGraph,
        cycles: list[CycleGroup],
        metrics: dict[str, ModuleMetrics],
    ) -> list[ArchIssue]:
        issues: list[ArchIssue] = []

        for group in cycles:
            chain = " -> ".join([*group.members, group.members[0]])
            label = "cross-library " if group.cross_library else ""
            issues.append(
                ArchIssue(
                    severity=IssueSeverity.ERROR,
                    kind=ArchIssueKind.CIRCULAR_DEPENDENCY,
                    subject=group.members[0],
                    message=f"{label}circular dependency of {len(group.members)} modules: {chain}",
                    related=group.members,
                )
            )

        for edge in graph.edges:
            source_layer = graph.nodes[edge.source].layer
            target_layer = graph.nodes[edge.target].layer
            if target_layer in FORBIDDEN_LAYER_DEPENDENCIES.get(source_layer, set()):
                issues.append(
                    ArchIssue(
                        severity=IssueSeverity.WARNING,
                        kind=ArchIssueKind.LAYER_VIOLATION,
                        subject=edge.source,
                        message=(
                            f"layer inversion: {edge.source} ({layer_label(source_layer)}) depends on "
                            f"{edge.target} ({layer_label(target_layer)})"
                        ),
                        related=[edge.source, edge.target],
                    )
                )

        for node_id, node in graph.nodes.items():
            m = metrics.get(node_id)
            ca = m.ca if m else 0
            ce = m.ce if m else 0

            if node.loc >= self.GOD_MODULE_LOC:
                issues.append(
                    ArchIssue(
                        severity=IssueSeverity.WARNING,
                        kind=ArchIssueKind.GOD_MODULE,
                        subject=node_id,
                        message=f"god module: {node.name} has {node.loc} lines of code",
                    )
                )
            if ce >= self.HUB_MODULE_CE:
                issues.append(
                    ArchIssue(
                        severity=IssueSeverity.INFO,
                        kind=ArchIssueKind.HUB_MODULE,
                        subject=node_id,
                        message=f"hub/spaghetti module: {node.name} depends on {ce} other modules",
                    )
                )
            if not node.has_interface and ca >= self.INTERFACE_BYPASS_CA:
                issues.append(
                    ArchIssue(
                        severity=IssueSeverity.INFO,
                        kind=ArchIssueKind.INTERFACE_BYPASS,
                        subject=node_id,
                        message=f"interface bypass: {node.name} is used by {ca} modules but has no .mli contract",
                    )
                )
            if ca == 0 and not node.is_entry:
                issues.append(
                    ArchIssue(
                        severity=IssueSeverity.INFO,
                        kind=ArchIssueKind.ORPHAN_MODULE,
                        subject=node_id,
                        message=f"orphan module: nothing depends on {node.name} and it is not an entry point",
                    )
                )

        rank = {IssueSeverity.ERROR: 0, IssueSeverity.WARNING: 1, IssueSeverity.INFO: 2}
        issues.sort(key=lambda i: (rank[i.severity], i.kind.value, i.subject))
        return issues

    # ------------------------------------------------------------------
    # Small utilities
    # ------------------------------------------------------------------

    @staticmethod
    def _wrap_prefix(lib: DuneLibraryStanza) -> str:
        """Dune wrapper module prefix of a library (``arch_domain`` -> ``Arch_domain``)."""
        return lib.name[:1].upper() + lib.name[1:]

    @staticmethod
    def _entry_modules(tree: DuneProjectTree) -> set[tuple[str, str]]:
        """(directory, module name) of every executable target in the project."""
        entries: set[tuple[str, str]] = set()
        for manifest in tree.manifests:
            for exe in manifest.executables:
                for name in exe.names:
                    if name:
                        entries.add((manifest.directory, name[:1].upper() + name[1:]))
        return entries

    @staticmethod
    def _is_entry(file_path: str, module_name: str, entry_modules: set[tuple[str, str]]) -> bool:
        return (str(Path(file_path).parent), module_name) in entry_modules

    @staticmethod
    def _relative_parts(root: Path, file_path: str) -> tuple[str, ...]:
        try:
            return Path(file_path).relative_to(root).parts[:-1]
        except ValueError:
            return ()
