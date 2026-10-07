# DPX-OCaml Architecture Viewer — Specification

**Status:** Phase 1 (MVP) — shipped. Phases 2–3 planned.
**Command:** `dpx viewer` · **Schema:** `architecture.json` v1.0.0 · **Last updated:** 2026-10-07

---

## 1. Purpose

The Architecture Viewer is a browser-based, fully offline interactive map of an
OCaml project's module architecture. It answers three questions in a few clicks:

1. **What is here?** — every Dune library, module, interface, and entity.
2. **How is it connected?** — the dependency graph with *why* evidence
   (`file:line:col` for every edge).
3. **Where and why is there a problem?** — cycles, layer violations, Martin
   metric hotspots, and the 25 pattern/safety findings, each with an
   explanation.

The UX model is "Google Maps for architecture": start at the project overview
(groups = subsystems), drill into a subsystem, then into a module, then into
its entities — and pan back out at any time. Every view is linkable.

## 2. Quick start

```bash
uv run dpx viewer /path/to/ocaml_project        # writes ./dpx_viewer/
uv run dpx viewer . -o reports/view --open      # custom dir + open browser
uv run dpx viewer . --no-patterns               # skip the 25-rule pass (faster)
```

| Option | Effect | Default |
|---|---|---|
| `PATH` | project directory to analyse | `.` |
| `-o, --out` | output directory | `./dpx_viewer` |
| `-e, --exclude` | directory name(s) to skip (repeatable) | — |
| `--no-patterns` | skip pattern detection pass; `findings` everywhere empty | off |
| `--open` | open the HTML in the default browser | off |

**Outputs** (always both):

- `dpx_viewer.html` — a single self-contained file (Cytoscape.js vendored
  inside; no CDN, no server, no JS build step). Open it with `file://`, send
  it to a colleague, or attach it to a PR.
- `architecture.json` — the normalized snapshot (schema §4); the stable
  contract for external tooling and Phase 3 diffs.

## 3. Hexagonal placement

| Component | Role |
|---|---|
| `application/services/viewer_snapshot_service.py` | `ViewerSnapshotService` — orchestrates arch scan + pattern scan + code-model parse, emits the JSON dict |
| `adapters/outbound/formatters/viewer_html_formatter.py` | `ViewerHtmlFormatter` — injects snapshot + vendored Cytoscape into the HTML template |
| `adapters/outbound/formatters/assets/viewer_template.html` | the viewer app (vanilla JS, template placeholders `__DPX_SNAPSHOT_JSON__` / `__DPX_CYTOSCAPE_JS__`) |
| `adapters/inbound/cli/commands/viewer.py` | `dpx viewer` typer command |
| `bootstrap/container.py` | `get_viewer_service()` wiring |

No domain objects leak into the snapshot: it is plain JSON-serializable data.

## 4. `architecture.json` schema (v1.0.0)

Top level:

```jsonc
{
  "schema_version": "1.0.0",
  "project": {
    "name": "...", "path": "...",            // absolute root
    "generated_at": "2026-10-07T12:00:00+00:00",
    "has_dune_manifest": true
  },
  "summary": {
    "files": 12, "modules": 8, "edges": 8, "cycles": 2,
    "issues": 5, "findings": 2, "elapsed_seconds": 0.05
  },
  "libraries":  [ { "name": "arch_domain", "modules": 2, "loc": 17,
                    "depends_on": ["arch_infra"] } ],
  "external_deps": ["str", "threads.posix"],
  "modules":    [ /* Module, see below */ ],
  "edges":      [ /* Edge, see below */ ],
  "cycles":     [ { "id": 0, "members": ["Arch_domain.Order", "…"],
                    "cross_library": false } ],
  "issues":     [ { "severity": "error|warning|info", "kind": "…",
                    "subject": "Arch_domain.Order", "message": "…",
                    "related": ["…"] } ]
}
```

**Module** (file paths are repo-relative POSIX):

