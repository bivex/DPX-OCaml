"""Tests for the Architecture Viewer pipeline (``dpx viewer``).

Covers the four layers of the feature:

* **Extractor** — ``DependencyOccurrence`` positions are exact and valid on the
  raw source; interface occurrences are attributed to the ``.mli`` file.
* **Architecture scan** — aggregated ``ArchEdge.locations`` carry verifiable
  ``file:line:col`` WHY-evidence, capped at ``MAX_EDGE_LOCATIONS``.
* **Snapshot** — the normalized ``architecture.json`` contract (schema, summary,
  cycles, findings joined across ``.ml``/``.mli`` siblings, entities, libraries).
* **Presentation** — the self-contained HTML (escaping, offline-ness, embedded
  JSON round-trip, JS syntax) and the ``dpx viewer`` CLI command.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest
from typer.testing import CliRunner

from pattern_detector.adapters.inbound.cli.main import app as cli_app
from pattern_detector.adapters.outbound.formatters.viewer_html_formatter import (
    ViewerHtmlFormatter,
)
from pattern_detector.adapters.outbound.parsers.dune_manifest_parser import (
    DuneManifestParser,
)
from pattern_detector.adapters.outbound.parsers.module_dep_extractor import (
    ModuleDependencyExtractor,
)
from pattern_detector.adapters.outbound.parsers.native_ocaml_parser_adapter import (
    NativeOCamlParserAdapter,
)
from pattern_detector.adapters.outbound.persistence.file_source_provider import (
    FileSourceProvider,
)
from pattern_detector.application.services.architecture_scan_service import (
    ArchitectureScanService,
)
from pattern_detector.application.services.detection_service import DetectionService
from pattern_detector.application.services.viewer_snapshot_service import (
    ViewerSnapshotService,
)
from pattern_detector.domain.architecture.models import EdgeKind
from pattern_detector.domain.rules import DEFAULT_RULES

FIXTURE = Path(__file__).resolve().parents[1] / "examples" / "ocaml_samples" / "multilib_arch"

#: Remote-loading constructs that must never appear in the generated HTML.
#: (Bare ``http://`` URLs are fine — the vendored Cytoscape MIT header contains
#: attribution URLs that are never fetched.)
_REMOTE_CONSTRUCTS = [
    'src="http',
    "src='http",
    'href="http',
    "@import",
    "fetch(",
    "XMLHttpRequest",
]

_ORDER_ML = """open Arch_infra.Db
open Types

type status = Pending | Confirmed

let describe n = Printf.sprintf "order:%d" n

let place o =
  let saved = Db.save "orders" in
  ({ o with amount = o.amount +. 1.0 }, if saved then Confirmed else Pending)
"""

_ORDER_MLI = """type t = { mutable amount : float; customer : string }

