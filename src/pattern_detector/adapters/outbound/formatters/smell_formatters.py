"""Formatters for exporting smell scan results to Terminal, JSON, Markdown, and HTML."""

from __future__ import annotations

import json
from io import StringIO

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from pattern_detector.domain.smells.models import SmellReport, SmellSeverity
from pattern_detector.ports.outbound.smell_exporter_port import SmellExporterPort


class SmellTerminalFormatter(SmellExporterPort):
    """Renders smell reports with rich colors, tables, and inspection cards."""

    @property
    def extension(self) -> str:
        return "txt"

    def format(self, report: SmellReport) -> str:
        string_io = StringIO()
        console = Console(file=string_io, force_terminal=True, color_system="truecolor", width=110)

        # 1. Header Banner
        header = Panel.fit(
            f"[bold white]🐫 DPX-OCaml: Clean Code Smell Detector • Hexagonal Static Analysis[/bold white]\n"
            f"[dim]Scanned: {report.scanned_files_count} file(s) in {report.elapsed_seconds:.3f}s | "
            f"Found: {len(report.detections)} smell instance(s)[/dim]",
            border_style="orange3",
        )
        console.print(header)

        if not report.detections:
            console.print("[bold green]✨ Clean Code: No code smells detected matching criteria![/bold green]")
            return string_io.getvalue()

        # 2. Summary Table
        table = Table(title="📊 Code Smells by Category & Severity", header_style="bold orange3")
        table.add_column("Category", style="cyan")
        table.add_column("Total", justify="right", style="bold")
        table.add_column("Severity Breakdown", style="dim")

        for cat, count in sorted(report.category_counts.items()):
            cat_dets = [d for d in report.detections if d.category.value == cat]
            crit = sum(1 for d in cat_dets if d.severity == SmellSeverity.CRITICAL)
            high = sum(1 for d in cat_dets if d.severity == SmellSeverity.HIGH)
            med = sum(1 for d in cat_dets if d.severity == SmellSeverity.MEDIUM)
            low = sum(1 for d in cat_dets if d.severity == SmellSeverity.LOW)
            breakdown = f"[red]{crit} CRIT[/red], [orange3]{high} HIGH[/orange3], [yellow]{med} MED[/yellow], [cyan]{low} LOW[/cyan]"
            table.add_row(cat, str(count), breakdown)

        console.print(table)
        console.print()

        # 3. Detection Cards
        console.print("[bold]📋 Identified Clean Code Smells & Antipatterns:[/bold]\n")
        for idx, d in enumerate(report.detections, 1):
            sev_color = self._severity_color(d.severity)
            loc = f"📍 Location: [cyan]{d.file}:{d.start_line}-{d.end_line}[/cyan]"
            header_text = (
                f"[bold orange3]#{idx} {d.smell_id}[/bold orange3] on "
                f"[bold]{d.symbol}[/bold] [{sev_color}]{d.severity.value}[/{sev_color}]"
            )

            lines = [
                header_text,
                f"├── {loc}",
                f"├── 🏷️ Category: [dim]{d.category.value}[/dim] (Confidence: {int(d.confidence * 100)}%)",
                f"├── 📏 Threshold: [dim]{d.threshold}[/dim]",
                f"├── 🔎 Evidence: {d.evidence}",
                f"└── 💡 Refactoring: [green]{d.suggested_refactoring}[/green]",
            ]
            console.print("\n".join(lines))
            console.print()

        return string_io.getvalue()

    def _severity_color(self, severity: SmellSeverity) -> str:
        return {
            SmellSeverity.CRITICAL: "bold red",
            SmellSeverity.HIGH: "bold orange3",
            SmellSeverity.MEDIUM: "yellow",
            SmellSeverity.LOW: "cyan",
        }[severity]


class SmellJsonFormatter(SmellExporterPort):
    """Outputs smell detection report as JSON strictly conforming to the requested schema."""

    @property
    def extension(self) -> str:
        return "json"

    def format(self, report: SmellReport) -> str:
        data = {
            "project_path": report.project_path,
            "scanned_files": report.scanned_files_count,
            "elapsed_seconds": round(report.elapsed_seconds, 4),
            "summary": {
                "total_smells": len(report.detections),
                "by_category": report.category_counts,
                "by_severity": report.severity_counts,
            },
            "findings": [
                {
                    "smell_id": d.smell_id,
                    "category": d.category.value,
                    "severity": d.severity.value,
                    "file": d.file,
                    "start_line": d.start_line,
                    "end_line": d.end_line,
                    "symbol": d.symbol,
                    "evidence": d.evidence,
                    "threshold": d.threshold,
                    "confidence": d.confidence,
                    "suggested_refactoring": d.suggested_refactoring,
                }
                for d in report.detections
            ],
        }
        return json.dumps(data, indent=2)