```jsonc
{
  "id": "Arch_domain.Order",       // Dune-wrap-aware node id
  "name": "Order", "file": "lib/domain/order.ml", "loc": 7,
  "library": "arch_domain", "layer": "domain|infra|ports|shared|api|unknown",
  "has_interface": true, "is_entry": false, "is_abstract": false,
  "exported_types": 1, "abstract_types": 0, "submodules": [],
  "cycle_id": 0,                   // null when not in a cycle; matches cycles[].id
  "dir": "lib/domain",
  "findings": [ /* Finding, see below */ ],
  "entities": {
    "types":     [ { "name": "status", "kind": "variant|record|gadt|poly_variant|abstract|concrete",
                     "abstract": false, "line": 7 } ],
    "functions": [ { "name": "place", "arity": 1, "complexity": 1,
                     "raises": false, "line": 11 } ]
  },
  "metrics": { "ca": 2, "ce": 2, "instability": 0.5, "abstractness": 0.0,
               "distance": 0.5, "zone": "balanced|zone of pain|zone of uselessness" }
}
```

**Edge** — one aggregated edge per module pair; `locations` is the WHY evidence:

```jsonc
{
  "source": "Arch_domain.Order", "target": "Arch_infra.Db",
  "kind": "open|include|functor_application|qualified_reference",  // strongest kind wins
  "weight": 3,                     // total occurrence count across the unit pair
  "cross_library": true, "cross_layer": true,
  "locations": [
    { "file": "lib/domain/order.ml", "line": 4, "column": 1,
      "occurrence": "Arch_infra.Db" }
  ]
}
```

**Finding** (pattern-scan detection joined to its module):

```jsonc
{
  "pattern": "physical_equality_smell", "category": "safety",
  "target": "==", "target_kind": "expression", "level": "medium",
  "confidence": 0.8, "message": "…",
  "file": "lib2-cycle/parse/parser.ml", "line": 3, "column": 1,
  "node": "Arch_parse.Parser"      // graph node the finding was joined to
}
```

### Caps

| Constant | Value | Where |
|---|---|---|
| `MAX_EDGE_LOCATIONS` | 50 | `ArchitectureScanService._accumulate` — per aggregated edge |
| `MAX_LOCATIONS_PER_EDGE` | 50 | snapshot serialisation of `edges[].locations` |
| `MAX_ENTITIES_PER_MODULE` | 300 | `edges[].entities` per module (types + functions combined) |

### Join keys

Graph nodes carry one canonical path per compilation unit; findings and
entities may reference either side of the `.ml`/`.mli` pair. The join
(`_unit_keys`) maps a node to `{path, sibling.ml, sibling.mli}` (resolved),
so a finding located in `repo.mli` attaches to the node whose file is
`repo.ml`.

## 5. WHY-evidence: the occurrence model

`ModuleDependencyExtractor` emits `DependencyOccurrence(kind, name, file,
line, column)` — 1-based positions valid on the **raw** source, because
`strip_comments_and_strings` blanks comments/strings in place without
changing offsets. Semantics:

- `open A.B` produces **two** occurrences: `open` at the directive start and
  `qualified_reference` at the module path. Both merge into the same edge
  (weight 2) with two distinct locations — the edge inspector can point at
  either.
- Interface-side references are attributed to the `.mli` file with the
  `.mli`'s own line numbering.
- Functor application `module B = F.Make (X)` emits `functor_application`
  occurrences for **both** `F.Make` and `X` at the binding start, plus a
  `qualified_reference` for the functor path.
- An edge's `kind` is the strongest evidence found
  (`open > include > functor_application > qualified_reference`); locations
  are deduplicated by `(file, line, column, occurrence)` and capped at 50.

This is what makes "Why is this arrow here?" answerable: the edge inspector
lists every location, and each one can be checked against the raw file.

## 6. Self-containment guarantees

- **No network.** The vendored Cytoscape.js 3.30.4 is the only third-party
  code. The test suite asserts the HTML contains no remote-loading constructs
  (`src="http…"`, `@import`, `fetch(`, `XMLHttpRequest`, …).
