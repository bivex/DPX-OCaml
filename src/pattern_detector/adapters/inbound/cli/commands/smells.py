"""``dpx smells`` CLI command: Clean Code Smell Detector for OCaml."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from pattern_detector.bootstrap.container import create_container
from pattern_detector.domain.smells.models import (
    SmellCategory,
    SmellSeverity,
    SmellThresholds,
)
from pattern_detector.ports.inbound.smell_scanner_port import (
    SmellOutputFormat,
    SmellScanOptions,
)

console = Console()


def smells(
    path: Annotated[
        str,
        typer.Argument(help="Path to an OCaml file (.ml/.mli) or directory to scan for clean code smells."),
    ] = ".",
    fmt: Annotated[
        SmellOutputFormat,
        typer.Option(
            "--format",
            "-f",
            help="Output format: terminal | json | markdown | html | all.",
        ),
    ] = SmellOutputFormat.TERMINAL,
    severity: Annotated[
        SmellSeverity,
        typer.Option(
            "--severity",
            "-s",
            help="Minimum severity threshold: LOW | MEDIUM | HIGH | CRITICAL.",
        ),
    ] = SmellSeverity.LOW,
    category: Annotated[
        SmellCategory | None,
        typer.Option(
            "--category",
            "-c",
            help="Filter by specific smell category (e.g. FUNCTIONS, NAMING, TYPES, CONTROL_FLOW, MODULES, etc.).",
        ),
    ] = None,
    max_func_lines: Annotated[
        int,
        typer.Option("--max-func-lines", help="Threshold for Long_Function smell."),
    ] = 50,
    max_complexity: Annotated[
        int,
        typer.Option("--max-complexity", help="Threshold for High_Cyclomatic_Complexity smell."),
    ] = 10,
    max_nesting: Annotated[
        int,
        typer.Option("--max-nesting", help="Threshold for Deep_Nesting smell."),
    ] = 4,
    max_args: Annotated[
        int,
        typer.Option("--max-args", help="Threshold for Too_Many_Arguments smell."),
    ] = 5,
    max_match_branches: Annotated[
        int,
        typer.Option("--max-match-branches", help="Threshold for Large_Match smell."),
    ] = 10,
    max_module_lines: Annotated[
        int,
        typer.Option("--max-module-lines", help="Threshold for Large_Module smell."),
    ] = 500,
    max_exported_values: Annotated[
        int,
        typer.Option("--max-exported-values", help="Threshold for Too_Many_Public_Functions smell."),
    ] = 30,
    max_opens: Annotated[
        int,
        typer.Option("--max-opens", help="Threshold for Excessive_Open smell."),
    ] = 10,
    out: Annotated[
        str | None,
        typer.Option(
            "--out",
            "-o",
            help="Output path for exported report file.",
        ),
    ] = None,
    exclude: Annotated[
        list[str] | None,
        typer.Option(
            "--exclude",
            "-e",
            help="Directory name(s) or patterns to exclude from scanning.",
        ),
    ] = None,
    fail_on_critical: Annotated[
        bool,
        typer.Option(
            "--fail-on-critical",
            help="Exit with non-zero exit code if CRITICAL smells are detected.",
        ),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Enable verbose diagnostic output."),
    ] = False,
) -> None:
    """Detect Clean Code smells and antipatterns in OCaml codebases using AST, graph, and flow analysis."""
    container = create_container()
    target = str(Path(path).resolve())

    thresholds = SmellThresholds(
        function_lines=max_func_lines,
        cyclomatic_complexity=max_complexity,
        nesting_depth=max_nesting,
        function_parameters=max_args,
        match_branches=max_match_branches,
        module_lines=max_module_lines,
        exported_value_count=max_exported_values,
        open_count=max_opens,
    )

    formats = (
        [SmellOutputFormat.JSON, SmellOutputFormat.MARKDOWN, SmellOutputFormat.HTML, SmellOutputFormat.TERMINAL]
        if fmt == SmellOutputFormat.ALL
        else [fmt]
    )

    options = SmellScanOptions(
        formats=formats,
        category=category,
        min_severity=severity,
        thresholds=thresholds,
        output_path=out,
        exclude_dirs=exclude or [],
        fail_on_critical=fail_on_critical,
        verbose=verbose,
    )

    service = container.get_smell_service()
    report = service.scan_smells(target, options=options)
    exporters = container.get_smell_exporters()

    # Terminal output
    if SmellOutputFormat.TERMINAL in formats:
        text = exporters[SmellOutputFormat.TERMINAL].format(report)
        console.out(text)

    # File exports
    file_formats = [f for f in formats if f != SmellOutputFormat.TERMINAL]
    for file_fmt in file_formats:
        exporter = exporters[file_fmt]
        rendered = exporter.format(report)
        if out:
            out_path = Path(out)
            if out_path.is_dir():
                dest = out_path / f"dpx_smells_report.{exporter.extension}"
            else:
                dest = out_path
        else:
            dest = Path.cwd() / f"dpx_smells_report.{exporter.extension}"

        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(rendered, encoding="utf-8")
        console.print(f"[dim]Exported:[/dim] [green]✓[/green] {dest}")

    if fail_on_critical:
        critical_count = sum(1 for d in report.detections if d.severity == SmellSeverity.CRITICAL)
        if critical_count > 0:
            console.print(f"[bold red]❌ Failure: {critical_count} CRITICAL code smell(s) detected![/bold red]")
            sys.exit(1)
