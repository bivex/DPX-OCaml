"""Robert C. Martin architecture metrics for OCaml component graphs.

Implements the classic package metrics adapted to OCaml compilation units:

* ``Ca`` (Afferent coupling)  — how many modules depend on this module.
* ``Ce`` (Efferent coupling)  — how many modules this module depends on.
* ``I``  (Instability)        — ``I = Ce / (Ca + Ce)``; 0 = maximally stable, 1 = maximally unstable.
* ``A``  (Abstractness)       — ratio of abstract type declarations in the module interface
                                 (a module without any type falls back to its interface contract:
                                 ``1.0`` with a ``.mli``, ``0.0`` without).
* ``D``  (Distance from the Main Sequence) — ``|A + I - 1|``; 0 sits on the balanced axis,
                                 ~1 lands in the "Zone of Pain" / "Zone of Uselessness".
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from pattern_detector.domain.architecture.models import ComponentGraph


class ModuleMetrics(BaseModel):
    """Martin coupling metrics for a single OCaml module (component)."""

    ca: int = 0
    ce: int = 0
    instability: float = 0.0
    abstractness: float = 0.0
    main_sequence_distance: float = 0.0

    @property
    def zone(self) -> str:
        """Qualitative placement relative to Martin's Main Sequence."""
        if self.main_sequence_distance >= 0.7:
            return "zone of pain" if self.instability < 0.5 else "zone of uselessness"
        return "balanced"


def compute_module_metrics(graph: ComponentGraph) -> dict[str, ModuleMetrics]:
    """Compute Ca/Ce/I/A/D for every node of the component graph."""
    adjacency = graph.adjacency()
    reverse = graph.reverse_adjacency()

    metrics: dict[str, ModuleMetrics] = {}
    for node_id, node in graph.nodes.items():
        ca = len(reverse.get(node_id, set()))
        ce = len(adjacency.get(node_id, set()))

        if ca + ce > 0:
            instability = ce / (ca + ce)
        else:
            instability = 0.0

        if node.exported_types > 0:
            abstractness = node.abstract_types / node.exported_types
        else:
            abstractness = 1.0 if node.has_interface else 0.0

        metrics[node_id] = ModuleMetrics(
            ca=ca,
            ce=ce,
            instability=round(instability, 3),
            abstractness=round(abstractness, 3),
            main_sequence_distance=round(abs(abstractness + instability - 1.0), 3),
        )
    return metrics


def attach_metrics(graph: ComponentGraph) -> dict[str, ModuleMetrics]:
    """Compute metrics for the graph and attach them to each ModuleNode in place."""
    metrics = compute_module_metrics(graph)
    for node_id, m in metrics.items():
        if node_id in graph.nodes:
            graph.nodes[node_id].metrics = m
    return metrics