- **No build toolchain.** The viewer is vanilla JS in a `<script id="dpx-app">`
  block; the formatter does two plain string substitutions. `node --check`
  (when available) validates the script syntax in tests.
- **XSS-safe by construction.** The snapshot is embedded via
  `json.dumps(...).replace("</", "<\\/")`; tests embed a hostile
  `</script><script>alert(1)</script>` payload and assert it cannot break out
  of the script element and still JSON-round-trips.

## 7. Screens (MVP)

| Screen | Where | What it shows |
|---|---|---|
| **Architecture Map** | main canvas | overview of groups (dune-library/layer/directory), drill-down per group, node size = LOC, colors = layer; pan/zoom/select; breadcrumbs |
| **Module inspector** | right panel | metrics (Ca/Ce/I/A/D + zone), entity list, depends-on / used-by, pattern findings, architecture issues, ⌖ Focus neighborhood, ⤢ Drill |
| **Edge inspector** | right panel | the WHY panel: kind, weight, cross flags, every `file:line:col` location |
| **Module Explorer** | `Tree` tab | searchable module tree grouped like the map, with issue/finding badges |
| **Cycles** | tab | SCC groups, cross-library flag, click to highlight members on the map |
| **Layers** | tab | hexagonal layer grouping + layer violations |
| **Metrics** | tab | Ca/Ce/I/A/D table + I/A scatter (*zone of pain* visualisation) |
| **Issues** | tab | architecture issues sorted by severity |
| **Findings** | tab | the 25 pattern/safety rules joined to modules |
| **Search** | ⌘K box | fuzzy search over modules, entities, findings, issues |
| **Deep links** | URL hash | `#/module/<id>`, `#/group/<name>` — restorable views |

## 8. Design decisions

1. **Single-file HTML over a React/Vite app (Phase 1).** The viewer must work
   fully offline and be emailable; a JS build chain in a Python package adds
   friction with no MVP benefit. Vanilla JS keeps `dpx viewer` output at ~440 KB.
2. **Schema-first.** `architecture.json` is the product; the HTML is one
   renderer. Phase 2 (React/Monaco) and Phase 3 (diff service) consume the
   same schema, versioned via `schema_version`.
3. **Caps at the domain and presentation layers.** A 1000-module project
   produces hot edges with thousands of occurrences; 50 capped locations keep
   the snapshot bounded while `weight` still tells the true magnitude.
4. **Cytoscape.js** over ELK/d3-force for MVP: batteries-included pan/zoom,
   layouts, and selectors keep the app script small. Re-evaluate for Phase 2
   hierarchical layouts.

## 9. Testing

`tests/test_viewer.py` (21 tests) covers, layer by layer:

- extractor occurrence positions (open/qualified dual emission, `.mli`
  attribution, functor functor+argument) validated against the raw sources;
- `ArchEdge.locations` end-to-end on the `multilib_arch` fixture — exact
  `file:line:col` lists checked against the fixture file contents, plus the
  60-reference cap project (weight 60 → 50 locations);
- snapshot contract: schema, summary counts, cycles/modules join, `.mli`
  finding join, entities, metrics, library rollups, relative paths,
  `--no-patterns`;
- HTML: placeholder substitution, exactly 3 `<script>` blocks, no
  remote-loading constructs, JSON round-trip, hostile-payload escaping,
  `node --check` on the app script;
- CLI via `typer.testing.CliRunner` (always `-o tmp_path`).

## 10. Roadmap

**Phase 2 — Source-level intelligence**
- Monaco-based source view with hover intelligence and in-place occurrences.
- React/Vite viewer consuming the same `architecture.json` (URL-persisted
  view state, keyboard-first navigation).
- Hide-externals, per-library filters, edge-kind filters in the map toolbar.

**Phase 3 — Architecture Diff (CI/PR)**
- `dpx viewer diff old.json new.json` — added/removed modules and edges,
  cycle mutations, metric regressions, new layer violations.
- GitHub PR comment / exit-code gate for architecture regressions.
