"""Self-contained interactive HTML exporter: force-directed module graph, zero external dependencies.

The produced artifact embeds the full scan payload as JSON plus a vanilla-JS
canvas renderer with zoom, pan, node dragging, click-to-highlight and a module
details side panel. No CDN / network access is required to view it.
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
    """Renders the component graph as a standalone interactive HTML page."""

    extension = "html"

    def format(self, result: ArchitectureScanResult, options: GraphViewOptions | None = None) -> str:
        options = options or GraphViewOptions()
        payload = self._payload(result, options)
        # "</" would terminate the enclosing <script> block; break it defensively.
        data_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
        return (
            _TEMPLATE
            .replace("__DATA__", data_json)
            .replace("__TITLE__", html.escape(result.project_path))
        )

    # ------------------------------------------------------------------

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
                        "i": m.instability if m else 0.0,
                        "a": m.abstractness if m else 0.0,
                        "d": m.main_sequence_distance if m else 0.0,
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
<title>dpx arch — __TITLE__</title>
<style>
  :root { --bg:#14181f; --panel:#1c222c; --line:#2b3442; --text:#dbe4ee; --dim:#8392a6; --accent:#4f8ef7; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--bg); color:var(--text); font:14px/1.45 -apple-system,"Segoe UI",Roboto,sans-serif; overflow:hidden; }
  header { position:fixed; top:0; left:0; right:0; height:52px; display:flex; align-items:center; gap:18px;
           padding:0 18px; background:rgba(20,24,31,.92); border-bottom:1px solid var(--line); z-index:10; }
  header h1 { font-size:15px; font-weight:600; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:40vw; }
  header .stats { color:var(--dim); font-size:12.5px; white-space:nowrap; }
  header button { background:var(--panel); color:var(--text); border:1px solid var(--line); border-radius:6px;
                  padding:5px 12px; font-size:12.5px; cursor:pointer; }
  header button:hover { border-color:var(--accent); color:var(--accent); }
  canvas { position:fixed; inset:52px 0 0 0; cursor:grab; }
  #legend { position:fixed; left:14px; bottom:14px; background:rgba(28,34,44,.92); border:1px solid var(--line);
            border-radius:8px; padding:10px 14px; font-size:12px; max-height:40vh; overflow:auto; }
  #legend .item { display:flex; align-items:center; gap:7px; margin:2px 0; color:var(--dim); }
  #legend .sw { width:10px; height:10px; border-radius:50%; flex:none; }
  #side { position:fixed; top:52px; right:-380px; width:360px; bottom:0; background:var(--panel);
          border-left:1px solid var(--line); padding:18px; overflow-y:auto; transition:right .18s ease; z-index:9; }
  #side.open { right:0; }
  #side h2 { font-size:16px; margin-bottom:4px; word-break:break-all; }
  #side .close { position:absolute; top:10px; right:12px; cursor:pointer; color:var(--dim); font-size:18px; }
  #side table { width:100%; border-collapse:collapse; margin:10px 0; }
  #side td { padding:3px 4px; font-size:12.5px; border-bottom:1px solid var(--line); }
  #side td:first-child { color:var(--dim); width:44%; }
  #side .dep { color:var(--accent); cursor:pointer; display:block; padding:1px 0; font-size:12.5px; }
  #side .dep:hover { text-decoration:underline; }
  #side .badges span { display:inline-block; margin:2px 4px 2px 0; padding:1px 8px; border-radius:10px;
                       font-size:11px; border:1px solid var(--line); color:var(--dim); }
  #side .zone-pain { color:#e05252; } #side .zone-useless { color:#f59f00; }
</style>
</head>
<body>
<header>
  <h1>🏗 __TITLE__</h1>
  <div class="stats" id="stats"></div>
  <button onclick="fitView()">Fit</button>
  <button onclick="relayout()">Re-layout</button>
</header>
<canvas id="cv"></canvas>
<div id="legend"></div>
<div id="side"><span class="close" onclick="closeSide()">✕</span><div id="sideBody"></div></div>
<script>
const DATA = __DATA__;
const cv = document.getElementById('cv'), ctx = cv.getContext('2d');
const side = document.getElementById('side'), sideBody = document.getElementById('sideBody');
const nodes = DATA.nodes.map(n => Object.assign(n, {
  r: 6 + Math.min(10, Math.sqrt(n.loc) / 2.5), vx: 0, vy: 0, x: 0, y: 0, fixed: false }));
const byId = Object.fromEntries(nodes.map(n => [n.id, n]));
const out = {}, inn = {};
DATA.links.forEach(e => { (out[e.s] = out[e.s] || []).push(e.t); (inn[e.t] = inn[e.t] || []).push(e.s); });

document.getElementById('stats').textContent =
  `${DATA.modules} modules · ${DATA.edges} deps · ${DATA.cycles} cycles · grouped by ${DATA.groupBy}`;
document.getElementById('legend').innerHTML = DATA.groups.map(g =>
  `<div class="item"><span class="sw" style="background:${g.color}"></span>${g.label}</div>`).join('') +
  `<div class="item"><span class="sw" style="background:#d63c3c"></span>cycle edge</div>`;

let W = 0, H = 0, view = { x: 0, y: 0, k: 1 }, alpha = 1, selected = null, hover = null;
function resize() {
  const dpr = window.devicePixelRatio || 1;
  W = window.innerWidth; H = window.innerHeight - 52;
  cv.width = W * dpr; cv.height = H * dpr; cv.style.width = W + 'px'; cv.style.height = H + 'px';
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}
window.addEventListener('resize', resize); resize();

(function place() {  // initial circular placement grouped by cluster
  const per = Math.ceil(Math.sqrt(nodes.length)) || 1;
  nodes.forEach((n, i) => {
    const gx = (i % per) / per, gy = Math.floor(i / per) / per;
    n.x = 60 + gx * 900 + (Math.random() - .5) * 80;
    n.y = 60 + gy * 700 + (Math.random() - .5) * 80;
  });
})();

function step() {
  if (alpha > 0.004) {
    const k = 70 * Math.sqrt((W * H) / Math.max(1, nodes.length));
    for (let i = 0; i < nodes.length; i++) {       // repulsion
      const a = nodes[i];
      for (let j = i + 1; j < nodes.length; j++) {
        const b = nodes[j];
        let dx = a.x - b.x, dy = a.y - b.y, d2 = dx * dx + dy * dy || 1;
        if (d2 > 250000) continue;
        const f = (k * k) / d2, d = Math.sqrt(d2), fx = f * dx / d, fy = f * dy / d;
        a.vx += fx; a.vy += fy; b.vx -= fx; b.vy -= fy;
      }
      a.vx += (W / 2 - a.x) * 0.002; a.vy += (H / 2 - a.y) * 0.002;  // gravity to center
    }
    DATA.links.forEach(e => {                        // spring attraction
      const a = byId[e.s], b = byId[e.t]; if (!a || !b) return;
      let dx = b.x - a.x, dy = b.y - a.y, d = Math.sqrt(dx * dx + dy * dy) || 1;
      const f = (d - 90) * 0.015, fx = f * dx / d, fy = f * dy / d;
      a.vx += fx; a.vy += fy; b.vx -= fx; b.vy -= fy;
    });
    nodes.forEach(n => {
      if (n.fixed) { n.vx = n.vy = 0; return; }
      n.vx *= 0.82; n.vy *= 0.82; n.x += Math.max(-25, Math.min(25, n.vx)); n.y += Math.max(-25, Math.min(25, n.vy));
    });
    alpha *= 0.985;
  }
  draw();
  requestAnimationFrame(step);
}

function draw() {
  ctx.clearRect(0, 0, W, H);
  ctx.save(); ctx.translate(view.x, view.y); ctx.scale(view.k, view.k);
  const dimOn = selected !== null;
  const neigh = selected === null ? {} :
    Object.fromEntries([...(out[selected] || []), ...(inn[selected] || [])].map(x => [x, 1]));
  DATA.links.forEach(e => {
    const a = byId[e.s], b = byId[e.t]; if (!a || !b) return;
    const hot = selected !== null && (e.s === selected || e.t === selected);
    ctx.globalAlpha = dimOn && !hot ? 0.07 : 0.55;
    ctx.strokeStyle = e.inCycle ? '#d63c3c' : e.crossLibrary ? '#b0650f' : '#5a6b80';
    ctx.lineWidth = (e.inCycle ? 2.2 : 1) * (hot ? 1.8 : 1);
    const dx = b.x - a.x, dy = b.y - a.y, d = Math.sqrt(dx * dx + dy * dy) || 1;
    const tx = b.x - (dx / d) * (b.r + 3), ty = b.y - (dy / d) * (b.r + 3);   // trim to node edge
    ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(tx, ty); ctx.stroke();
    if (hot || view.k > 1.6) arrow(a, tx, ty, dx / d, dy / d, ctx.strokeStyle); // arrowheads when readable
  });
  ctx.globalAlpha = 1;
  nodes.forEach(n => {
    const isNeigh = selected !== null && (n.id === selected || neigh[n.id]);
    ctx.globalAlpha = dimOn && !isNeigh ? 0.15 : 1;
    ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, 7);
    ctx.fillStyle = n.groupColor; ctx.fill();
    ctx.lineWidth = n.cycle ? 2.5 : n.id === selected ? 3 : 1;
    ctx.strokeStyle = n.cycle ? '#d63c3c' : n.id === selected ? '#ffffff' : '#20242c';
    ctx.stroke();
    if (n.isEntry) { ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(n.x, n.y, 2, 0, 7); ctx.fill(); }
    if (view.k > 0.9 || isNeigh) {
      ctx.globalAlpha = (dimOn && !isNeigh) ? 0.15 : 0.9;
      ctx.font = `${Math.max(9, 10 / view.k)}px sans-serif`; ctx.textAlign = 'center';
      ctx.fillStyle = n.id === selected ? '#ffffff' : '#aebccd';
      ctx.fillText(n.label + (n.hasInterface ? ' 📄' : ''), n.x, n.y + n.r + 11 / view.k + 2);
    }
  });
  ctx.globalAlpha = 1; ctx.restore();
}
function arrow(a, tx, ty, ux, uy, color) {
  const s = 6;
  ctx.beginPath();
  ctx.moveTo(tx, ty);
  ctx.lineTo(tx - s * ux - s * 0.45 * uy, ty - s * uy + s * 0.45 * ux);
  ctx.lineTo(tx - s * ux + s * 0.45 * uy, ty - s * uy - s * 0.45 * ux);
  ctx.closePath(); ctx.fillStyle = color; ctx.fill();
}

function fitView() {
  if (!nodes.length) return;
  let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
  nodes.forEach(n => { x0 = Math.min(x0, n.x); y0 = Math.min(y0, n.y); x1 = Math.max(x1, n.x); y1 = Math.max(y1, n.y); });
  const pad = 70;
  view.k = Math.min(2.2, Math.max(0.15, Math.min(W / (x1 - x0 + pad), H / (y1 - y0 + pad))));
  view.x = W / 2 - view.k * (x0 + x1) / 2; view.y = H / 2 - view.k * (y0 + y1) / 2;
}
function relayout() { alpha = 1; }

function toWorld(mx, my) { return { x: (mx - view.x) / view.k, y: (my - view.y) / view.k }; }
function hit(mx, my) {
  const p = toWorld(mx, my);
  for (let i = nodes.length - 1; i >= 0; i--) {
    const n = nodes[i], dx = p.x - n.x, dy = p.y - n.y;
    if (dx * dx + dy * dy <= (n.r + 4) * (n.r + 4)) return n;
  }
  return null;
}
let drag = null, panning = false, moved = 0, last = null;
cv.addEventListener('mousedown', e => {
  const r = cv.getBoundingClientRect(), mx = e.clientX - r.left, my = e.clientY - r.top;
  moved = 0; last = { x: e.clientX, y: e.clientY };
  const n = hit(mx, my);
  if (n) { drag = n; n.fixed = true; alpha = Math.max(alpha, 0.3); }
  else { panning = true; cv.style.cursor = 'grabbing'; }
});
window.addEventListener('mousemove', e => {
  if (drag) {
    const r = cv.getBoundingClientRect(), p = toWorld(e.clientX - r.left, e.clientY - r.top);
    drag.x = p.x; drag.y = p.y; moved++;
  } else if (panning && last) {
    view.x += e.clientX - last.x; view.y += e.clientY - last.y; moved++;
    last = { x: e.clientX, y: e.clientY };
  }
});
window.addEventListener('mouseup', () => {
  if (drag && moved < 4) select(drag.id);
  if (!drag && panning && moved < 4) closeSide();
  if (drag) drag.fixed = false;
  drag = null; panning = false; cv.style.cursor = 'grab';
});
cv.addEventListener('wheel', e => {
  e.preventDefault();
  const r = cv.getBoundingClientRect(), mx = e.clientX - r.left, my = e.clientY - r.top;
  const f = e.deltaY < 0 ? 1.12 : 1 / 1.12, k2 = Math.min(6, Math.max(0.08, view.k * f));
  view.x = mx - (mx - view.x) * (k2 / view.k); view.y = my - (my - view.y) * (k2 / view.k); view.k = k2;
}, { passive: false });

function select(id) {
  selected = id; const n = byId[id]; if (!n) return;
  const zoneCls = n.zone === 'zone of pain' ? 'zone-pain' : n.zone === 'zone of uselessness' ? 'zone-useless' : '';
  const deps = [...new Set(out[id] || [])].sort(), users = [...new Set(inn[id] || [])].sort();
  sideBody.innerHTML = `
    <h2>${n.id}</h2>
    <div class="badges"><span>${n.library || 'no library'}</span><span>${n.layer}</span>
      ${n.hasInterface ? '<span>.mli</span>' : ''}${n.isEntry ? '<span>entry point</span>' : ''}
      ${n.cycle ? '<span style="color:#d63c3c;border-color:#d63c3c">in cycle</span>' : ''}</div>
    <table>
      <tr><td>LOC</td><td>${n.loc}</td></tr>
      <tr><td>Afferent Ca</td><td>${n.ca} module(s) depend on it</td></tr>
      <tr><td>Efferent Ce</td><td>depends on ${n.ce} module(s)</td></tr>
      <tr><td>Instability I</td><td>${(+n.i).toFixed(2)}</td></tr>
      <tr><td>Abstractness A</td><td>${(+n.a).toFixed(2)}</td></tr>
      <tr><td>Main-seq D</td><td>${(+n.d).toFixed(2)} <span class="${zoneCls}">(${n.zone})</span></td></tr>
    </table>
    <strong>Depends on (${deps.length})</strong>${deps.map(d => `<span class="dep" onclick="select('${d}')">→ ${d}</span>`).join('') || '<div class="dim">none</div>'}
    <p></p><strong>Used by (${users.length})</strong>${users.map(u => `<span class="dep" onclick="select('${u}')">← ${u}</span>`).join('') || '<div class="dim">none</div>'}`;
  side.classList.add('open');
}
function closeSide() { selected = null; side.classList.remove('open'); }

fitView(); step();
</script>
</body>
</html>
"""
