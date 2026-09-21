"""``dpx arch`` CLI command: project architecture & dependency graph scanner."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from pattern_detector.bootstrap.container import Container, create_container
from pattern_detector.domain.architecture.models import ArchitectureScanResult
from pattern_detector.ports.inbound.arch_scanner_port import (
    ArchOutputFormat,
    ArchScanOptions,
    GraphGrouping,
)
from pattern_detector.ports.outbound.arch_exporter_port import (
    ArchitectureExporterPort,
    GraphViewOptions,
)

console = Console()

# File-producing formats implied by ``--format all``.
_FILE_FORMATS = [
    ArchOutputFormat.MERMAID,
    ArchOutputFormat.DOT,
    ArchOutputFormat.HTML,
    ArchOutputFormat.JSON,
]


def arch(
    path: Annotated[
        str,
        typer.Argument(help="Path to the OCaml project to analyse (defaults to the current directory)."),
    ] = ".",
    fmt: Annotated[
        ArchOutputFormat,
        typer.Option(
            "--format",
            "-f",
            help="Output format: terminal | mermaid | dot | html | json | all.",
        ),
    ] = ArchOutputFormat.TERMINAL,
    group_by: Annotated[
        GraphGrouping,
        typer.Option(
            "--group-by",
            help="Grouping of graph nodes: dune-library | layer | directory.",
        ),
    ] = GraphGrouping.DUNE_LIBRARY,
    show_cycles_only: Annotated[
        bool,
        typer.Option(
            "--show-cycles-only",
            help="Show only modules participating in circular dependencies.",
        ),
    ] = False,
    metrics: Annotated[
        bool,
        typer.Option(
            "--metrics/--no-metrics",
            help="Include Martin component metrics (Ca/Ce/I/A/D) in the report.",
        ),
    ] = True,
    out: Annotated[
        str | None,
        typer.Option(
            "--out",
            "-o",
            help="Directory for exported files (defaults to the current directory).",
        ),
    ] = None,
    exclude: Annotated[
        list[str] | None,
        typer.Option(
            "--exclude",
            "-e",
            help="Directory name(s) to exclude from scanning (e.g. -e _build -e test).",
        ),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Enable verbose logging."),
    ] = False,
) -> None:
    """Analyse Dune project architecture: module DAG, layers, cycles, Martin metrics."""
    container = create_container()
    target = str(Path(path).resolve())

    formats: list[ArchOutputFormat] = (
        _FILE_FORMATS + [ArchOutputFormat.TERMINAL] if fmt == ArchOutputFormat.ALL else [fmt]
    )
    options = ArchScanOptions(
        formats=formats,
        group_by=group_by,
        show_cycles_only=show_cycles_only,
        with_metrics=metrics,
        output_dir=out,
        exclude_dirs=exclude or [],
        verbose=verbose,
    )

    service = container.get_arch_service()
    result = service.scan_architecture(target, options=options)

    exporters = container.get_arch_exporters()
    view_options = GraphViewOptions(
        group_by=group_by.value,
        show_cycles_only=show_cycles_only,
        with_metrics=metrics,
    )

    if ArchOutputFormat.TERMINAL in formats:
        text = exporters[ArchOutputFormat.TERMINAL].format(result, view_options)
        # The formatter renders rich markup into ANSI itself; out() prints verbatim.
        console.out(text)

    written = _export_files(container, result, formats, view_options, out)
    if written:
        console.print("[dim]Exported:[/dim]")
        for file_path in written:
            console.print(f"  [green]✓[/green] {file_path}")


def _export_files(
    container: Container,
    result: ArchitectureScanResult,
    formats: list[ArchOutputFormat],
    view_options: GraphViewOptions,
    out: str | None,
) -> list[str]:
    """Write every file-based export; returns the list of paths written."""
    exporters: dict[ArchOutputFormat, ArchitectureExporterPort] = {
        fmt: exporter
        for fmt, exporter in container.get_arch_exporters().items()
        if fmt in formats and fmt is not ArchOutputFormat.TERMINAL
    }
    if not exporters:
        return []

    directory = Path(out).expanduser() if out else Path.cwd()
    directory.mkdir(parents=True, exist_ok=True)

    written: list[str] = []
    for exporter in exporters.values():
        file_path = directory / f"dpx_arch_report.{exporter.extension}"
        file_path.write_text(exporter.format(result, view_options), encoding="utf-8")
        written.append(str(file_path))
    return written
