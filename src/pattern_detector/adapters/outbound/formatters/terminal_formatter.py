"""Rich terminal exporter: interactive architecture report for ``dpx arch``."""

from __future__ import annotations

import io

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree

from pattern_detector.adapters.outbound.formatters.graph_grouping import grouped_nodes
from pattern_detector.domain.architecture.models import (
    ArchitectureScanResult,
    ArchLayer,
    IssueSeverity,
    ModuleNode,
    layer_label,
)
from pattern_detector.ports.outbound.arch_exporter_port import (
    ArchitectureExporterPort,
    GraphViewOptions,
)

_SEVERITY_STYLE = {
    IssueSeverity.ERROR: ("red", "❌"),
    IssueSeverity.WARNING: ("yellow", "⚠️ "),
    IssueSeverity.INFO: ("blue", "ℹ️ "),
}

_LAYER_ORDER: list[ArchLayer] = [
    ArchLayer.API,
    ArchLayer.ADAPTERS,
    ArchLayer.PORTS,
    ArchLayer.DOMAIN,
    ArchLayer.INFRASTRUCTURE,
    ArchLayer.SHARED,
    ArchLayer.UNKNOWN,
]

_LAYER_COLOR = {
    ArchLayer.DOMAIN: "cyan",
    ArchLayer.PORTS: "magenta",
    ArchLayer.ADAPTERS: "blue",
    ArchLayer.INFRASTRUCTURE: "yellow",
    ArchLayer.API: "green",
    ArchLayer.SHARED: "white",
    ArchLayer.UNKNOWN: "dim",
}


