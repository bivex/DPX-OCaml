"""Tarjan's strongly connected components algorithm for OCaml module dependency graphs.

An iterative (explicit stack) implementation is used so that large projects
(thousands of modules) never hit the Python recursion limit. Every SCC of size
greater than one — plus modules that depend on themselves — is a circular
dependency. Cycles spanning several Dune libraries are flagged as such, since
OCaml cannot break them with a local ``module rec``.
"""

from __future__ import annotations

from collections.abc import Iterator

from pattern_detector.domain.architecture.models import ComponentGraph, CycleGroup


def strongly_connected_components(adjacency: dict[str, set[str]]) -> list[list[str]]:
    """Iterative Tarjan SCC over ``adjacency`` (node -> outgoing neighbours).

    Returns components as sorted lists; singletons without a self-loop are
    filtered out, so the result contains only actual circular dependencies.
    """
    index: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    on_stack: set[str] = set()
    stack: list[str] = []
    components: list[list[str]] = []

    for start in sorted(adjacency):
        if start in index:
            continue

        # Explicit DFS stack: (node, iterator over its successors)
        work: list[tuple[str, Iterator[str]]] = [
            (start, iter(sorted(adjacency.get(start, set()))))
        ]
        while work:
            node, successors = work[-1]
            advanced = False

            if node not in index:
                index[node] = lowlink[node] = len(index)
                stack.append(node)
                on_stack.add(node)

            for succ in successors:
                if succ not in adjacency:
                    continue  # reference outside the graph (stdlib / unresolved)
                if succ not in index:
                    work.append((succ, iter(sorted(adjacency.get(succ, set())))))
                    advanced = True
                    break
                if succ in on_stack:
                    lowlink[node] = min(lowlink[node], index[succ])

            if advanced:
                continue

            # All successors processed: pop the DFS frame.
            work.pop()
            if work:
                parent = work[-1][0]
                lowlink[parent] = min(lowlink[parent], lowlink[node])

            if lowlink[node] == index[node]:
                component: list[str] = []
                while True:
                    member = stack.pop()
                    on_stack.remove(member)
                    component.append(member)
                    if member == node:
                        break
                has_self_loop = node in adjacency.get(node, set())
                if len(component) > 1 or has_self_loop:
                    components.append(sorted(component))

    return components


def detect_cycles(graph: ComponentGraph) -> list[CycleGroup]:
    """Detect circular dependency groups in a component graph and flag cross-library ones."""
    # Unlike ComponentGraph.adjacency() (which drops self-edges for metric purity),
    # cycle detection must keep them: a module referencing itself is a dependency cycle.
    adjacency: dict[str, set[str]] = {node_id: set() for node_id in graph.nodes}
    for edge in graph.edges:
        adjacency.setdefault(edge.source, set()).add(edge.target)

    components = strongly_connected_components(adjacency)

    cycles: list[CycleGroup] = []
    for cycle_id, members in enumerate(components):
        libraries = {graph.library_of(member) for member in members}
        cross_library = len(libraries - {""}) > 1
        cycles.append(CycleGroup(cycle_id=cycle_id, members=members, cross_library=cross_library))
    return cycles
