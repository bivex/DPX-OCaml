"""Self-contained interactive HTML exporter powered by GoJS.

Produces a rich interactive diagram with hierarchical and force-directed layouts,
collapsible library groups, Martin metrics inspection, live search, minimap overview,
and side panel inspectors.
"""

from __future__ import annotations

import html
import json

from pattern_detector.adapters.outbound.formatters.graph_grouping import (
    cycle_edge_pairs,
    group_key,
    grouped_nodes,
)
from pattern_detector.domain.architecture.models import ArchitectureScanResult
from pattern_detector.ports.outbound.arch_exporter_port import (
    ArchitectureExporterPort,
    GraphViewOptions,
)

_KIND_LABEL = {
    "open": "open",
    "include": "include",
    "functor_application": "functor",
    "qualified_reference": "ref",
}

_GROUP_PALETTE = [
    "#4f8ef7", "#37b24d", "#f76707", "#ae3ec9", "#e64980",
    "#1c7ed6", "#0ca678", "#f59f00", "#7048e8", "#e8590c",
    "#1098ad", "#74b816", "#d6336c", "#3b5bdb", "#66d9e8",
]


class HtmlGraphFormatter(ArchitectureExporterPort):
    """Renders the component graph as a rich GoJS interactive HTML page."""

    extension = "html"

    def format(self, result: ArchitectureScanResult, options: GraphViewOptions | None = None) -> str:
        options = options or GraphViewOptions()
        payload = self._payload(result, options)
        data_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
        return (
            _TEMPLATE
            .replace("__DATA__", data_json)
            .replace("__TITLE__", html.escape(result.project_path))
        )

    def _payload(self, result: ArchitectureScanResult, options: GraphViewOptions) -> dict[str, object]:
        cycle_pairs = cycle_edge_pairs(result)
        groups: list[dict[str, str]] = []
        nodes: list[dict[str, object]] = []
        group_color: dict[str, str] = {}

        grouped = grouped_nodes(result, options.group_by, options.show_cycles_only)
        visible: set[str] = set()
        for index, (label, members) in enumerate(grouped):
            color = _GROUP_PALETTE[index % len(_GROUP_PALETTE)]
            group_color[label] = color
            groups.append({"label": label, "color": color})
            for node in members:
                visible.add(node.id)
                key = group_key(node, options.group_by, result.project_path)
                m = node.metrics
                nodes.append(
                    {
                        "id": node.id,
                        "label": node.name,
                        "group": key,
                        "groupColor": group_color.get(key, "#4f8ef7"),
                        "library": node.dune_library or "",
                        "layer": node.layer.value,
                        "loc": node.loc,
                        "hasInterface": node.has_interface,
                        "isEntry": node.is_entry,
                        "cycle": node.cycle_id is not None,
                        "ca": m.ca if m else 0,
                        "ce": m.ce if m else 0,
                        "i": round(m.instability, 3) if m else 0.0,
                        "a": round(m.abstractness, 3) if m else 0.0,
                        "d": round(m.main_sequence_distance, 3) if m else 0.0,
                        "zone": m.zone if m else "—",
                    }
                )

        edges = [
            {
                "s": e.source,
                "t": e.target,
                "kind": _KIND_LABEL.get(e.kind.value, e.kind.value),
                "weight": e.weight,
                "inCycle": (e.source, e.target) in cycle_pairs,
                "crossLibrary": e.cross_library,
            }
            for e in result.graph.edges
            if e.source in visible and e.target in visible
        ]

        return {
            "project": result.project_path,
            "groupBy": options.group_by,
            "modules": result.modules_count,
            "edges": result.edges_count,
            "cycles": len(result.cycles),
            "issues": [
                {"severity": i.severity.value, "kind": i.kind.value, "message": i.message}
                for i in result.issues
            ],
            "groups": groups,
            "nodes": nodes,
            "links": edges,
        }


