"""Architecture & dependency graph analysis domain (Dune-aware OCaml topology)."""

from pattern_detector.domain.architecture.cycle_detector import (
    detect_cycles,
    strongly_connected_components,
)
from pattern_detector.domain.architecture.metrics import (
    ModuleMetrics,
    compute_module_metrics,
)
from pattern_detector.domain.architecture.models import (
    ArchEdge,
    ArchIssue,
    ArchIssueKind,
    ArchitectureScanResult,
    ArchLayer,
    ComponentGraph,
    CycleGroup,
    EdgeKind,
    IssueSeverity,
    ModuleNode,
    infer_layer,
    layer_label,
)

__all__ = [
    "ArchEdge",
    "ArchIssue",
    "ArchIssueKind",
    "ArchLayer",
    "ArchitectureScanResult",
    "ComponentGraph",
    "CycleGroup",
    "EdgeKind",
    "IssueSeverity",
    "ModuleMetrics",
    "ModuleNode",
    "compute_module_metrics",
    "detect_cycles",
    "infer_layer",
    "layer_label",
    "strongly_connected_components",
]
