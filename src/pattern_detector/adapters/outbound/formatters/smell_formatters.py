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

        # Count by severity
        crit_count = sum(1 for d in report.detections if d.severity == SmellSeverity.CRITICAL)
        high_count = sum(1 for d in report.detections if d.severity == SmellSeverity.HIGH)
        med_count = sum(1 for d in report.detections if d.severity == SmellSeverity.MEDIUM)
        low_count = sum(1 for d in report.detections if d.severity == SmellSeverity.LOW)

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DPX-OCaml • Clean Code Smell Dashboard</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{
      background: #090d16;
      color: #e2e8f0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      margin: 0;
      padding: 24px 32px;
      line-height: 1.5;
    }}
    header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 20px;
      margin-bottom: 24px;
    }}
    .logo-area h1 {{
      margin: 0;
      font-size: 26px;
      font-weight: 800;
      letter-spacing: -0.5px;
      background: linear-gradient(135deg, #f97316 0%, #ec4899 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .logo-area .subtitle {{
      color: #94a3b8;
      font-size: 13px;
      margin-top: 4px;
    }}
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }}
    .stat-card {{
      background: #111827;
      border: 1px solid #1f2937;
      border-radius: 10px;
      padding: 16px;
      cursor: pointer;
      transition: transform 0.15s ease, border-color 0.15s ease;
    }}
    .stat-card:hover {{
      transform: translateY(-2px);
      border-color: #38bdf8;
    }}
    .stat-title {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      font-weight: 600;
      color: #94a3b8;
      margin-bottom: 6px;
    }}
    .stat-value {{
      font-size: 26px;
      font-weight: 800;
      color: #f8fafc;
    }}
    .stat-crit {{ border-top: 3px solid #ef4444; }}
    .stat-high {{ border-top: 3px solid #f97316; }}
    .stat-med  {{ border-top: 3px solid #eab308; }}
    .stat-low  {{ border-top: 3px solid #0ea5e9; }}
    .stat-all  {{ border-top: 3px solid #a855f7; }}

    .toolbar {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      background: #111827;
      border: 1px solid #1f2937;
      border-radius: 10px;
      padding: 14px 18px;
      margin-bottom: 20px;
    }}
    .search-box {{
      flex: 1;
      min-width: 240px;
      background: #090d16;
      border: 1px solid #374151;
      border-radius: 6px;
      color: #fff;
      padding: 8px 14px;
      font-size: 14px;
      outline: none;
    }}
    .search-box:focus {{
      border-color: #38bdf8;
    }}
    .filter-select {{
      background: #090d16;
      border: 1px solid #374151;
      border-radius: 6px;
      color: #cbd5e1;
      padding: 8px 12px;
      font-size: 13px;
      outline: none;
    }}
    .pill-group {{
      display: flex;
      gap: 6px;
    }}
    .pill {{
      background: #1f2937;
      border: 1px solid #374151;
      color: #cbd5e1;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      user-select: none;
      transition: all 0.15s ease;
    }}
    .pill:hover {{ background: #374151; }}
    .pill.active {{
      background: #38bdf8;
      border-color: #38bdf8;
      color: #0b0f19;
    }}

    .results-meta {{
      font-size: 13px;
      color: #94a3b8;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .findings-container {{
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .card {{
      background: #111827;
      border: 1px solid #1f2937;
      border-radius: 10px;
      padding: 18px 20px;
      transition: border-color 0.15s ease;
    }}
    .card:hover {{
      border-color: #374151;
    }}
    .card-CRITICAL {{ border-left: 4px solid #ef4444; }}
    .card-HIGH     {{ border-left: 4px solid #f97316; }}
    .card-MEDIUM   {{ border-left: 4px solid #eab308; }}
    .card-LOW      {{ border-left: 4px solid #0ea5e9; }}

    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 8px;
    }}
    .card-title {{
      font-size: 16px;
      font-weight: 700;
      color: #f1f5f9;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .card-title code {{
      background: #1e293b;
      color: #38bdf8;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 14px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .badge-CRITICAL {{ background: #dc2626; color: #fff; }}
    .badge-HIGH {{ background: #ea580c; color: #fff; }}
    .badge-MEDIUM {{ background: #eab308; color: #000; }}
    .badge-LOW {{ background: #0284c7; color: #fff; }}
    .badge-cat {{
      background: #1e293b;
      color: #94a3b8;
      border: 1px solid #334155;
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 4px;
    }}

    .meta-line {{
      font-size: 12px;
      color: #94a3b8;
      margin-bottom: 10px;
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
    }}
    .meta-line a {{
      color: #60a5fa;
      text-decoration: none;
    }}
    .meta-line a:hover {{ text-decoration: underline; }}
    .evidence {{
      background: #0f172a;
      border-left: 3px solid #38bdf8;
      padding: 10px 14px;
      border-radius: 4px;
      font-size: 13.5px;
      color: #cbd5e1;
      margin: 10px 0;
    }}
    .refactoring {{
      background: rgba(6, 78, 59, 0.4);
      border: 1px solid #065f46;
      border-radius: 6px;
      padding: 10px 14px;
      color: #6ee7b7;
      font-size: 13px;
      margin-top: 10px;
    }}
    .pagination {{
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 12px;
      margin-top: 28px;
    }}
    .page-btn {{
      background: #1f2937;
      border: 1px solid #374151;
      color: #cbd5e1;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 13px;
      cursor: pointer;
    }}
    .page-btn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
    }}
    .page-info {{
      font-size: 13px;
      color: #94a3b8;
    }}
  </style>
</head>
<body>
  <header>
    <div class="logo-area">
      <h1>🐫 DPX-OCaml • Clean Code Smell Dashboard</h1>
      <div class="subtitle">
        Static analysis of OCaml codebase • <b>{report.project_path}</b>
      </div>
    </div>
    <div style="text-align: right; font-size: 12px; color: #64748b;">
      <div>Scanned: <b>{report.scanned_files_count} files</b></div>
      <div>Elapsed: <b>{report.elapsed_seconds:.2f}s</b></div>
    </div>
  </header>

  <div class="stats-grid">
    <div class="stat-card stat-all" onclick="filterBySev('ALL')">
      <div class="stat-title">Total Smells</div>
      <div class="stat-value">{len(report.detections)}</div>
    </div>
    <div class="stat-card stat-crit" onclick="filterBySev('CRITICAL')">
      <div class="stat-title">Critical</div>
      <div class="stat-value" style="color: #ef4444;">{crit_count}</div>
    </div>
    <div class="stat-card stat-high" onclick="filterBySev('HIGH')">
      <div class="stat-title">High</div>
      <div class="stat-value" style="color: #f97316;">{high_count}</div>
    </div>
    <div class="stat-card stat-med" onclick="filterBySev('MEDIUM')">
      <div class="stat-title">Medium</div>
      <div class="stat-value" style="color: #eab308;">{med_count}</div>
    </div>
    <div class="stat-card stat-low" onclick="filterBySev('LOW')">
      <div class="stat-title">Low</div>
      <div class="stat-value" style="color: #0ea5e9;">{low_count}</div>
    </div>
  </div>

  <div class="toolbar">
    <input type="text" id="searchInput" class="search-box" placeholder="Search by smell ID, symbol, file path, or evidence..." oninput="onFilterChange()" />
    <select id="categorySelect" class="filter-select" onchange="onFilterChange()">
      <option value="ALL">All Categories</option>
      <option value="FUNCTIONS">FUNCTIONS</option>
      <option value="NAMING">NAMING</option>
      <option value="TYPES">TYPES</option>
      <option value="CONTROL_FLOW">CONTROL_FLOW</option>
      <option value="MODULES">MODULES</option>
      <option value="DUPLICATION">DUPLICATION</option>
      <option value="STATE_AND_EFFECTS">STATE_AND_EFFECTS</option>
      <option value="DEPENDENCIES">DEPENDENCIES</option>
      <option value="ERROR_HANDLING">ERROR_HANDLING</option>
      <option value="TESTABILITY">TESTABILITY</option>
      <option value="ARCHITECTURE">ARCHITECTURE</option>
      <option value="REFACTORING_SAFETY">REFACTORING_SAFETY</option>
    </select>
    <div class="pill-group">
      <div class="pill active" id="pill-ALL" onclick="filterBySev('ALL')">All</div>
      <div class="pill" id="pill-CRITICAL" onclick="filterBySev('CRITICAL')">Critical</div>
      <div class="pill" id="pill-HIGH" onclick="filterBySev('HIGH')">High</div>
      <div class="pill" id="pill-MEDIUM" onclick="filterBySev('MEDIUM')">Medium</div>
      <div class="pill" id="pill-LOW" onclick="filterBySev('LOW')">Low</div>
    </div>
  </div>

  <div class="results-meta">
    <span id="resultsCount">Loading findings...</span>
    <span>Page size: 50 items</span>
  </div>

  <div id="findingsContainer" class="findings-container"></div>

  <div class="pagination">
    <button id="prevBtn" class="page-btn" onclick="changePage(-1)">← Previous</button>
    <span id="pageInfo" class="page-info">Page 1</span>
    <button id="nextBtn" class="page-btn" onclick="changePage(1)">Next →</button>
  </div>

  <script>
    const allData = {findings_json};
    let currentSev = 'ALL';
    let filteredData = allData;
    let currentPage = 1;
    const PAGE_SIZE = 50;

    function filterBySev(sev) {{
      currentSev = sev;
      document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
      const activePill = document.getElementById('pill-' + sev);
      if (activePill) activePill.classList.add('active');
      onFilterChange();
    }}

    function onFilterChange() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const cat = document.getElementById('categorySelect').value;

      filteredData = allData.filter(d => {{
        if (currentSev !== 'ALL' && d.severity !== currentSev) return false;
        if (cat !== 'ALL' && d.category !== cat) return false;
        if (query) {{
          const matchStr = (d.smell_id + ' ' + d.symbol + ' ' + d.file + ' ' + d.evidence).toLowerCase();
          if (!matchStr.includes(query)) return false;
        }}
        return true;
      }});

      currentPage = 1;
      render();
    }}

    function changePage(delta) {{
      const maxPage = Math.max(1, Math.ceil(filteredData.length / PAGE_SIZE));
      currentPage = Math.min(Math.max(1, currentPage + delta), maxPage);
      render();
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function render() {{
      const container = document.getElementById('findingsContainer');
      const countEl = document.getElementById('resultsCount');
      const pageInfo = document.getElementById('pageInfo');
      const prevBtn = document.getElementById('prevBtn');
      const nextBtn = document.getElementById('nextBtn');

      countEl.innerText = `Showing ${{filteredData.length}} of ${{allData.length}} finding(s)`;
      const totalPages = Math.max(1, Math.ceil(filteredData.length / PAGE_SIZE));
      pageInfo.innerText = `Page ${{currentPage}} of ${{totalPages}}`;

      prevBtn.disabled = (currentPage <= 1);
      nextBtn.disabled = (currentPage >= totalPages);

      container.innerHTML = '';

      if (filteredData.length === 0) {{
        container.innerHTML = '<div style="text-align: center; color: #64748b; padding: 48px;">No matching smells found.</div>';
        return;
      }}

      const startIdx = (currentPage - 1) * PAGE_SIZE;
      const endIdx = Math.min(startIdx + PAGE_SIZE, filteredData.length);
      const pageSlice = filteredData.slice(startIdx, endIdx);

      const fragment = document.createDocumentFragment();
      pageSlice.forEach((d, idx) => {{
        const globalIdx = startIdx + idx + 1;
        const card = document.createElement('div');
        card.className = `card card-${{d.severity}}`;

        card.innerHTML = `
          <div class="card-top">
            <div class="card-title">
              <span>#${{globalIdx}} ${{d.smell_id}}</span>
              <code>${{d.symbol}}</code>
            </div>
            <div style="display: flex; gap: 8px; align-items: center;">
              <span class="badge-cat">${{d.category}}</span>
              <span class="badge badge-${{d.severity}}">${{d.severity}}</span>
            </div>
          </div>
          <div class="meta-line">
            <span>📍 <a href="file://${{d.file}}#L${{d.start_line}}">${{d.file}}:${{d.start_line}}-${{d.end_line}}</a></span>
            <span>📏 Threshold: <b>${{d.threshold}}</b></span>
            <span>🎯 Confidence: <b>${{Math.round(d.confidence * 100)}}%</b></span>
          </div>
          <div class="evidence">🔎 ${{d.evidence}}</div>
          <div class="refactoring">💡 <b>Suggested Refactoring:</b> ${{d.suggested_refactoring}}</div>
        `;
        fragment.appendChild(card);
      }});

      container.appendChild(fragment);
    }}

    // Initial render
    onFilterChange();
  </script>
</body>
</html>"""