_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>dpx arch (GoJS) — __TITLE__</title>
<script src="https://cdn.jsdelivr.net/npm/gojs/release/go.js"></script>
<style>
  :root {
    --bg: #0f172a;
    --panel: #1e293b;
    --line: #334155;
    --text: #f8fafc;
    --dim: #94a3b8;
    --accent: #38bdf8;
    --danger: #ef4444;
    --warning: #f59e0b;
    --success: #22c55e;
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    background: var(--bg);
    color: var(--text);
    font: 13px/1.45 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    overflow: hidden;
    height: 100vh;
    display: flex;
    flex-direction: column;
  }
  header {
    height: 54px;
    background: rgba(15, 23, 42, 0.95);
    border-bottom: 1px solid var(--line);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    z-index: 20;
    gap: 12px;
  }
  .header-left {
    display: flex;
    align-items: center;
    gap: 12px;
    min-width: 0;
  }
  .header-title {
    font-size: 15px;
    font-weight: 700;
    color: #f1f5f9;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .badge-tag {
    background: #0284c7;
    color: #fff;
    padding: 2px 8px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
  }
  .stats-bar {
    display: flex;
    gap: 14px;
    color: var(--dim);
    font-size: 12px;
    white-space: nowrap;
  }
  .stats-item span {
    color: var(--text);
    font-weight: 600;
  }
  .controls-bar {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .search-box {
    position: relative;
    display: flex;
    align-items: center;
  }
  .search-box input {
    background: #090d16;
    border: 1px solid var(--line);
    border-radius: 6px;
    padding: 5px 10px 5px 28px;
    color: var(--text);
    font-size: 12px;
    width: 170px;
    outline: none;
    transition: all .15s;
  }
  .search-box input:focus {
    width: 220px;
    border-color: var(--accent);
    box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
  }
  .search-icon {
    position: absolute;
    left: 8px;
    color: var(--dim);
    pointer-events: none;
    font-size: 11px;
  }
  button, select {
    background: var(--panel);
    color: var(--text);
    border: 1px solid var(--line);
    border-radius: 6px;
    padding: 5px 10px;
    font-size: 12px;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.15s, border-color 0.15s, color 0.15s;
  }
  button:hover, select:hover {
    border-color: var(--accent);
    color: var(--accent);
  }
  #mainContainer {
    position: relative;
    flex: 1;
    overflow: hidden;
  }
  #diagramDiv {
    width: 100%;
    height: 100%;
    background: #0f172a;
    outline: none;
  }
  #overviewDiv {
    position: absolute;
    bottom: 16px;
    left: 16px;
    width: 220px;
    height: 140px;
    background: rgba(30, 41, 59, 0.92);
    border: 1px solid var(--line);
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    z-index: 10;
  }
  #overviewTitle {
    position: absolute;
    top: 4px;
    left: 8px;
    font-size: 10px;
    color: var(--dim);
    font-weight: 600;
    pointer-events: none;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    z-index: 11;
  }
  #legend {
    position: absolute;
    top: 16px;
    left: 16px;
    background: rgba(30, 41, 59, 0.92);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 11.5px;
    max-height: 45vh;
    overflow-y: auto;
    z-index: 10;
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
  }
  #legend h4 {
    margin-bottom: 6px;
    font-size: 11px;
    color: var(--dim);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  #legend .item {
    display: flex;
    align-items: center;
    gap: 7px;
    margin: 3px 0;
    color: #cbd5e1;
    cursor: pointer;
  }
  #legend .item:hover {
    color: #fff;
  }
  #legend .sw {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    flex: none;
  }
  #side {
    position: absolute;
    top: 0;
    right: -420px;
    width: 400px;
    bottom: 0;
    background: var(--panel);
    border-left: 1px solid var(--line);
    box-shadow: -8px 0 24px rgba(0,0,0,0.5);
    padding: 20px;
    overflow-y: auto;
    transition: right 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    z-index: 30;
  }
  #side.open { right: 0; }
  #side .close {
    position: absolute;
    top: 14px;
    right: 16px;
    cursor: pointer;
    color: var(--dim);
    font-size: 18px;
    padding: 2px 6px;
    border-radius: 4px;
  }
  #side .close:hover { color: #fff; background: rgba(255,255,255,0.08); }
  #side h2 { font-size: 17px; margin-bottom: 2px; word-break: break-all; color: #f8fafc; }
  #side .sub-lib { font-size: 12px; color: var(--dim); margin-bottom: 14px; }
  .section-title {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    color: var(--dim);
    margin: 14px 0 6px;
    font-weight: 700;
  }
  #side table { width: 100%; border-collapse: collapse; margin-bottom: 12px; }
  #side td {
    padding: 5px 6px;
    font-size: 12px;
    border-bottom: 1px solid rgba(51, 65, 85, 0.5);
  }
  #side td:first-child { color: var(--dim); width: 45%; }
  #side td:last-child { font-family: monospace; font-weight: 600; color: #f1f5f9; }
  .dep-list {
    max-height: 150px;
    overflow-y: auto;
    border: 1px solid var(--line);
    border-radius: 6px;
    background: rgba(15, 23, 42, 0.5);
    padding: 4px 8px;
  }
  .dep-item {
    padding: 3px 0;
    font-size: 12px;
    color: var(--accent);
    cursor: pointer;
    text-decoration: none;
    display: block;
  }
  .dep-item:hover { text-decoration: underline; color: #7dd3fc; }
  .dep-empty { font-size: 11.5px; color: var(--dim); font-style: italic; padding: 4px 0; }
  .badge-pill {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
  }
  .zone-pain { background: rgba(239, 68, 68, 0.18); color: #f87171; border: 1px solid #ef4444; }
  .zone-useless { background: rgba(245, 158, 11, 0.18); color: #fbbf24; border: 1px solid #f59e0b; }
  .zone-balanced { background: rgba(34, 197, 94, 0.18); color: #4ade80; border: 1px solid #22c55e; }
  .cycle-badge { background: #ef4444; color: #fff; }
  #fallbackNotice {
    position: absolute;
    inset: 0;
    background: #0f172a;
    display: none;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 12px;
    color: #f8fafc;
    z-index: 100;
  }
</style>
</head>
<body>
<header>
  <div class="header-left">
    <div class="header-title">
      🏗 __TITLE__
      <span class="badge-tag">GoJS Engine</span>
    </div>
    <div class="stats-bar">
      <div class="stats-item">Modules: <span id="statModules">-</span></div>
      <div class="stats-item">Deps: <span id="statDeps">-</span></div>
      <div class="stats-item">Cycles: <span id="statCycles">-</span></div>
    </div>
  </div>
  <div class="controls-bar">
    <div class="search-box">
      <span class="search-icon">🔍</span>
      <input type="text" id="searchInput" placeholder="Search module..." oninput="searchModules(this.value)">
    </div>
    <select id="layoutSelect" onchange="changeLayout(this.value)">
      <option value="layered">Layered Digraph</option>
      <option value="force">Force-Directed</option>
      <option value="tree">Tree Layout</option>
    </select>
    <button onclick="toggleGroups(true)">Expand All</button>
    <button onclick="toggleGroups(false)">Collapse All</button>
    <button onclick="fitView()">Fit</button>
    <button onclick="relayout()">Re-layout</button>
  </div>
</header>

<div id="mainContainer">
  <div id="diagramDiv"></div>
  <div id="overviewDiv">
    <div id="overviewTitle">Minimap</div>
  </div>
  <div id="legend"></div>
  <div id="side">
    <span class="close" onclick="closeSide()">✕</span>
    <div id="sideBody"></div>
  </div>
  <div id="fallbackNotice">
    <h3>GoJS diagram library loading...</h3>
    <p style="color:var(--dim)">Please ensure internet access to cdn.jsdelivr.net</p>
  </div>
</div>

<script>
const DATA = __DATA__;

if (typeof go === 'undefined') {
  document.getElementById('fallbackNotice').style.display = 'flex';
}

document.getElementById('statModules').textContent = DATA.modules;
document.getElementById('statDeps').textContent = DATA.edges;
document.getElementById('statCycles').textContent = DATA.cycles;
if (DATA.cycles > 0) {
  document.getElementById('statCycles').style.color = '#ef4444';
}

// Build Legend
const legendDiv = document.getElementById('legend');
legendDiv.innerHTML = `<h4>Libraries (${DATA.groups.length})</h4>` +
  DATA.groups.map(g => `<div class="item" onclick="focusGroup('${g.label}')"><span class="sw" style="background:${g.color}"></span>${g.label}</div>`).join('') +
  `<div class="item"><span class="sw" style="background:#ef4444"></span>cycle link</div>` +
  `<div class="item"><span class="sw" style="background:#f59e0b"></span>cross-lib link</div>`;

// Dependency maps for fast lookup
const outMap = {}, inMap = {};
DATA.links.forEach(e => {
  (outMap[e.s] = outMap[e.s] || []).push(e.t);
  (inMap[e.t] = inMap[e.t] || []).push(e.s);
});

// Initialize GoJS Diagram
const $ = go.GraphObject.make;

const myDiagram = $(go.Diagram, "diagramDiv", {
  "undoManager.isEnabled": true,
  "animationManager.isEnabled": true,
  initialAutoScale: go.Diagram.Uniform,
  padding: 30,
  layout: $(go.LayeredDigraphLayout, {
    direction: 90,
    layerSpacing: 50,
    columnSpacing: 25,
    setsPortSpots: false,
    aggressiveOption: go.LayeredDigraphLayout.AggressiveMore
  })
});

// Minimap Overview
const myOverview = $(go.Overview, "overviewDiv", {
  observed: myDiagram,
  contentAlignment: go.Spot.Center
});

// Node Selection & Highlight Adornment
const nodeSelectionAdornment =
  $(go.Adornment, "Auto",
    $(go.Shape, "RoundedRectangle", { parameter1: 8, fill: null, stroke: "#38bdf8", strokeWidth: 3 }),
    $(go.Placeholder)
  );

// Node Template
myDiagram.nodeTemplate =
  $(go.Node, "Auto",
    {
      selectionAdornmentTemplate: nodeSelectionAdornment,
      click: (e, node) => showDetails(node.data),
      toolTip:
        $("ToolTip",
          { "Border.fill": "#1e293b", "Border.stroke": "#475569" },
          $(go.TextBlock,
            { margin: 6, font: "12px monospace", stroke: "#f8fafc" },
            new go.Binding("text", "", d =>
              `${d.id}\nLOC: ${d.loc} | Ca: ${d.ca} | Ce: ${d.ce}\nInstability (I): ${d.i} | Abstractness (A): ${d.a}\nZone: ${d.zone}`)
          )
        )
    },
    $(go.Shape, "RoundedRectangle",
      {
        parameter1: 6,
        fill: "#1e293b",
        stroke: "#334155",
        strokeWidth: 1.5,
        cursor: "pointer"
      },
      new go.Binding("stroke", "cycle", c => c ? "#ef4444" : "#334155"),
      new go.Binding("strokeWidth", "cycle", c => c ? 2.5 : 1.5),
      new go.Binding("fill", "isHighlighted", h => h ? "#0c4a6e" : "#1e293b")
    ),
    $(go.Panel, "Vertical",
      { margin: new go.Margin(6, 8, 6, 8) },
      // Header: Dot color + Module Name
      $(go.Panel, "Horizontal",
        { alignment: go.Spot.Left },
        $(go.Shape, "Circle",
          { width: 8, height: 8, strokeWidth: 0, margin: new go.Margin(0, 6, 0, 0) },
          new go.Binding("fill", "groupColor")
        ),
        $(go.TextBlock,
          {
            font: "bold 13px -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
            stroke: "#f8fafc",
            maxSize: new go.Size(200, NaN),
            wrap: go.TextBlock.WrapFit
          },
          new go.Binding("text", "label")
        )
      ),
      // Stats: LOC & Instability
      $(go.Panel, "Horizontal",
        { margin: new go.Margin(3, 0, 0, 0), alignment: go.Spot.Left },
        $(go.TextBlock,
          { font: "11px monospace", stroke: "#94a3b8" },
          new go.Binding("text", "", d => `LOC: ${d.loc} · I: ${d.i}`)
        )
      ),
      // Badge: Zone / Cycle
      $(go.Panel, "Auto",
        { margin: new go.Margin(4, 0, 0, 0), alignment: go.Spot.Left },
        $(go.Shape, "RoundedRectangle",
          { parameter1: 4, strokeWidth: 0 },
          new go.Binding("fill", "zone", z => {
            if (z === "zone of pain") return "#7f1d1d";
            if (z === "zone of uselessness") return "#78350f";
            return "#14532d";
          })
        ),
        $(go.TextBlock,
          { margin: new go.Margin(1, 5, 1, 5), font: "10px sans-serif", stroke: "#f8fafc" },
          new go.Binding("text", "zone")
        )
      )
    )
  );

// Group Template (Dune Library Cluster)
myDiagram.groupTemplate =
  $(go.Group, "Auto",
    {
      layout: $(go.LayeredDigraphLayout, { direction: 90, layerSpacing: 25, columnSpacing: 20 }),
      isSubGraphExpanded: true,
      computesBoundsIncludingLinks: false
    },
    $(go.Shape, "RoundedRectangle",
      {
        parameter1: 8,
        fill: "rgba(30, 41, 59, 0.4)",
        stroke: "#475569",
        strokeWidth: 1.5,
        strokeDashArray: [4, 4]
      },
      new go.Binding("stroke", "color")
    ),
    $(go.Panel, "Vertical",
      { defaultAlignment: go.Spot.Left, margin: 8 },
      $(go.Panel, "Horizontal",
        { defaultAlignment: go.Spot.Center, margin: new go.Margin(0, 0, 6, 0) },
        $("SubGraphExpanderButton", { margin: new go.Margin(0, 6, 0, 0) }),
        $(go.TextBlock,
          { font: "bold 13px sans-serif", stroke: "#f1f5f9" },
          new go.Binding("text", "label")
        ),
        $(go.Shape, "Circle",
          { width: 8, height: 8, strokeWidth: 0, margin: new go.Margin(0, 0, 0, 8) },
          new go.Binding("fill", "color")
        )
      ),
      $(go.Placeholder, { padding: new go.Margin(6, 6, 6, 6) })
    )
  );

// Link Template
myDiagram.linkTemplate =
  $(go.Link,
    {
      routing: go.Link.AvoidsNodes,
      curve: go.Link.JumpOver,
      corner: 6,
      toShortLength: 3,
      toolTip:
        $("ToolTip",
          { "Border.fill": "#1e293b", "Border.stroke": "#475569" },
          $(go.TextBlock,
            { margin: 4, font: "11px monospace", stroke: "#f8fafc" },
            new go.Binding("text", "", d =>
              `${d.s} → ${d.t}\n[${d.kind}] weight: ${d.weight}${d.inCycle ? ' (CYCLE)' : ''}${d.crossLibrary ? ' (cross-lib)' : ''}`)
          )
        )
    },
    $(go.Shape,
      { strokeWidth: 1.2 },
      new go.Binding("stroke", "", d => d.inCycle ? "#ef4444" : d.crossLibrary ? "#f59e0b" : "#475569"),
      new go.Binding("strokeWidth", "inCycle", c => c ? 2.5 : 1.2),
      new go.Binding("strokeDashArray", "inCycle", c => c ? [6, 3] : null)
    ),
    $(go.Shape,
      { toArrow: "Standard", strokeWidth: 0 },
      new go.Binding("fill", "", d => d.inCycle ? "#ef4444" : d.crossLibrary ? "#f59e0b" : "#475569")
    )
  );

// Populate Model
const groupNodes = DATA.groups.map(g => ({
  id: g.label,
  key: g.label,
  label: g.label,
  isGroup: true,
  color: g.color
}));

const moduleNodes = DATA.nodes.map(n => ({
  ...n,
  key: n.id,
  group: n.group
}));

const linkData = DATA.links.map(l => ({
  from: l.s,
  to: l.t,
  ...l
}));

myDiagram.model = new go.GraphLinksModel({
  nodeKeyProperty: "key",
  nodeGroupKeyProperty: "group",
  linkFromKeyProperty: "from",
  linkToKeyProperty: "to",
  nodeDataArray: [...groupNodes, ...moduleNodes],
  linkDataArray: linkData
});

// UI Actions
function fitView() {
  myDiagram.commandHandler.zoomToFit();
}

function relayout() {
  myDiagram.layoutDiagram(true);
}

function changeLayout(type) {
  myDiagram.startTransaction("changeLayout");
  if (type === "layered") {
    myDiagram.layout = $(go.LayeredDigraphLayout, {
      direction: 90,
      layerSpacing: 50,
      columnSpacing: 25,
      setsPortSpots: false,
      aggressiveOption: 2  /* AggressiveMore */
    });
  } else if (type === "force") {
    myDiagram.layout = $(go.ForceDirectedLayout, {
      defaultSpringLength: 70,
      defaultElectricalCharge: 150
    });
  } else if (type === "tree") {
    myDiagram.layout = $(go.TreeLayout, {
      angle: 90,
      layerSpacing: 45,
      nodeSpacing: 30
    });
  }
  myDiagram.commitTransaction("changeLayout");
}

function toggleGroups(expand) {
  myDiagram.startTransaction("toggleGroups");
  myDiagram.nodes.each(n => {
    if (n instanceof go.Group) {
      n.isSubGraphExpanded = expand;
    }
  });
  myDiagram.commitTransaction("toggleGroups");
}

function focusGroup(groupLabel) {
  const g = myDiagram.findNodeForKey(groupLabel);
  if (g) {
    myDiagram.select(g);
    myDiagram.centerRect(g.actualBounds);
  }
}

function searchModules(term) {
  if (!term) {
    myDiagram.clearHighlighteds();
    return;
  }
  myDiagram.startTransaction("search");
  myDiagram.clearHighlighteds();
  const lower = term.toLowerCase();
  let firstMatch = null;
  myDiagram.nodes.each(n => {
    if (!n.data.isGroup && n.data.label && n.data.label.toLowerCase().includes(lower)) {
      n.isHighlighted = true;
      if (!firstMatch) firstMatch = n;
    }
  });
  if (firstMatch) {
    myDiagram.centerRect(firstMatch.actualBounds);
    showDetails(firstMatch.data);
  }
  myDiagram.commitTransaction("search");
}

function closeSide() {
  document.getElementById('side').classList.remove('open');
}

function selectNode(id) {
  const n = myDiagram.findNodeForKey(id);
  if (n) {
    myDiagram.select(n);
    myDiagram.centerRect(n.actualBounds);
    showDetails(n.data);
  }
}

function showDetails(n) {
  if (!n || n.isGroup) return;
  const side = document.getElementById('side');
  const body = document.getElementById('sideBody');
  side.classList.add('open');

  const outs = outMap[n.id] || [];
  const ins = inMap[n.id] || [];

  const zonePill = n.zone === "zone of pain"
    ? `<span class="badge-pill zone-pain">Zone of Pain (D=${n.d})</span>`
    : n.zone === "zone of uselessness"
    ? `<span class="badge-pill zone-useless">Zone of Uselessness (D=${n.d})</span>`
    : `<span class="badge-pill zone-balanced">Balanced (D=${n.d})</span>`;

  const cyclePill = n.cycle ? `<span class="badge-pill cycle-badge">IN CYCLE</span>` : '';

  body.innerHTML = `
    <h2>${n.label}</h2>
    <div class="sub-lib">${n.id} · Library: <b>${n.library || '—'}</b></div>
    <div style="margin-bottom:12px">${zonePill} ${cyclePill}</div>

    <div class="section-title">Robert C. Martin Component Metrics</div>
    <table>
      <tr><td>Lines of Code (LOC)</td><td>${n.loc}</td></tr>
      <tr><td>Afferent Coupling (Ca)</td><td>${n.ca} (incoming)</td></tr>
      <tr><td>Efferent Coupling (Ce)</td><td>${n.ce} (outgoing)</td></tr>
      <tr><td>Instability (I = Ce/(Ca+Ce))</td><td>${n.i}</td></tr>
      <tr><td>Abstractness (A)</td><td>${n.a}</td></tr>
      <tr><td>Distance to Main Sequence (D)</td><td>${n.d}</td></tr>
      <tr><td>Has .mli Interface</td><td>${n.hasInterface ? '✓ Yes' : '✗ No'}</td></tr>
    </table>

    <div class="section-title">Dependencies (${outs.length})</div>
    <div class="dep-list">
      ${outs.length ? outs.map(x => `<a class="dep-item" onclick="selectNode('${x}')">→ ${x}</a>`).join('') : '<div class="dep-empty">None (leaf module)</div>'}
    </div>

    <div class="section-title">Depended on by (${ins.length})</div>
    <div class="dep-list">
      ${ins.length ? ins.map(x => `<a class="dep-item" onclick="selectNode('${x}')">← ${x}</a>`).join('') : '<div class="dep-empty">None (root / entry module)</div>'}
    </div>
  `;
}
</script>
</body>
</html>
"""