class TerminalArchitectureFormatter(ArchitectureExporterPort):
    """Renders the architecture scan result as a rich terminal report."""

    extension = "txt"

    def format(self, result: ArchitectureScanResult, options: GraphViewOptions | None = None) -> str:
        options = options or GraphViewOptions()
        buffer = io.StringIO()
        console = Console(file=buffer, force_terminal=True, width=120)

        console.print(self._header_panel(result))
        if options.show_cycles_only:
            console.print("[bold red]Mode: cycles only — showing circular dependencies exclusively[/bold red]")
        console.print(self._library_table(result))
        console.print(self._layer_tree(result))
        console.print(self._cycles_panel(result))
        if options.with_metrics:
            console.print(self._metrics_table(result, options))
        console.print(self._issues_block(result))
        console.print(self._summary_line(result))
        return buffer.getvalue()

    # ------------------------------------------------------------------

    def _header_panel(self, result: ArchitectureScanResult) -> Panel:
        dune = "yes" if result.has_dune_manifest else "no (filesystem fallback)"
        body = (
            f"[bold]{result.project_path}[/bold]\n"
            f"Dune project: {dune}   Files: {result.files_scanned}   "
            f"Modules: {result.modules_count}   Edges: {result.edges_count}   "
            f"Time: {result.elapsed_seconds:.2f}s"
        )
        return Panel(body, title="🏗  Architecture Scan", border_style="cyan", expand=False)

    def _library_table(self, result: ArchitectureScanResult) -> Table:
        table = Table(title="Dune Libraries", title_justify="left", expand=False)
        table.add_column("Library", style="cyan", no_wrap=True)
        table.add_column("Modules", justify="right")
        table.add_column("Depends on (local)", style="dim")
        table.add_column("External deps", style="dim")

        module_count: dict[str, int] = {}
        for node in result.graph.nodes.values():
            key = node.dune_library or "(no library)"
            module_count[key] = module_count.get(key, 0) + 1

        library_names = sorted({n.dune_library for n in result.graph.nodes.values() if n.dune_library})
        if not library_names and not module_count:
            return table
        for lib in library_names or ["(no library)"]:
            local_deps = result.graph.library_deps.get(lib, [])
            external = result.graph.external_deps.get(lib, [])
            table.add_row(
                lib,
                str(module_count.get(lib, 0)),
                ", ".join(local_deps) if local_deps else "—",
                ", ".join(external) if external else "—",
            )
        return table

    def _layer_tree(self, result: ArchitectureScanResult) -> Tree:
        tree = Tree("🏗  [bold]Layers[/bold] [dim](dependencies must point inward: API → Domain ← Infra)[/dim]")
        by_layer: dict[ArchLayer, list[ModuleNode]] = {}
        for node in result.graph.nodes.values():
            by_layer.setdefault(node.layer, []).append(node)

        for layer in _LAYER_ORDER:
            modules = by_layer.get(layer)
            if not modules:
                continue
            color = _LAYER_COLOR[layer]
            branch = tree.add(f"[{color}]{layer_label(layer)}[/{color}] [dim]({len(modules)})[/dim]")
            for node in sorted(modules, key=lambda n: n.id):
                flags = []
                if node.is_entry:
                    flags.append("🚪 entry")
                if node.has_interface:
                    flags.append("📄 .mli")
                if node.cycle_id is not None:
                    flags.append("🔁 cycle")
                suffix = f" [dim]{'  '.join(flags)}  {node.loc} LOC[/dim]" if flags else f" [dim]{node.loc} LOC[/dim]"
                prefix = f"[dim]{node.dune_library}::[/dim]" if node.dune_library else ""
                branch.add(f"{prefix}{node.id}{suffix}")
        return tree

    def _cycles_panel(self, result: ArchitectureScanResult) -> Panel | str:
        if not result.cycles:
            return "[green]✅ No circular dependencies detected[/green]"
        body_lines = []
        for cycle in result.cycles:
            chain = " → ".join([*cycle.members, cycle.members[0]])
            marker = " [bold red](cross-library)[/bold red]" if cycle.cross_library else ""
            body_lines.append(f"[red]🔁 #{cycle.cycle_id}{marker}[/red]\n  {chain}")
        return Panel("\n".join(body_lines), title="Circular Dependencies", border_style="red", expand=False)

    def _metrics_table(self, result: ArchitectureScanResult, options: GraphViewOptions) -> Table:
        table = Table(
            title="Martin Component Metrics",
            title_justify="left",
            expand=False,
            caption="I = Ce/(Ca+Ce) instability · A = abstractness · D = |A+I-1| main-sequence distance",
        )
        table.add_column("Module", style="cyan", no_wrap=True)
        table.add_column("Layer", no_wrap=True)
        table.add_column("Ca", justify="right")
        table.add_column("Ce", justify="right")
        table.add_column("I", justify="right")
        table.add_column("A", justify="right")
        table.add_column("D", justify="right")
        table.add_column("Zone")

        for _, nodes in grouped_nodes(result, options.group_by, options.show_cycles_only):
            for node in nodes:
                if node.metrics is None:
                    continue
                m = node.metrics
                zone_style = "red" if m.zone != "balanced" else "green"
                table.add_row(
                    node.id,
                    layer_label(node.layer),
                    str(m.ca),
                    str(m.ce),
                    f"{m.instability:.2f}",
                    f"{m.abstractness:.2f}",
                    f"{m.main_sequence_distance:.2f}",
                    f"[{zone_style}]{m.zone}[/{zone_style}]",
                )
        return table

    def _issues_block(self, result: ArchitectureScanResult) -> Table:
        table = Table(title="Architecture Issues", title_justify="left", expand=False, show_lines=False)
        table.add_column("Sev", width=3)
        table.add_column("Finding", overflow="fold")

        for issue in result.issues:
            style, icon = _SEVERITY_STYLE[issue.severity]
            table.add_row(icon, f"[{style}]{issue.message}[/{style}]")
        if not result.issues:
            table.add_row("✅", "[green]No architecture issues detected[/green]")
        return table

    def _summary_line(self, result: ArchitectureScanResult) -> str:
        errors = sum(1 for i in result.issues if i.severity == IssueSeverity.ERROR)
        warnings = sum(1 for i in result.issues if i.severity == IssueSeverity.WARNING)
        infos = sum(1 for i in result.issues if i.severity == IssueSeverity.INFO)
        return (
            f"\n[bold]{len(result.issues)} issues[/bold] "
            f"(❌ {errors} · ⚠️  {warnings} · ℹ️  {infos}) · "
            f"scan completed in {result.elapsed_seconds:.2f}s"
        )