val describe : int -> string
val place : Types.t -> Types.t * status
"""


def _arch_service() -> ArchitectureScanService:
    return ArchitectureScanService(
        source_provider=FileSourceProvider(),
        dune_parser=DuneManifestParser(),
        extractor=ModuleDependencyExtractor(),
    )


def _snapshot_service() -> ViewerSnapshotService:
    return ViewerSnapshotService(
        arch_service=_arch_service(),
        source_provider=FileSourceProvider(),
        parser=NativeOCamlParserAdapter(),
        detector=DetectionService(rules=list(DEFAULT_RULES)),
    )


def _scan_edge(scan: object, source: str, target: str):
    return next(
        e for e in scan.graph.edges if e.source == source and e.target == target  # type: ignore[attr-defined]
    )


def _snap_edge(snapshot: dict, source: str, target: str) -> dict:
    return next(e for e in snapshot["edges"] if e["source"] == source and e["target"] == target)


def _snap_module(snapshot: dict, module_id: str) -> dict:
    return next(m for m in snapshot["modules"] if m["id"] == module_id)


def _write_repeated_refs_project(root: Path, count: int = 60) -> Path:
    """Tiny Dune project whose ``user.ml`` references ``Helper`` ``count`` times."""
    root.mkdir(parents=True, exist_ok=True)
    (root / "dune-project").write_text("(lang dune 3.0)\n", encoding="utf-8")
    lib = root / "lib"
    lib.mkdir()
    (lib / "dune").write_text("(library (name helpers))\n", encoding="utf-8")
    (lib / "helper.ml").write_text("let value = 42\n", encoding="utf-8")
    refs = "\n".join(f"let u{i} = Helper.value + {i}" for i in range(count))
    (lib / "user.ml").write_text(refs + "\n", encoding="utf-8")
    return root


# ----------------------------------------------------------------------
# Extractor: DependencyOccurrence positions
# ----------------------------------------------------------------------


def test_extractor_occurrences_carry_exact_raw_positions() -> None:
    sources = {"proj/lib/order.ml": _ORDER_ML, "proj/lib/order.mli": _ORDER_MLI}
    info = ModuleDependencyExtractor().extract(sources)["proj/lib/order.ml"]

    assert info.opens == {"Arch_infra.Db": 1, "Types": 1}
    assert info.qualified_refs["Types"] == 2
    assert info.has_interface is True

    occ = {(o.kind, o.name, o.file, o.line, o.column) for o in info.occurrences}
    # open directive: occurrence anchored at the directive start (col 1)…
    assert ("open", "Arch_infra.Db", "proj/lib/order.ml", 1, 1) in occ
    assert ("open", "Types", "proj/lib/order.ml", 2, 1) in occ
    # …plus a qualified-reference occurrence anchored at the module path (col 6)
    assert ("qualified_reference", "Arch_infra.Db", "proj/lib/order.ml", 1, 6) in occ
    # short-form use after `open Arch_infra.Db`
    assert ("qualified_reference", "Db", "proj/lib/order.ml", 9, 15) in occ
    # interface-side references are attributed to the .mli with its own numbering
    assert ("qualified_reference", "Types", "proj/lib/order.mli", 4, 13) in occ
    assert ("qualified_reference", "Types", "proj/lib/order.mli", 4, 24) in occ

    # Positions are valid on the RAW sources (comments/strings stripped in place)
    ml, mli = _ORDER_ML.splitlines(), _ORDER_MLI.splitlines()
    assert ml[0][5:18] == "Arch_infra.Db"
    assert ml[8][14:16] == "Db"
    assert mli[3][12:17] == "Types"
    assert mli[3][23:28] == "Types"


def test_extractor_functor_occurrences_cover_functor_and_argument() -> None:
    src = {"proj/lib/db.ml": "module Backend = Arch_ports.Repo.Make (Store)\n"}
    info = ModuleDependencyExtractor().extract(src)["proj/lib/db.ml"]

    assert info.functor_apps == [("Arch_ports.Repo.Make", "Store")]
    occ = {(o.kind, o.name, o.line, o.column) for o in info.occurrences}
    assert ("functor_application", "Arch_ports.Repo.Make", 1, 1) in occ
    assert ("functor_application", "Store", 1, 1) in occ
    # the functor path itself is also captured as a qualified reference
    assert ("qualified_reference", "Arch_ports.Repo.Make", 1, 18) in occ


# ----------------------------------------------------------------------
# Architecture scan: per-edge file:line:col evidence
# ----------------------------------------------------------------------


def test_edge_locations_are_exact_and_valid_on_raw_source() -> None:
    scan = _arch_service().scan_architecture(str(FIXTURE))
    edge = _scan_edge(scan, "Arch_domain.Order", "Arch_domain.Types")

    assert edge.kind is EdgeKind.OPEN
    assert edge.weight == 3
    assert edge.cross_library is False
    assert [(loc.file, loc.line, loc.column, loc.occurrence) for loc in edge.locations] == [
        (str(FIXTURE / "lib/domain/order.ml"), 5, 1, "Types"),
        (str(FIXTURE / "lib/domain/order.mli"), 6, 13, "Types"),
        (str(FIXTURE / "lib/domain/order.mli"), 6, 24, "Types"),
    ]

    # Every location points at the claimed text in the raw fixture files
    order_ml = (FIXTURE / "lib/domain/order.ml").read_text(encoding="utf-8").splitlines()
    order_mli = (FIXTURE / "lib/domain/order.mli").read_text(encoding="utf-8").splitlines()
    assert order_ml[4].startswith("open Types")
    assert order_mli[5][12:17] == "Types"
    assert order_mli[5][23:28] == "Types"


def test_cross_library_edge_merges_all_evidence_kinds() -> None:
    scan = _arch_service().scan_architecture(str(FIXTURE))
    edge = _scan_edge(scan, "Arch_domain.Order", "Arch_infra.Db")

    assert edge.kind is EdgeKind.OPEN
    assert edge.weight == 3
    assert edge.cross_library is True
    assert edge.cross_layer is True
    assert {(loc.line, loc.column, loc.occurrence) for loc in edge.locations} == {
        (4, 1, "Arch_infra.Db"),  # open directive
        (4, 6, "Arch_infra.Db"),  # module path of the directive
        (12, 15, "Db"),  # short-form use
    }
    assert all(Path(loc.file).name == "order.ml" for loc in edge.locations)
    order_ml = (FIXTURE / "lib/domain/order.ml").read_text(encoding="utf-8").splitlines()
    assert order_ml[11][14:16] == "Db"


def test_functor_application_edge_carries_binding_position() -> None:
    scan = _arch_service().scan_architecture(str(FIXTURE))
    edge = _scan_edge(scan, "Arch_infra.Db", "Arch_ports.Repo")

    assert edge.kind is EdgeKind.FUNCTOR_APPLICATION
    assert edge.cross_library is True
    assert {(loc.line, loc.column) for loc in edge.locations} == {(10, 1), (10, 18)}
    assert all(Path(loc.file).name == "db.ml" for loc in edge.locations)
    db_ml = (FIXTURE / "lib/infra/db.ml").read_text(encoding="utf-8").splitlines()
    assert db_ml[9][17:37] == "Arch_ports.Repo.Make"


def test_edge_locations_are_capped_at_fifty(tmp_path: Path) -> None:
    root = _write_repeated_refs_project(tmp_path)
    scan = _arch_service().scan_architecture(str(root))
    edge = _scan_edge(scan, "Helpers.User", "Helpers.Helper")

    assert edge.weight == 60
    assert len(edge.locations) == 50
    assert len({(l.file, l.line, l.column, l.occurrence) for l in edge.locations}) == 50


# ----------------------------------------------------------------------
# Snapshot: normalized architecture.json contract
# ----------------------------------------------------------------------


@pytest.fixture(scope="module")
def snapshot() -> dict:
    return _snapshot_service().build_snapshot(str(FIXTURE))


def test_snapshot_schema_and_summary(snapshot: dict) -> None:
    assert snapshot["schema_version"] == "1.0.0"
    assert snapshot["project"]["name"] == "multilib_arch"
    assert snapshot["project"]["has_dune_manifest"] is True
    assert set(snapshot) >= {
        "schema_version",
        "project",
        "summary",
        "libraries",
        "external_deps",
        "modules",
        "edges",
        "cycles",
        "issues",
    }

    s = snapshot["summary"]
    assert (s["files"], s["modules"], s["edges"], s["cycles"], s["issues"], s["findings"]) == (
        12,
        8,
        8,
        2,
        5,
        2,
    )


def test_snapshot_cycles_use_id_and_modules_carry_cycle_id(snapshot: dict) -> None:
    cycles = {c["id"]: c for c in snapshot["cycles"]}
    assert set(cycles) == {0, 1}
    assert cycles[0] == {
        "id": 0,
        "members": ["Arch_domain.Order", "Arch_domain.Types"],
        "cross_library": False,
    }
    assert cycles[1]["cross_library"] is True

    assert _snap_module(snapshot, "Arch_domain.Order")["cycle_id"] == 0
    assert _snap_module(snapshot, "Arch_parse.Parser")["cycle_id"] == 1
    assert _snap_module(snapshot, "Arch_infra.Db")["cycle_id"] is None


def test_snapshot_joins_findings_across_mli_sibling(snapshot: dict) -> None:
    repo = _snap_module(snapshot, "Arch_ports.Repo")
    assert [(f["pattern"], f["file"], f["line"], f["column"]) for f in repo["findings"]] == [
        ("functor_parametric_module", "lib/ports/repo.mli", 1, 1)
    ]
    # graph node file is repo.ml — the join must still attach the .mli finding
    assert repo["file"] == "lib/ports/repo.ml"

    parser = _snap_module(snapshot, "Arch_parse.Parser")
    assert parser["findings"][0]["pattern"] == "physical_equality_smell"
    assert parser["findings"][0]["file"] == "lib2-cycle/parse/parser.ml"
    assert parser["findings"][0]["line"] == 3

    for module in snapshot["modules"]:
        for f in module["findings"]:
            assert set(f) == {
                "pattern",
                "category",
                "target",
                "target_kind",
                "confidence",
                "level",
                "message",
                "file",
                "line",
                "column",
                "node",
            }
            assert f["node"] == module["id"]


def test_snapshot_entities_and_metrics(snapshot: dict) -> None:
    order = _snap_module(snapshot, "Arch_domain.Order")
    assert order["entities"]["types"] == [
        {"name": "status", "kind": "variant", "abstract": False, "line": 7}
    ]
    functions = {(f["name"], f["arity"], f["complexity"]) for f in order["entities"]["functions"]}
    assert {("describe", 1, 1), ("place", 1, 1)} <= functions

    helper = _snap_module(snapshot, "Arch_utils.Helper")
    assert [("iterate", 3, 2)] == [
        (f["name"], f["arity"], f["complexity"]) for f in helper["entities"]["functions"]
    ]

    assert order["metrics"] == {
        "ca": 2,
        "ce": 2,
        "instability": 0.5,
        "abstractness": 0.0,
        "distance": 0.5,
        "zone": "balanced",
    }
    assert helper["metrics"]["zone"] == "zone of pain"
    assert _snap_module(snapshot, "Main")["is_entry"] is True


def test_snapshot_libraries_rollup(snapshot: dict) -> None:
    libs = {lib["name"]: lib for lib in snapshot["libraries"]}
    assert set(libs) == {"arch_domain", "arch_infra", "arch_lex", "arch_parse", "arch_ports", "arch_utils"}
    assert libs["arch_domain"]["modules"] == 2
    assert libs["arch_domain"]["loc"] == 17
    assert libs["arch_domain"]["depends_on"] == ["arch_infra"]
    assert libs["arch_lex"]["depends_on"] == ["arch_parse"]
    assert libs["arch_ports"]["depends_on"] == []


def test_snapshot_edges_are_relative_with_locations(snapshot: dict) -> None:
    edge = _snap_edge(snapshot, "Arch_domain.Order", "Arch_domain.Types")
    assert edge["kind"] == "open"
    assert edge["cross_library"] is False
    assert [
        (loc["file"], loc["line"], loc["column"], loc["occurrence"])
        for loc in edge["locations"]
    ] == [
        ("lib/domain/order.ml", 5, 1, "Types"),
        ("lib/domain/order.mli", 6, 13, "Types"),
        ("lib/domain/order.mli", 6, 24, "Types"),
    ]

    db_edge = _snap_edge(snapshot, "Arch_domain.Order", "Arch_infra.Db")
    assert db_edge["cross_library"] is True
    assert db_edge["cross_layer"] is True

    for e in snapshot["edges"]:
        assert set(e) == {
            "source",
            "target",
            "kind",
            "weight",
            "cross_library",
            "cross_layer",
            "locations",
        }
        for loc in e["locations"]:
            assert not loc["file"].startswith("/")
            assert loc["line"] >= 1
            assert loc["column"] >= 1
            assert loc["occurrence"]


def test_snapshot_without_patterns_skips_findings_and_entities() -> None:
    snap = _snapshot_service().build_snapshot(str(FIXTURE), include_patterns=False)
    assert snap["summary"]["findings"] == 0
    assert all(m["findings"] == [] for m in snap["modules"])
    assert all(m["entities"] == {"types": [], "functions": []} for m in snap["modules"])


def test_snapshot_caps_edge_locations_at_fifty(tmp_path: Path) -> None:
    root = _write_repeated_refs_project(tmp_path)
    snap = _snapshot_service().build_snapshot(str(root))
    edge = _snap_edge(snap, "Helpers.User", "Helpers.Helper")

    assert edge["weight"] == 60
    assert len(edge["locations"]) == 50
    assert snap["summary"]["modules"] == 2


# ----------------------------------------------------------------------
# HTML formatter: self-contained offline viewer
# ----------------------------------------------------------------------


@pytest.fixture(scope="module")
def html(snapshot: dict) -> str:
    return ViewerHtmlFormatter().render(snapshot)


def test_html_placeholders_substituted_with_three_scripts(html: str) -> None:
    assert "__DPX_" not in html
    assert html.count("<script") == 3
    assert "window.DPX" in html


def test_html_loads_no_remote_resources(html: str) -> None:
    for construct in _REMOTE_CONSTRUCTS:
        assert construct not in html, construct


def test_html_embeds_snapshot_json_round_trip(html: str, snapshot: dict) -> None:
    marker = "window.DPX = "
    start = html.index(marker) + len(marker)
    payload = html[start : html.index("</script>", start)].strip().rstrip(";")
    assert json.loads(payload.replace("<\\/", "</")) == snapshot


def test_html_escapes_hostile_payload() -> None:
    hostile = {"project": {"name": "</script><script>alert(1)</script>"}}
    html = ViewerHtmlFormatter().render(hostile)

    # the payload cannot break out of the script element
    assert "alert(1)</script>" not in html
    assert "<\\/script>" in html

    marker = "window.DPX = "
    start = html.index(marker) + len(marker)
    payload = html[start : html.index("</script>", start)].strip().rstrip(";")
    assert json.loads(payload.replace("<\\/", "</")) == hostile


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_app_javascript_is_syntactically_valid(html: str, tmp_path: Path) -> None:
    match = re.search(r'<script id="dpx-app">(.*?)</script>', html, re.DOTALL)
    assert match is not None
    app_js = tmp_path / "dpx_app.js"
    app_js.write_text(match.group(1), encoding="utf-8")

    result = subprocess.run(
        ["node", "--check", str(app_js)], capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, result.stderr


# ----------------------------------------------------------------------
# CLI: `dpx viewer`
# ----------------------------------------------------------------------


def test_cli_viewer_writes_snapshot_and_html(tmp_path: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(cli_app, ["viewer", str(FIXTURE), "--out", str(tmp_path)])

    assert result.exit_code == 0, result.output
    snapshot_path = tmp_path / "architecture.json"
    html_path = tmp_path / "dpx_viewer.html"
    assert snapshot_path.exists()
    assert html_path.exists()

    data = json.loads(snapshot_path.read_text(encoding="utf-8"))
    assert data["summary"]["modules"] == 8
    assert data["summary"]["findings"] == 2

    html = html_path.read_text(encoding="utf-8")
    assert "window.DPX" in html
    assert "__DPX_" not in html


def test_cli_viewer_no_patterns_flag(tmp_path: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(
        cli_app, ["viewer", str(FIXTURE), "-o", str(tmp_path), "--no-patterns"]
    )

    assert result.exit_code == 0, result.output
    data = json.loads((tmp_path / "architecture.json").read_text(encoding="utf-8"))
    assert data["summary"]["findings"] == 0
    assert all(m["findings"] == [] for m in data["modules"])
