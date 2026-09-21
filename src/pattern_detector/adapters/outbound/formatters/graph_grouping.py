"""Shared grouping/view-filtering logic for all architecture graph exporters."""

from __future__ import annotations

from pathlib import Path

from pattern_detector.domain.architecture.models import (
    ArchitectureScanResult,
    ModuleNode,
)


def group_key(node: ModuleNode, group_by: str, project_root: str) -> str:
    """Stable group label of a module for the requested grouping mode."""
    if group_by == "layer":
        return node.layer.value
    if group_by == "directory":
        try:
            parts = Path(node.file_path).relative_to(project_root).parts[:-1]
        except ValueError:
            return "(root)"
        return "/".join(parts) if parts else "(root)"
    return node.dune_library or "(no library)"


def visible_nodes(result: ArchitectureScanResult, show_cycles_only: bool) -> list[ModuleNode]:
    """Nodes to render: all, or only members of circular dependency groups."""
    if not show_cycles_only:
        return list(result.graph.nodes.values())
    return [n for n in result.graph.nodes.values() if n.cycle_id is not None]


def grouped_nodes(
    result: ArchitectureScanResult,
    group_by: str,
    show_cycles_only: bool,
) -> list[tuple[str, list[ModuleNode]]]:
    """Nodes bucketed into ordered (group label, members) pairs."""
    buckets: dict[str, list[ModuleNode]] = {}
    for node in visible_nodes(result, show_cycles_only):
        buckets.setdefault(group_key(node, group_by, result.project_path), []).append(node)

    ordered: list[tuple[str, list[ModuleNode]]] = []
    for label in sorted(buckets, key=lambda k: (k == "(no library)", k.lower())):
        ordered.append((label, sorted(buckets[label], key=lambda n: n.id)))
    return ordered


def cycle_edge_pairs(result: ArchitectureScanResult) -> set[tuple[str, str]]:
    """(source, target) pairs whose both endpoints share a cycle group."""
    pairs: set[tuple[str, str]] = set()
    for edge in result.graph.edges:
        src = result.graph.nodes.get(edge.source)
        tgt = result.graph.nodes.get(edge.target)
        if (
            src is not None
            and tgt is not None
            and src.cycle_id is not None
            and src.cycle_id == tgt.cycle_id
        ):
            pairs.add((edge.source, edge.target))
    return pairs
