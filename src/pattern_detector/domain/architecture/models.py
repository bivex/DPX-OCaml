"""Domain models for the OCaml Project Architecture & Dependency Graph Scanner.

Covers Dune-aware module topology (ModuleNode / ArchEdge / ComponentGraph),
architectural layer classification (Hexagonal / Clean Architecture) and
architecture anomaly reporting (ArchIssue).
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field

from pattern_detector.domain.architecture.metrics import ModuleMetrics


class EdgeKind(str, Enum):
    """Kind of dependency between two OCaml modules."""

    OPEN = "open"
    INCLUDE = "include"
    FUNCTOR_APPLICATION = "functor_application"
    QUALIFIED_REFERENCE = "qualified_reference"


class ArchLayer(str, Enum):
    """Architectural layer a module belongs to (Hexagonal / Clean Architecture roles)."""

    DOMAIN = "domain"
    PORTS = "ports"
    ADAPTERS = "adapters"
    INFRASTRUCTURE = "infrastructure"
    API = "api"
    SHARED = "shared"
    UNKNOWN = "unknown"


class IssueSeverity(str, Enum):
    """Severity of an architectural anomaly."""

    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class ArchIssueKind(str, Enum):
    """Taxonomy of detected architecture anomalies."""

    CIRCULAR_DEPENDENCY = "circular_dependency"
    LAYER_VIOLATION = "layer_violation"
    ORPHAN_MODULE = "orphan_module"
    GOD_MODULE = "god_module"
    HUB_MODULE = "hub_module"
    INTERFACE_BYPASS = "interface_bypass"


class ModuleNode(BaseModel):
    """A vertex of the component graph: one OCaml compilation unit (.ml [+ .mli])."""

    id: str
    name: str
    file_path: str
    loc: int = 0
    dune_library: str = ""
    layer: ArchLayer = ArchLayer.UNKNOWN
    has_interface: bool = False
    is_entry: bool = False
    is_abstract: bool = False
    exported_types: int = 0
    abstract_types: int = 0
    submodules: list[str] = Field(default_factory=list)
    cycle_id: int | None = None
    metrics: ModuleMetrics | None = None


class ArchEdge(BaseModel):
    """A directed dependency edge between two modules of the component graph."""

    source: str
    target: str
    kind: EdgeKind = EdgeKind.QUALIFIED_REFERENCE
    weight: int = 1
    cross_library: bool = False
    cross_layer: bool = False


class CycleGroup(BaseModel):
    """A strongly connected component of size > 1 (or a self-referencing module)."""

    cycle_id: int
    members: list[str]
    cross_library: bool = False


class ArchIssue(BaseModel):
    """A single architecture anomaly finding (cycle, layer inversion, god module...)."""

    severity: IssueSeverity
    kind: ArchIssueKind
    subject: str
    message: str
    related: list[str] = Field(default_factory=list)


class ComponentGraph(BaseModel):
    """Full DAG (with detected cycles) of OCaml module dependencies in a project."""

    project_path: str = ""
    nodes: dict[str, ModuleNode] = Field(default_factory=dict)
    edges: list[ArchEdge] = Field(default_factory=list)
    library_deps: dict[str, list[str]] = Field(default_factory=dict)
    external_deps: dict[str, list[str]] = Field(default_factory=dict)

    def adjacency(self) -> dict[str, set[str]]:
        """Outgoing adjacency map (module -> set of modules it depends on)."""
        adj: dict[str, set[str]] = {node_id: set() for node_id in self.nodes}
        for edge in self.edges:
            if edge.source != edge.target:
                adj.setdefault(edge.source, set()).add(edge.target)
        return adj

    def reverse_adjacency(self) -> dict[str, set[str]]:
        """Incoming adjacency map (module -> set of modules depending on it)."""
        radj: dict[str, set[str]] = {node_id: set() for node_id in self.nodes}
        for edge in self.edges:
            if edge.source != edge.target:
                radj.setdefault(edge.target, set()).add(edge.source)
        return radj

    def edge_lookup(self) -> dict[tuple[str, str], ArchEdge]:
        """Index of edges by (source, target) pair."""
        return {(e.source, e.target): e for e in self.edges}

    def library_of(self, node_id: str) -> str:
        """Dune library a node belongs to (empty string when not under Dune control)."""
        node = self.nodes.get(node_id)
        return node.dune_library if node else ""


class ArchitectureScanResult(BaseModel):
    """Complete outcome of one architecture scan pipeline execution."""

    project_path: str
    has_dune_manifest: bool
    files_scanned: int
    modules_count: int
    edges_count: int
    elapsed_seconds: float
    graph: ComponentGraph
    cycles: list[CycleGroup] = Field(default_factory=list)
    issues: list[ArchIssue] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Layer classification heuristics (Hexagonal / Clean Architecture)
# ---------------------------------------------------------------------------

_LAYER_PATH_HINTS: list[tuple[frozenset[str], ArchLayer]] = [
    (frozenset({"domain", "model", "models", "core"}), ArchLayer.DOMAIN),
    (frozenset({"port", "ports", "interfaces", "usecase", "usecases", "application"}), ArchLayer.PORTS),
    (frozenset({"adapter", "adapters", "controller", "controllers", "presenters", "routes"}), ArchLayer.ADAPTERS),
    (
        frozenset({"infra", "infrastructure", "db", "database", "persistence", "drivers", "external", "gateway", "repositories"}),
        ArchLayer.INFRASTRUCTURE,
    ),
    (frozenset({"api", "http", "rest", "graphql", "web", "cli", "bin", "cmd", "main", "exe", "entry", "entrypoint", "app", "server"}), ArchLayer.API),
    (frozenset({"utils", "util", "common", "shared", "helpers", "support", "stdlib"}), ArchLayer.SHARED),
]

#: Forbidden dependency directions between architectural layers (Clean Architecture:
#: dependencies must point inwards, Domain depends on nothing implementation-specific).
FORBIDDEN_LAYER_DEPENDENCIES: dict[ArchLayer, set[ArchLayer]] = {
    ArchLayer.DOMAIN: {ArchLayer.INFRASTRUCTURE, ArchLayer.ADAPTERS, ArchLayer.API},
    ArchLayer.PORTS: {ArchLayer.INFRASTRUCTURE, ArchLayer.ADAPTERS},
    ArchLayer.SHARED: {ArchLayer.DOMAIN, ArchLayer.PORTS},
}

_LAYER_LABELS: dict[ArchLayer, str] = {
    ArchLayer.DOMAIN: "Domain",
    ArchLayer.PORTS: "Ports (Application Core)",
    ArchLayer.ADAPTERS: "Adapters",
    ArchLayer.INFRASTRUCTURE: "Infrastructure",
    ArchLayer.API: "API / Entry Points",
    ArchLayer.SHARED: "Shared Utils",
    ArchLayer.UNKNOWN: "Unclassified",
}


def layer_label(layer: ArchLayer) -> str:
    """Human-friendly label for an architectural layer."""
    return _LAYER_LABELS[layer]


def infer_layer(relative_parts: tuple[str, ...], module_name: str = "") -> ArchLayer:
    """Classify a module into an architectural layer from its path (and name fallback).

    The outermost matching path segment wins: the first directory names the
    architectural boundary (``lib/domain/...`` -> DOMAIN, ``adapters/http/...``
    -> ADAPTERS even though ``http`` alone would suggest API).
    When no path segment matches, common entry-point names (Main, Cli, Server...)
    classify the module as an API entry point.
    """
    for segment in relative_parts:
        seg = segment.lower()
        for hints, layer in _LAYER_PATH_HINTS:
            if seg in hints:
                return layer
    if module_name.lower() in {"main", "cli", "app", "server", "daemon"}:
        return ArchLayer.API
    return ArchLayer.UNKNOWN