class SmellMarkdownFormatter(SmellExporterPort):
    """Renders smell reports in GitHub-flavored Markdown."""

    @property
    def extension(self) -> str:
        return "md"

    def format(self, report: SmellReport) -> str:
        lines = [
            "# 🐫 DPX-OCaml Clean Code Smell Report",
            "",
            f"- **Scanned Files:** `{report.scanned_files_count}`",
            f"- **Analysis Time:** `{report.elapsed_seconds:.3f}s`",
            f"- **Total Smells Detected:** `{len(report.detections)}`",
            "",
            "## 📊 Breakdown by Severity",
            "",
            "| Severity | Count |",
            "|:---|---:|",
        ]
        for sev in (SmellSeverity.CRITICAL, SmellSeverity.HIGH, SmellSeverity.MEDIUM, SmellSeverity.LOW):
            lines.append(f"| **{sev.value}** | `{report.severity_counts.get(sev.value, 0)}` |")

        lines.extend([
            "",
            "## 📋 Detailed Smell Findings",
            "",
            "| # | Smell ID | Category | Severity | Symbol / Location | Evidence | Suggested Refactoring |",
            "|---|---|---|---|---|---|---|",
        ])

        for idx, d in enumerate(report.detections, 1):
            file_link = f"`{d.file}:{d.start_line}`"
            evidence_clean = d.evidence.replace("|", "\\|")
            refactor_clean = d.suggested_refactoring.replace("|", "\\|")
            lines.append(
                f"| {idx} | **{d.smell_id}** | `{d.category.value}` | `{d.severity.value}` | `{d.symbol}` ({file_link}) | {evidence_clean} | {refactor_clean} |"
            )

        return "\n".join(lines)


class SmellHtmlFormatter(SmellExporterPort):
    """Generates an interactive, standalone dark dashboard for browsing smells."""

    @property
    def extension(self) -> str:
        return "html"

    def format(self, report: SmellReport) -> str:
        findings_json = json.dumps([
            {
                "smell_id": d.smell_id,
                "category": d.category.value,
                "severity": d.severity.value,
                "file": d.file,
                "start_line": d.start_line,
                "end_line": d.end_line,
                "symbol": d.symbol,
                "evidence": d.evidence,
                "threshold": d.threshold,
                "confidence": d.confidence,
                "suggested_refactoring": d.suggested_refactoring,
            }
            for d in report.detections
        ])

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>DPX-OCaml • Clean Code Smell Dashboard</title>
  <style>
    body {{
      background: #0f172a;
      color: #e2e8f0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      padding: 24px;
    }}
    .header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
      padding-bottom: 16px;
      margin-bottom: 24px;
    }}
    h1 {{ color: #f97316; margin: 0; font-size: 24px; }}
    .badge {{
      display: inline-block;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: bold;
    }}
    .badge-CRITICAL {{ background: #dc2626; color: #fff; }}
    .badge-HIGH {{ background: #ea580c; color: #fff; }}
    .badge-MEDIUM {{ background: #eab308; color: #000; }}
    .badge-LOW {{ background: #0284c7; color: #fff; }}
    .card {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 12px;
    }}
    .card-title {{
      font-size: 16px;
      font-weight: bold;
      color: #38bdf8;
      display: flex;
      justify-content: space-between;
    }}
    .evidence {{ color: #cbd5e1; margin: 8px 0; font-size: 14px; }}
    .refactoring {{ color: #4ade80; font-size: 13px; background: #064e3b; padding: 6px 10px; border-radius: 4px; }}
    .meta {{ font-size: 12px; color: #94a3b8; margin-top: 6px; }}
  </style>
</head>
<body>
  <div class="header">
    <div>
      <h1>🐫 DPX-OCaml Clean Code Smell Report</h1>
      <div style="color: #94a3b8; font-size: 13px; margin-top: 4px;">
        {len(report.detections)} smell instance(s) detected across {report.scanned_files_count} file(s) in {report.elapsed_seconds:.3f}s
      </div>
    </div>
  </div>
  <div id="container"></div>
  <script>
    const data = {findings_json};
    const container = document.getElementById('container');
    data.forEach((d, i) => {{
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <div class="card-title">
          <span>#${{i+1}} ${{d.smell_id}} • <code>${{d.symbol}}</code></span>
          <span class="badge badge-${{d.severity}}">${{d.severity}}</span>
        </div>
        <div class="meta">📍 ${{d.file}}:${{d.start_line}}-${{d.end_line}} | 🏷️ ${{d.category}} | 📏 Threshold: ${{d.threshold}}</div>
        <div class="evidence">🔎 ${{d.evidence}}</div>
        <div class="refactoring">💡 <b>Suggested Refactoring:</b> ${{d.suggested_refactoring}}</div>
      `;
      container.appendChild(card);
    }});
  </script>
</body>
</html>"""
