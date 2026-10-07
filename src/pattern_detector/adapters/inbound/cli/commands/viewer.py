"""``dpx viewer`` CLI command: interactive Architecture Viewer generator."""

from __future__ import annotations

import json
import webbrowser
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel

from pattern_detector.adapters.outbound.formatters.viewer_html_formatter import (
    ViewerHtmlFormatter,
)
from pattern_detector.bootstrap.container import create_container

console = Console()

#: Default output directory for ``architecture.json`` + the viewer HTML.
DEFAULT_OUT_DIR = "dpx_viewer"

_SNAPSHOT_FILE = "architecture.json"
_HTML_FILE = "dpx_viewer.html"


def viewer(
    path: Annotated[
        str,
        typer.Argument(help="Path to the OCaml project to analyse (defaults to the current directory)."),
    ] = ".",
    out: Annotated[
        str | None,
        typer.Option(
            "--out",
            "-o",
            help=f"Directory for the viewer output (defaults to ./{DEFAULT_OUT_DIR}).",
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
    no_patterns: Annotated[
        bool,
        typer.Option(
            "--no-patterns",
            help="Skip the pattern-detector pass (faster; findings tab will be empty).",
        ),
    ] = False,
    open_browser: Annotated[
        bool,
        typer.Option(
            "--open",
            help="Open the generated viewer in the default web browser.",
        ),
    ] = False,
) -> None:
    """Build the interactive Architecture Viewer: a self-contained HTML map + architecture.json."""
    container = create_container()
    target = str(Path(path).resolve())

    snapshot = container.get_viewer_service().build_snapshot(
        target,
        exclude_dirs=exclude or [],
        include_patterns=not no_patterns,
    )

    out_dir = Path(out).expanduser() if out else Path.cwd() / DEFAULT_OUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    snapshot_path = out_dir / _SNAPSHOT_FILE
    snapshot_path.write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    html_path = out_dir / _HTML_FILE
    html_path.write_text(ViewerHtmlFormatter().render(snapshot), encoding="utf-8")

    s = snapshot["summary"]
    console.print(
        Panel.fit(
            f"[bold white]🐫 Interactive Architecture Viewer[/bold white]\n"
            f"[dim]{s['files']} files · {s['modules']} modules · {s['edges']} edges · "
            f"{s['cycles']} cycles · {s['issues']} issues · {s['findings']} findings · "
            f"{s['elapsed_seconds']:.2f}s[/dim]\n"
            f"[green]✓[/green] [cyan]{html_path}[/cyan] [dim](self-contained, works offline)[/dim]\n"
            f"[green]✓[/green] [cyan]{snapshot_path}[/cyan] [dim](schema {snapshot['schema_version']})[/dim]",
            border_style="orange3",
        )
    )

    if open_browser:
        webbrowser.open(html_path.resolve().as_uri())
