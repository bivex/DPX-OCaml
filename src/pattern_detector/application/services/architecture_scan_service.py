"""Application service orchestrating the architecture & dependency graph scan.

Pipeline (implements ScanArchitectureUseCase):

1. Collect ``.ml``/``.mli`` sources through SourceProviderPort.
2. Parse the Dune build topology through DuneManifestParserPort.
3. Extract per-compilation-unit dependency facts (open/include/functor/ref).
4. Build the ComponentGraph: Dune-wrap-aware module ids, layer classification.
5. Analyse: Tarjan cycles, Martin metrics, architecture issues.
"""

from __future__ import annotations

import re
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
        self.dir_modules: dict[str, dict[str, str]] = {}  # directory path -> module -> node id
        self.scopes: dict[str, dict[str, str]] = {}  # node id -> {module name: target node id}

    def register(
        self,
        node_id: str,
        module_name: str,
        library: str,
        wrapped: bool,
        directory: str,
    ) -> None:
        if wrapped and library:
            self.siblings.setdefault(library, {})[module_name] = node_id
            self.wrap_prefixes[node_id.rsplit(".", 1)[0]] = library
        elif library:
            self.siblings.setdefault(library, {})[module_name] = node_id

        if directory:
            self.dir_modules.setdefault(directory, {})[module_name] = node_id

    def build_scopes(
        self,
        units: dict[str, ModuleDependencyInfo],
        node_id_by_unit: dict[str, str],
    ) -> None:
        """Compute bare module names brought into scope for each unit via open/include."""
        info_by_nid = {
            node_id_by_unit[uk]: info
            for uk, info in units.items()
            if uk in node_id_by_unit
        }
        memo: dict[str, dict[str, str]] = {}

        def get_scope(nid: str, visited: set[str]) -> dict[str, str]:
            if nid in memo:
                return memo[nid]
            if nid in visited:
                return {}
            visited.add(nid)

            scope: dict[str, str] = {}
            uinfo = info_by_nid.get(nid)
            if uinfo is None:
                return scope

            source_node = self.nodes.get(nid)
            source_lib = source_node.dune_library if source_node else ""
            source_dir = str(Path(uinfo.file_path).parent.resolve())

            for target in list(uinfo.opens) + list(uinfo.includes):
                # 1. Target is a library wrapper prefix (e.g. "Stdune", "Arch_infra")
                lib_name = self.wrap_prefixes.get(target) or self.wrap_prefixes.get(target.split(".")[0])
                if lib_name and lib_name in self.siblings:
                    scope.update(self.siblings[lib_name])

                # 2. Target is a module in the same library
                if source_lib:
                    sib_id = self.siblings.get(source_lib, {}).get(target)
                    if sib_id and sib_id != nid:
                        scope.update(get_scope(sib_id, visited.copy()))

                # 3. Target is a module in the same directory
                dir_sib = self.dir_modules.get(source_dir, {}).get(target)
                if dir_sib and dir_sib != nid:
                    scope.update(get_scope(dir_sib, visited.copy()))

            memo[nid] = scope
            return scope

        for nid in info_by_nid:
            self.scopes[nid] = get_scope(nid, set())

    def resolve(
        self,
        target_name: str,
        source_id: str,
        source_lib: str,
        source_dir: str,
        local_modules: set[str],
    ) -> str | None:
        """Resolve a raw reference from a source compilation unit to a graph node id, or None."""
        parts = target_name.split(".")
        head = parts[0]

        # References to locally defined modules, aliases, or functor parameters are intra-unit
        if head in local_modules:
            return None

        # Multi-segment qualified reference (e.g. "A.B" or "A.B.C")
        if len(parts) >= 2:
            # Longest matching path in self.nodes
            for i in range(len(parts), 1, -1):
                candidate = ".".join(parts[:i])
                if candidate in self.nodes:
                    return candidate

            # If parts[0] is in self.wrap_prefixes, it was an explicit cross-lib path like "Http.Header" or "Alcotest_engine.V1".
            if parts[0] in self.wrap_prefixes:
                wrap_id = f"{parts[0]}.{parts[0]}"
                if wrap_id in self.nodes:
                    return wrap_id
                return None

            # Sibling in source_lib? (e.g. "Order.describe" where "Order" is a sibling in source_lib)
            if source_lib:
                sib = self.siblings.get(source_lib, {}).get(parts[0])
                if sib is not None:
                    return sib

            # Sibling in source_dir?
            if source_dir:
                dir_sib = self.dir_modules.get(source_dir, {}).get(parts[0])
                if dir_sib is not None:
                    return dir_sib

            # In open scope?
            scoped = self.scopes.get(source_id, {}).get(parts[0])
            if scoped is not None:
                return scoped

            return None

        # Bare single-segment reference (len(parts) == 1):

        # Sibling in the same wrapped library
        if source_lib:
            sib = self.siblings.get(source_lib, {}).get(head)
            if sib is not None:
                return sib

        # Sibling in the same directory (unwrapped modules / exes)
        if source_dir:
            dir_sib = self.dir_modules.get(source_dir, {}).get(head)
            if dir_sib is not None:
                return dir_sib

        # In scope via open / include
        scoped = self.scopes.get(source_id, {}).get(head)
        if scoped is not None:
            return scoped

        # Explicit library wrapper module (e.g. `open Stdune` -> node `Stdune.Stdune`)
        if head in self.wrap_prefixes:
            wrap_id = f"{head}.{head}"
            if wrap_id in self.nodes:
                return wrap_id

        return None


class ArchitectureScanService(ScanArchitectureUseCase):
    """End-to-end architecture scanning orchestrator for Dune/OCaml projects."""

    GOD_MODULE_LOC = 400
    HUB_MODULE_CE = 15
    INTERFACE_BYPASS_CA = 3
    PAIN_ZONE_CA = 5
    PAIN_ZONE_MAX_I = 0.2
    PAIN_ZONE_MAX_A = 0.1
    PAIN_ZONE_MIN_LOC = 50
    USELESS_ZONE_MIN_A = 0.7
    LEAKY_INTERFACE_CA = 3

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
        issues = self._collect_issues(graph, cycles, metrics, tree)

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
            if lib is not None and lib.include_subdirs == "qualified" and lib.directory:
                try:
                    rel_parts = Path(info.file_path).parent.resolve().relative_to(Path(lib.directory).resolve()).parts
                    if rel_parts:
                        prefix_mod = ".".join(p[:1].upper() + p[1:] for p in rel_parts)
                        module = f"{prefix_mod}.{module}"
                except ValueError:
                    pass

            node_id = f"{wrap}.{module}" if wrap else module
            if node_id in graph.nodes:
                # Collision: disambiguate using directory relative parts
                rel = self._relative_parts(root, info.file_path)
                prefix = "_".join(rel) if rel else str(Path(info.file_path).parent.name)
                prefix = re.sub(r"[^A-Za-z0-9_]", "_", prefix)
                node_id = f"{prefix}.{module}"
                counter = 1
                base_id = node_id
                while node_id in graph.nodes:
                    node_id = f"{base_id}_{counter}"
                    counter += 1

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
            index.register(
                node_id=node_id,
                module_name=module,
                library=lib.name if lib is not None else "",
                wrapped=bool(wrap),
                directory=str(Path(info.file_path).parent.resolve()),
            )

        index.build_scopes(units, node_id_by_unit)

        # Pass 2: resolve references and emit one aggregated edge per module pair.
        pending: dict[tuple[str, str], tuple[EdgeKind, int]] = {}
        for unit_key, info in units.items():
            source_id = node_id_by_unit[unit_key]
            source_lib = graph.nodes[source_id].dune_library
            source_dir = str(Path(info.file_path).parent.resolve())
            source_local_mods = set(info.local_modules)

            wants: list[tuple[str, EdgeKind, int]] = []
            wants.extend((t, EdgeKind.OPEN, w) for t, w in info.opens.items())
            wants.extend((t, EdgeKind.INCLUDE, w) for t, w in info.includes.items())
            wants.extend((t, EdgeKind.QUALIFIED_REFERENCE, w) for t, w in info.qualified_refs.items())
            for functor, argument in info.functor_apps:
                wants.append((functor, EdgeKind.FUNCTOR_APPLICATION, 1))
                wants.append((argument, EdgeKind.FUNCTOR_APPLICATION, 1))

            for target_name, kind, weight in wants:
                target_id = index.resolve(
                    target_name,
                    source_id=source_id,
                    source_lib=source_lib,
                    source_dir=source_dir,
                    local_modules=source_local_mods,
                )
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
        tree: DuneProjectTree | None = None,
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

            if (
                m
                and ca >= self.PAIN_ZONE_CA
                and m.instability <= self.PAIN_ZONE_MAX_I
                and m.abstractness <= self.PAIN_ZONE_MAX_A
                and node.loc >= self.PAIN_ZONE_MIN_LOC
            ):
                issues.append(
                    ArchIssue(
                        severity=IssueSeverity.WARNING,
                        kind=ArchIssueKind.ZONE_OF_PAIN,
                        subject=node_id,
                        message=(
                            f"zone of pain: {node.name} is rigidly concrete (A={m.abstractness:.2f}) "
                            f"yet heavily depended on by {ca} modules (I={m.instability:.2f}, D={m.main_sequence_distance:.2f})"
                        ),
                    )
                )

            if (
                m
                and ca == 0
                and ce >= 1
                and not node.is_entry
                and m.abstractness >= self.USELESS_ZONE_MIN_A
                and node.exported_types >= 2
            ):
                issues.append(
                    ArchIssue(
                        severity=IssueSeverity.INFO,
                        kind=ArchIssueKind.ZONE_OF_USELESSNESS,
                        subject=node_id,
                        message=(
                            f"zone of uselessness: {node.name} is highly abstract (A={m.abstractness:.2f}) "
                            f"with {node.exported_types} types, but has no dependents (I={m.instability:.2f}, D={m.main_sequence_distance:.2f})"
                        ),
                    )
                )

            if (
                node.has_interface
                and ca >= self.LEAKY_INTERFACE_CA
                and node.exported_types >= 2
                and node.abstract_types == 0
            ):
                issues.append(
                    ArchIssue(
                        severity=IssueSeverity.INFO,
                        kind=ArchIssueKind.LEAKY_INTERFACE,
                        subject=node_id,
                        message=(
                            f"leaky interface: {node.name}.mli exports {node.exported_types} types, "
                            f"but none are abstract. Implementation details are fully exposed to {ca} clients."
                        ),
                    )
                )

        # Functor application anomalies: one-shot functors
        functor_apps: dict[str, list[str]] = {}
        for edge in graph.edges:
            if edge.kind is EdgeKind.FUNCTOR_APPLICATION:
                functor_apps.setdefault(edge.target, []).append(edge.source)

        for target_id, sources in functor_apps.items():
            if len(sources) == 1:
                target_node = graph.nodes.get(target_id)
                name = target_node.name if target_node else target_id
                issues.append(
                    ArchIssue(
                        severity=IssueSeverity.INFO,
                        kind=ArchIssueKind.ONE_SHOT_FUNCTOR,
                        subject=target_id,
                        message=(
                            f"one-shot functor: {name} is instantiated as a functor in only 1 place ({sources[0]}). "
                            f"Consider whether a simple record or higher-order function would suffice."
                        ),
                        related=[sources[0]],
                    )
                )

        if tree:
            _HAZARDOUS_UNWRAPPED_NAMES = {
                "Utils", "Util", "Config", "Types", "Common", "Helper", "Helpers",
                "Error", "Errors", "Log", "Logging",
            }
            local_libs_map: dict[str, DuneLibraryStanza] = {}
            for lib in tree.libraries:
                local_libs_map[lib.name] = lib
                if lib.public_name:
                    local_libs_map[lib.public_name] = lib

            declared_by_lib: dict[str, set[str]] = {
                lib.name: set(lib.libraries) for lib in tree.libraries
            }

            for lib in tree.libraries:
                # 1. Dead Library Dependencies (declared in (libraries ...) but never used)
                for dep in lib.libraries:
                    if dep in local_libs_map:
                        target_lib = local_libs_map[dep]
                        if target_lib.name == lib.name:
                            continue
                        has_edge = any(
                            graph.nodes[e.source].dune_library == lib.name
                            and graph.nodes[e.target].dune_library == target_lib.name
                            for e in graph.edges
                        )
                        if not has_edge:
                            issues.append(
                                ArchIssue(
                                    severity=IssueSeverity.WARNING,
                                    kind=ArchIssueKind.DEAD_LIBRARY_DEPENDENCY,
                                    subject=lib.name,
                                    message=(
                                        f"dead library dependency: library '{lib.name}' declares dependency on "
                                        f"'{dep}', but none of its modules use any module from it. "
                                        f"Remove to optimize Dune build graph parallelism."
                                    ),
                                    related=[target_lib.name],
                                )
                            )

                # 2. Missing public interface (.mli) for public library
                if lib.public_name:
                    candidates = {
                        lib.name[:1].upper() + lib.name[1:],
                    }
                    pub_short = lib.public_name.split(".")[-1].replace("-", "_")
                    candidates.add(pub_short[:1].upper() + pub_short[1:])

                    for node in graph.nodes.values():
                        if node.dune_library == lib.name and node.name in candidates and not node.has_interface:
                            issues.append(
                                ArchIssue(
                                    severity=IssueSeverity.WARNING,
                                    kind=ArchIssueKind.MISSING_PUBLIC_INTERFACE,
                                    subject=node.id,
                                    message=(
                                        f"missing public interface: library '{lib.public_name}' (name {lib.name}) "
                                        f"is public, but its facade module {node.name} has no .mli contract. "
                                        f"Internal symbols are unintentionally exposed as public API."
                                    ),
                                )
                            )

                # 3. Unwrapped namespace hazard: (wrapped false) with generic module names
                if not lib.wrapped:
                    for node in graph.nodes.values():
                        if node.dune_library == lib.name and node.name in _HAZARDOUS_UNWRAPPED_NAMES:
                            issues.append(
                                ArchIssue(
                                    severity=IssueSeverity.WARNING,
                                    kind=ArchIssueKind.UNWRAPPED_NAMESPACE_HAZARD,
                                    subject=node.id,
                                    message=(
                                        f"unwrapped namespace hazard: library '{lib.name}' has (wrapped false) "
                                        f"and exports generic module '{node.name}', risking linker collisions across projects."
                                    ),
                                )
                            )

            # 4. Undeclared library dependency: module uses symbols from lib_B but
            #    lib_A's dune stanza doesn't list lib_B in (libraries ...).
            reported_undeclared: set[tuple[str, str]] = set()
            for edge in graph.edges:
                if not edge.cross_library:
                    continue
                src_lib = graph.nodes[edge.source].dune_library
                tgt_lib = graph.nodes[edge.target].dune_library
                if not src_lib or not tgt_lib:
                    continue
                pair_key = (src_lib, tgt_lib)
                if pair_key in reported_undeclared:
                    continue
                declared = declared_by_lib.get(src_lib, set())
                tgt_stanza = local_libs_map.get(tgt_lib)
                if tgt_stanza is None:
                    continue
                names_to_check = {tgt_stanza.name}
                if tgt_stanza.public_name:
                    names_to_check.add(tgt_stanza.public_name)
                if not (declared & names_to_check):
                    reported_undeclared.add(pair_key)
                    issues.append(
                        ArchIssue(
                            severity=IssueSeverity.WARNING,
                            kind=ArchIssueKind.UNDECLARED_LIBRARY_DEPENDENCY,
                            subject=edge.source,
                            message=(
                                f"undeclared library dependency: module '{edge.source}' (library '{src_lib}') "
                                f"uses '{edge.target}' from library '{tgt_lib}', "
                                f"but '{src_lib}' does not list '{tgt_lib}' in its dune (libraries ...) stanza. "
                                f"This will fail at link time."
                            ),
                            related=[edge.target],
                        )
                    )

            # 5. Test reaching internals: a test stanza module directly imports
            #    a library-internal module instead of going through the public facade.
            test_dirs: set[str] = set()
            for manifest in tree.manifests:
                for exe in manifest.executables:
                    mdir = manifest.directory.lower().replace("\\", "/")
                    if any(seg in mdir for seg in ("/test", "/tests", "_test", "_tests")):
                        test_dirs.add(manifest.directory)
                        break

            for edge in graph.edges:
                if not edge.cross_library or not test_dirs:
                    continue
                src_node = graph.nodes.get(edge.source)
                tgt_node = graph.nodes.get(edge.target)
                if src_node is None or tgt_node is None:
                    continue
                src_dir = str(Path(src_node.file_path).parent.resolve())
                if not any(
                    src_dir.startswith(str(Path(td).resolve()))
                    for td in test_dirs
                ):
                    continue
                tgt_lib_name = tgt_node.dune_library
                tgt_stanza = local_libs_map.get(tgt_lib_name) if tgt_lib_name else None
                if tgt_stanza is None or tgt_stanza.public_name:
                    continue
                if not tgt_stanza.wrapped:
                    continue
                facade_name = self._wrap_prefix(tgt_stanza)
                if tgt_node.name != facade_name:
                    issues.append(
                        ArchIssue(
                            severity=IssueSeverity.WARNING,
                            kind=ArchIssueKind.TEST_REACHING_INTERNALS,
                            subject=edge.source,
                            message=(
                                f"test reaching internals: test module '{edge.source}' directly accesses "
                                f"internal module '{edge.target}' from library '{tgt_lib_name}', "
                                f"bypassing its public facade '{facade_name}'. "
                                f"Tests coupled to implementation details break on refactoring."
                            ),
                            related=[edge.target],
                        )
                    )

            # 4. Undeclared library dependency: module uses symbols from lib_B but
            #    lib_A's dune stanza doesn't list lib_B in (libraries ...).
            reported_undeclared: set[tuple[str, str]] = set()
            for edge in graph.edges:
                if not edge.cross_library:
                    continue
                src_lib = graph.nodes[edge.source].dune_library
                tgt_lib = graph.nodes[edge.target].dune_library
                if not src_lib or not tgt_lib:
                    continue
                pair_key = (src_lib, tgt_lib)
                if pair_key in reported_undeclared:
                    continue
                declared = declared_by_lib.get(src_lib, set())
                tgt_stanza = local_libs_map.get(tgt_lib)
                if tgt_stanza is None:
                    continue
                names_to_check = {tgt_stanza.name}
                if tgt_stanza.public_name:
                    names_to_check.add(tgt_stanza.public_name)
                if not (declared & names_to_check):
                    reported_undeclared.add(pair_key)
                    issues.append(
                        ArchIssue(
                            severity=IssueSeverity.WARNING,
                            kind=ArchIssueKind.UNDECLARED_LIBRARY_DEPENDENCY,
                            subject=edge.source,
                            message=(
                                f"undeclared library dependency: module '{edge.source}' (library '{src_lib}') "
                                f"uses '{edge.target}' from library '{tgt_lib}', "
                                f"but '{src_lib}' does not list '{tgt_lib}' in its dune (libraries ...) stanza. "
                                f"This will fail at link time."
                            ),
                            related=[edge.target],
                        )
                    )

            # 5. Test reaching internals: a test stanza module directly imports
            #    a library-internal module instead of going through the public facade.
            test_dirs: set[str] = set()
            for manifest in tree.manifests:
                for exe in manifest.executables:
                    mdir = manifest.directory.lower().replace("\\", "/")
                    if any(seg in mdir for seg in ("/test", "/tests", "_test", "_tests")):
                        test_dirs.add(manifest.directory)
                        break

            if test_dirs:
                for edge in graph.edges:
                    if not edge.cross_library:
                        continue
                    src_node = graph.nodes.get(edge.source)
                    tgt_node = graph.nodes.get(edge.target)
                    if src_node is None or tgt_node is None:
                        continue
                    src_dir = str(Path(src_node.file_path).parent.resolve())
                    if not any(
                        src_dir.startswith(str(Path(td).resolve()))
                        for td in test_dirs
                    ):
                        continue
                    tgt_lib_name = tgt_node.dune_library
                    tgt_stanza = local_libs_map.get(tgt_lib_name) if tgt_lib_name else None
                    if tgt_stanza is None or tgt_stanza.public_name:
                        continue
                    if not tgt_stanza.wrapped:
                        continue
                    facade_name = self._wrap_prefix(tgt_stanza)
                    if tgt_node.name != facade_name:
                        issues.append(
                            ArchIssue(
                                severity=IssueSeverity.WARNING,
                                kind=ArchIssueKind.TEST_REACHING_INTERNALS,
                                subject=edge.source,
                                message=(
                                    f"test reaching internals: test module '{edge.source}' directly accesses "
                                    f"internal module '{edge.target}' from library '{tgt_lib_name}', "
                                    f"bypassing its public facade '{facade_name}'. "
                                    f"Tests coupled to implementation details break on refactoring."
                                ),
                                related=[edge.target],
                            )
                        )

        # 6. Module name collision across libraries: two different local libraries
        #    export a module with the same bare name — silent shadowing when both are opened.
        name_to_libs: dict[str, list[str]] = {}
        for node in graph.nodes.values():
            if node.dune_library:
                name_to_libs.setdefault(node.name, []).append(node.dune_library)

        reported_collisions: set[frozenset[str]] = set()
        for mod_name, libs in name_to_libs.items():
            unique_libs = list(dict.fromkeys(libs))
            if len(unique_libs) < 2:
                continue
            key = frozenset(unique_libs)
            if key in reported_collisions:
                continue
            reported_collisions.add(key)
            libs_str = ", ".join(f"'{lib}'" for lib in unique_libs)
            issues.append(
                ArchIssue(
                    severity=IssueSeverity.WARNING,
                    kind=ArchIssueKind.MODULE_NAME_COLLISION,
                    subject=mod_name,
                    message=(
                        f"module name collision: module '{mod_name}' is defined in {len(unique_libs)} different "
                        f"libraries ({libs_str}). Simultaneously opening both causes silent shadowing "
                        f"and may produce subtle runtime bugs."
                    ),
                    related=unique_libs,
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
