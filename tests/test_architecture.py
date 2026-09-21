"""Tests for the architecture & dependency graph scanner (``dpx arch``)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from pattern_detector.adapters.outbound.formatters.dot_formatter import (
    DotArchitectureFormatter,
)
from pattern_detector.adapters.outbound.formatters.graph_grouping import group_key
from pattern_detector.adapters.outbound.formatters.html_graph_formatter import (
    HtmlGraphFormatter,
)
from pattern_detector.adapters.outbound.formatters.json_formatter import (
    JsonArchitectureFormatter,
)
from pattern_detector.adapters.outbound.formatters.mermaid_formatter import (
    MermaidArchitectureFormatter,
)
from pattern_detector.adapters.outbound.formatters.terminal_formatter import (
    TerminalArchitectureFormatter,
)
from pattern_detector.adapters.outbound.parsers.dune_manifest_parser import (
    DuneManifestParser,
    SExpressionError,
    parse_sexp,
    tokenize,
)
from pattern_detector.adapters.outbound.parsers.module_dep_extractor import (
    ModuleDependencyExtractor,
    strip_comments_and_strings,
)
from pattern_detector.adapters.outbound.persistence.file_source_provider import (
    FileSourceProvider,
)
from pattern_detector.application.services.architecture_scan_service import (
    ArchitectureScanService,
)
from pattern_detector.domain.architecture.cycle_detector import (
    detect_cycles,
    strongly_connected_components,
)
from pattern_detector.domain.architecture.metrics import compute_module_metrics
from pattern_detector.domain.architecture.models import (
    ArchEdge,
    ArchLayer,
    ComponentGraph,
    EdgeKind,
    ModuleNode,
    infer_layer,
)
from pattern_detector.ports.inbound.arch_scanner_port import (
    ArchScanOptions,
    GraphGrouping,
)
from pattern_detector.ports.outbound.arch_exporter_port import GraphViewOptions

FIXTURE = Path(__file__).resolve().parents[1] / "examples" / "ocaml_samples" / "multilib_arch"


def scan_fixture(**option_kwargs: object) -> object:
    service = ArchitectureScanService(
        source_provider=FileSourceProvider(),
        dune_parser=DuneManifestParser(),
        extractor=ModuleDependencyExtractor(),
    )
    options = ArchScanOptions(**option_kwargs) if option_kwargs else None  # type: ignore[arg-type]
    return service.scan_architecture(str(FIXTURE), options=options)


# ----------------------------------------------------------------------
# Dune manifest parser: S-expression primitives
# ----------------------------------------------------------------------


def test_tokenize_handles_parens_quotes_and_comments() -> None:
    text = '(library (name arch_x)) ; trailing comment\n("quoted string")'
    assert tokenize(text) == [
        "(",
        "library",
        "(",
        "name",
        "arch_x",
        ")",
        ")",
        "(",
        '"quoted string"',
        ")",
    ]


def test_parse_sexp_nested_structure() -> None:
    parsed = parse_sexp("(library (name foo) (libraries bar baz))")
    assert parsed == [["library", ["name", "foo"], ["libraries", "bar", "baz"]]]


def test_parse_sexpr_rejects_unbalanced() -> None:
    with pytest.raises(SExpressionError):
        parse_sexp("(library (name foo)")


def test_parse_project_multi_library(tmp_path: Path) -> None:
    (tmp_path / "dune-project").write_text("(lang dune 3.0)\n(name proj)\n")
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib" / "dune").write_text(
        "(library (name my_lib) (public_name my-lib) (libraries base stdio))\n"
    )
    (tmp_path / "tool").mkdir()
    (tmp_path / "tool" / "dune").write_text("(executable (name main) (libraries my_lib))\n")

    tree = DuneManifestParser().parse_project(str(tmp_path))

    assert tree.dune_project is not None
    assert tree.dune_project.lang_version == "3.0"
    assert len(tree.libraries) == 1
    lib = tree.libraries[0]
    assert lib.name == "my_lib"
    assert lib.public_name == "my-lib"
    assert lib.libraries == ["base", "stdio"]
    assert lib.wrapped is True
    assert len(tree.manifests[0].executables) == 0

    exe = tree.manifests[1].executables[0] if len(tree.manifests) > 1 else None
    # The executable stanza may live in a second manifest directory.
    all_execs = [e for m in tree.manifests for e in m.executables]
    assert any("main" in e.names for e in all_execs)
    assert exe is None or "main" in exe.names


def test_parse_project_unwrapped_and_select(tmp_path: Path) -> None:
    (tmp_path / "dune").write_text(
        "(library (name plain) (wrapped false) "
        "(libraries (select x from (lib_a -> a.ml) (lib_b -> b.ml))))\n"
    )
    tree = DuneManifestParser().parse_project(str(tmp_path))
    lib = tree.libraries[0]
    assert lib.wrapped is False
    assert set(lib.libraries) == {"lib_a", "lib_b"}


def test_parse_project_without_dune_is_empty(tmp_path: Path) -> None:
    tree = DuneManifestParser().parse_project(str(tmp_path))
    assert tree.libraries == []
    assert tree.manifests == []
    assert tree.dune_project is None


# ----------------------------------------------------------------------
# Module dependency extractor
# ----------------------------------------------------------------------


def test_module_name_of_capitalizes_first_letter() -> None:
    assert ModuleDependencyExtractor.module_name_of("my_module") == "My_module"
    assert ModuleDependencyExtractor.module_name_of("Already") == "Already"


def test_strip_comments_and_strings_blanks_only_payloads() -> None:
    src = '(* open Foo *)\nlet s = "open Bar"\nlet x = 1\n'
    stripped = strip_comments_and_strings(src)
    assert "Foo" not in stripped
    assert "Bar" not in stripped
    assert "let x = 1" in stripped
    assert stripped.count("\n") == src.count("\n")  # line structure preserved


def test_extract_opens_includes_refs_functors() -> None:
    sources = {
        "src/app.ml": (
            "open Base\n"
            "open! Stdio\n"
            "include Helper\n"
            "module Backend = Registry.Make (Sqlite)\n"
            "let v = Core.List.length []\n"
        )
    }
    infos = ModuleDependencyExtractor().extract(sources)
    info = infos["src/app.ml"]

    assert info.module_name == "App"
    assert info.opens == {"Base": 1, "Stdio": 1}
    assert info.includes == {"Helper": 1}
    assert ("Registry.Make", "Sqlite") in info.functor_apps
    assert info.qualified_refs.get("Core.List") == 1
    # `module Backend = Registry.Make (...)` is a functor application, not a
    # struct/sig submodule definition, so it must not appear in `submodules`.
    assert "Backend" not in info.submodules
    assert info.has_interface is False
    assert info.is_interface_only is False


def test_extract_submodules() -> None:
    sources = {"src/store.ml": "module Inner = struct let x = 1 end\n"}
    info = ModuleDependencyExtractor().extract(sources)["src/store.ml"]
    assert info.submodules == ["Inner"]


def test_extract_merges_interface_pair() -> None:
    sources = {
        "src/repo.mli": "type t\nval save : string -> t -> unit\n",
        "src/repo.ml": "type t = { db : string }\nlet save _ _ = ()\n",
    }
    infos = ModuleDependencyExtractor().extract(sources)
    assert list(infos) == ["src/repo.ml"]  # pair keyed by the .ml path
    info = infos["src/repo.ml"]
    assert info.module_name == "Repo"
    assert info.has_interface is True
    assert info.is_interface_only is False
    assert info.defines_type_t is True
    # The interface defines the exported contract: `type t` (abstract) + t in `val`.
    assert info.exported_types >= 1
    assert info.abstract_types >= 1


def test_extract_interface_only_unit() -> None:
    sources = {"src/contract.mli": "type t\n"}
    infos = ModuleDependencyExtractor().extract(sources)
    # Interface-only units are keyed by their virtual .ml path.
    info = infos["src/contract.ml"]
    assert info.is_interface_only is True
    assert info.has_interface is True
    assert info.file_path == "src/contract.mli"


def test_count_loc_ignores_blank_lines() -> None:
    assert ModuleDependencyExtractor.count_loc("\nlet a = 1\n\nlet b = 2\n") == 2


# ----------------------------------------------------------------------
# Cycle detection (Tarjan SCC)
# ----------------------------------------------------------------------


def test_scc_finds_two_cycles_and_self_loop() -> None:
    adjacency = {
        "a": {"b"},
        "b": {"c"},
        "c": {"a", "d"},
        "d": {"e"},
        "e": {"d"},
        "f": set(),
        "s": {"s"},  # self-referencing module
    }
    components = strongly_connected_components(adjacency)
    sizes = sorted(len(c) for c in components)
    # Singletons without a self-loop are filtered out; "f" never appears.
    assert sizes == [1, 2, 3]
    members = {frozenset(c) for c in components}
    assert frozenset({"a", "b", "c"}) in members
    assert frozenset({"d", "e"}) in members
    assert ["s"] in components


def test_detect_cycles_groups_and_cross_library_flag() -> None:
    graph = ComponentGraph(
        nodes={
            "Lib.A": ModuleNode(id="Lib.A", name="A", file_path="a.ml", dune_library="lib"),
            "Lib.B": ModuleNode(id="Lib.B", name="B", file_path="b.ml", dune_library="lib"),
            "Lib.C": ModuleNode(id="Lib.C", name="C", file_path="c.ml", dune_library="lib"),
            "Other.S": ModuleNode(id="Other.S", name="S", file_path="s.ml", dune_library="other"),
        },
        edges=[
            ArchEdge(source="Lib.A", target="Lib.B"),
            ArchEdge(source="Lib.B", target="Lib.A"),
            ArchEdge(source="Lib.C", target="Lib.A"),
            ArchEdge(source="Other.S", target="Other.S"),
        ],
    )
    cycles = detect_cycles(graph)
    assert len(cycles) == 2
    cycle_of_a = next(c for c in cycles if "Lib.A" in c.members)
    assert set(cycle_of_a.members) == {"Lib.A", "Lib.B"}
    assert cycle_of_a.cross_library is False
    assert ["Other.S"] in [c.members for c in cycles]  # self-loop survives
    # Node cycle_id attachment is the scan service's job (see fixture e2e test).


# ----------------------------------------------------------------------
# Martin metrics
# ----------------------------------------------------------------------


def _metrics_graph() -> ComponentGraph:
    nodes = {
        "Core": ModuleNode(
            id="Core",
            name="Core",
            file_path="core.mli",
            has_interface=True,
            abstract_types=2,
            exported_types=2,
        ),
        "Service": ModuleNode(id="Service", name="Service", file_path="service.ml"),
        "Util": ModuleNode(id="Util", name="Util", file_path="util.ml"),
        "Api": ModuleNode(
            id="Api",
            name="Api",
            file_path="api.mli",
            has_interface=True,
            abstract_types=2,
            exported_types=2,
        ),
    }
    edges = [
        # Service depends on Core (aggregated to one edge regardless of weight).
        ArchEdge(source="Service", target="Core", kind=EdgeKind.OPEN, weight=2),
        # Util is depended upon but depends on nothing.
        ArchEdge(source="Service", target="Util"),
        # Api is fully abstract yet depends outward and nobody uses it.
        ArchEdge(source="Api", target="Service"),
    ]
    return ComponentGraph(nodes=nodes, edges=edges)


def test_compute_module_metrics_ca_ce_instability() -> None:
    metrics = compute_module_metrics(_metrics_graph())
    core, service, util, api = metrics["Core"], metrics["Service"], metrics["Util"], metrics["Api"]

    assert core.ca == 1  # Service -> Core
    assert core.ce == 0
    assert core.instability == pytest.approx(0.0)

    assert service.ca == 1  # Api -> Service
    assert service.ce == 2  # distinct dependency targets, not summed weights
    assert service.instability == pytest.approx(2 / 3, abs=1e-3)  # rounded to 3 decimals

    # Abstractness: interface module with only abstract exports is fully abstract.
    assert core.abstractness == pytest.approx(1.0)
    assert service.abstractness == pytest.approx(0.0)  # no interface, no exports

    # D = |A + I - 1|: Core sits exactly on the Main Sequence.
    assert core.main_sequence_distance == pytest.approx(0.0)
    assert core.zone == "balanced"

    # Service: A=0, I=2/3 -> D = 1/3, still balanced.
    # Metrics round to 3 decimals, so compare with matching tolerance.
    assert service.main_sequence_distance == pytest.approx(1 / 3, abs=1e-3)

    # Util: depended upon, depends on nothing -> I=0, A=0, D=1: zone of pain.
    assert util.instability == pytest.approx(0.0)
    assert util.main_sequence_distance == pytest.approx(1.0)
    assert util.zone == "zone of pain"

    # Api: fully abstract AND fully unstable (I=1) -> zone of uselessness.
    assert api.ca == 0
    assert api.ce == 1
    assert api.instability == pytest.approx(1.0)
    assert api.abstractness == pytest.approx(1.0)
    assert api.main_sequence_distance == pytest.approx(1.0)
    assert api.zone == "zone of uselessness"


def test_abstractness_fallback_without_interface() -> None:
    # No .mli and no exported types -> concrete (A=0); .mli without types -> A=1.
    graph = ComponentGraph(
        nodes={
            "Plain": ModuleNode(id="Plain", name="Plain", file_path="p.ml"),
            "Empty": ModuleNode(id="Empty", name="Empty", file_path="e.mli", has_interface=True),
        },
        edges=[],
    )
    metrics = compute_module_metrics(graph)
    assert metrics["Plain"].abstractness == pytest.approx(0.0)
    assert metrics["Empty"].abstractness == pytest.approx(1.0)


# ----------------------------------------------------------------------
# Layer classification
# ----------------------------------------------------------------------


def test_infer_layer_outermost_segment_wins() -> None:
    assert infer_layer(("lib", "domain", "order.ml")) is ArchLayer.DOMAIN
    assert infer_layer(("lib", "ports", "repo.ml")) is ArchLayer.PORTS
    assert infer_layer(("lib", "infrastructure", "db.ml")) is ArchLayer.INFRASTRUCTURE
    assert infer_layer(("lib", "utils", "helper.ml")) is ArchLayer.SHARED
    assert infer_layer(("bin", "main.ml")) is ArchLayer.API
    # The outer boundary wins over deeper, conflicting hints.
    assert infer_layer(("adapters", "http", "routes.ml")) is ArchLayer.ADAPTERS
    assert infer_layer(("adapters", "inbound", "cli", "shell.ml")) is ArchLayer.ADAPTERS
    assert infer_layer(("lib", "api", "http.ml")) is ArchLayer.API
    # Name fallback for entry points when no segment matches.
    assert infer_layer(("somewhere", "x.ml"), module_name="Main") is ArchLayer.API
    assert infer_layer(("somewhere", "mystery.ml")) is ArchLayer.UNKNOWN


# ----------------------------------------------------------------------
# Graph grouping helpers
# ----------------------------------------------------------------------


def test_group_key_by_library_layer_directory() -> None:
    node = ModuleNode(id="X", name="X", file_path="/p/lib/domain/x.ml", dune_library="arch_x", layer=ArchLayer.DOMAIN)
    assert group_key(node, GraphGrouping.DUNE_LIBRARY.value, "/p") == "arch_x"
    assert group_key(node, GraphGrouping.LAYER.value, "/p") == "domain"
    assert group_key(node, GraphGrouping.DIRECTORY.value, "/p") == "lib/domain"


# ----------------------------------------------------------------------
# End-to-end scan over the multi-library fixture
# ----------------------------------------------------------------------


def test_scan_fixture_full_result() -> None:
    result = scan_fixture()

    assert result.has_dune_manifest is True
    assert result.modules_count == 8
    assert result.edges_count == 8
    assert set(result.graph.library_deps) >= {"arch_domain", "arch_lex", "arch_parse"}

    ids = set(result.graph.nodes)
    assert "Arch_domain.Order" in ids
    assert "Arch_ports.Repo" in ids
    assert "Arch_infra.Db" in ids
    assert "Arch_utils.Helper" in ids

    # Entry point detection: bin/main.ml
    main = result.graph.nodes["Main"]
    assert main.is_entry is True
    assert main.layer is ArchLayer.API

    # Functor application resolved to the defining compilation unit.
    functor_edges = [e for e in result.graph.edges if e.kind is EdgeKind.FUNCTOR_APPLICATION]
    assert any(e.source == "Arch_infra.Db" and e.target == "Arch_ports.Repo" for e in functor_edges)

    # Two cycles: intra-library and cross-library.
    assert len(result.cycles) == 2
    cross = [c for c in result.cycles if c.cross_library]
    assert len(cross) == 1
    assert set(cross[0].members) == {"Arch_lex.Lexer", "Arch_parse.Parser"}

    kinds = [i.kind.value for i in result.issues]
    assert kinds.count("circular_dependency") == 2
    assert "layer_violation" in kinds
    assert "orphan_module" in kinds

    violation = next(i for i in result.issues if i.kind.value == "layer_violation")
    assert violation.subject == "Arch_domain.Order"
    assert "Arch_infra.Db" in violation.related


def test_scan_without_dune_falls_back_to_filesystem(tmp_path: Path) -> None:
    (tmp_path / "a.ml").write_text("open B\nlet x = B.y\n")
    (tmp_path / "b.ml").write_text("open A\n")
    service = ArchitectureScanService(
        source_provider=FileSourceProvider(),
        dune_parser=DuneManifestParser(),
        extractor=ModuleDependencyExtractor(),
    )
    result = service.scan_architecture(str(tmp_path))
    assert result.has_dune_manifest is False
    assert result.modules_count == 2
    assert len(result.cycles) == 1  # A -> B -> A even without any dune metadata
    node_ids = set(result.graph.nodes)
    assert node_ids == {"A", "B"}


def test_qualified_ref_routes_to_longest_module_not_wrapper(tmp_path: Path) -> None:
    (tmp_path / "dune-project").write_text("(lang dune 3.0)\n")
    (tmp_path / "lib_a").mkdir()
    (tmp_path / "lib_a" / "dune").write_text("(library (name lib_a))\n")
    (tmp_path / "lib_a" / "mod_x.ml").write_text("let value = 42\n")
    (tmp_path / "lib_a" / "lib_a.ml").write_text("module Mod_x = Mod_x\n")

    (tmp_path / "lib_b").mkdir()
    (tmp_path / "lib_b" / "dune").write_text("(library (name lib_b) (libraries lib_a))\n")
    (tmp_path / "lib_b" / "consumer.ml").write_text("let x = Lib_a.Mod_x.value\n")

    service = ArchitectureScanService(
        source_provider=FileSourceProvider(),
        dune_parser=DuneManifestParser(),
        extractor=ModuleDependencyExtractor(),
    )
    result = service.scan_architecture(str(tmp_path))

    # Should route to Lib_a.Mod_x, NEVER to wrapper Lib_a.Lib_a
    edges = [(e.source, e.target) for e in result.graph.edges]
    assert ("Lib_b.Consumer", "Lib_a.Mod_x") in edges
    assert ("Lib_b.Consumer", "Lib_a.Lib_a") not in edges
    assert len(result.cycles) == 0


def test_local_module_shadows_sibling_unit(tmp_path: Path) -> None:
    (tmp_path / "dune-project").write_text("(lang dune 3.0)\n")
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib" / "dune").write_text("(library (name my_lib))\n")
    (tmp_path / "lib" / "helper.ml").write_text("let run () = ()\n")
    (tmp_path / "lib" / "caller.ml").write_text(
        "module Helper = struct let run () = () end\n"
        "let test () = Helper.run ()\n"
    )

    service = ArchitectureScanService(
        source_provider=FileSourceProvider(),
        dune_parser=DuneManifestParser(),
        extractor=ModuleDependencyExtractor(),
    )
    result = service.scan_architecture(str(tmp_path))

    # Helper is shadowed by the local submodule definition; no edge to My_lib.Helper
    edges = [(e.source, e.target) for e in result.graph.edges]
    assert ("My_lib.Caller", "My_lib.Helper") not in edges
    assert len(result.cycles) == 0


def test_bare_fallback_prevented_across_libraries(tmp_path: Path) -> None:
    (tmp_path / "dune-project").write_text("(lang dune 3.0)\n")
    (tmp_path / "lib_a").mkdir()
    (tmp_path / "lib_a" / "dune").write_text("(library (name lib_a))\n")
    (tmp_path / "lib_a" / "random.ml").write_text("let x = 1\n")

    (tmp_path / "lib_b").mkdir()
    (tmp_path / "lib_b" / "dune").write_text("(library (name lib_b))\n")
    (tmp_path / "lib_b" / "user.ml").write_text("let r = Random.int 10\n")

    service = ArchitectureScanService(
        source_provider=FileSourceProvider(),
        dune_parser=DuneManifestParser(),
        extractor=ModuleDependencyExtractor(),
    )
    result = service.scan_architecture(str(tmp_path))

    # Bare Random.int in lib_b must NOT resolve to Lib_a.Random via global fallback
    edges = [(e.source, e.target) for e in result.graph.edges]
    assert ("Lib_b.User", "Lib_a.Random") not in edges
    assert len(result.cycles) == 0


# ----------------------------------------------------------------------
# Formatter smoke tests
# ----------------------------------------------------------------------


def _view(**kwargs: object) -> GraphViewOptions:
    return GraphViewOptions(**kwargs)  # type: ignore[arg-type]


def test_terminal_formatter_report() -> None:
    result = scan_fixture()
    text = TerminalArchitectureFormatter().format(result, _view(with_metrics=True))
    assert "Arch_domain.Order" in text
    assert "CIRCULAR" in text or "circular" in text.lower()
    assert "layer inversion" in text
    assert "orphan" in text.lower()


def test_mermaid_formatter_structure() -> None:
    result = scan_fixture()
    text = MermaidArchitectureFormatter().format(result, _view(group_by=GraphGrouping.LAYER.value))
    assert text.startswith("%%")
    assert "graph TD" in text
    assert "subgraph" in text
    assert "==>" in text  # thick cycle links
    assert "Arch_domain_Order" in text  # sanitized ids
    assert 'stroke:#e05252' in text


def test_dot_formatter_clusters() -> None:
    result = scan_fixture()
    text = DotArchitectureFormatter().format(result, _view())
    assert "digraph architecture" in text
    assert "subgraph cluster_" in text
    assert '"Arch_domain.Order"' in text
    # Cycle edges are highlighted.
    assert '#d63c3c' in text


def test_html_formatter_self_contained() -> None:
    result = scan_fixture()
    text = HtmlGraphFormatter().format(result, _view())
    assert "const DATA =" in text
    assert "http://" not in text and "https://" not in text  # no CDN
    assert "<canvas" in text
    # The JSON payload lives on a single line after `const DATA = `.
    payload = text.split("const DATA = ", 1)[1].split("\n", 1)[0]
    assert "Arch_domain.Order" in payload
    assert "</" not in payload.replace("<\\/", "")  # script-breakout escaped


def test_json_formatter_round_trip() -> None:
    result = scan_fixture()
    text = JsonArchitectureFormatter().format(result, _view())
    data = json.loads(text)
    assert data["modules_count"] == 8
    assert data["edges_count"] == 8
    assert len(data["cycles"]) == 2
    assert any(i["kind"] == "layer_violation" for i in data["issues"])


def test_show_cycles_only_filters_formatters() -> None:
    result = scan_fixture()
    text = MermaidArchitectureFormatter().format(result, _view(show_cycles_only=True))
    assert "Arch_domain_Order" in text  # cycle member stays visible
    assert "Helper" not in text  # orphan (non-cycle) module is filtered out
    assert "Main" not in text  # entry module is filtered out too


def test_multi_param_functor_does_not_create_spurious_edge(tmp_path: Path) -> None:
    (tmp_path / "dune-project").write_text("(lang dune 3.0)\n")
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib" / "dune").write_text("(library (name my_lib))\n")
    (tmp_path / "lib" / "conf.ml").write_text("let config = 1\n")
    (tmp_path / "lib" / "worker.ml").write_text(
        "module Make (Conf : Config) (Data : Data_sig) =\n"
        "struct\n"
        "  let c = Conf.length\n"
        "  let d = Data.val_\n"
        "end\n"
    )

    service = ArchitectureScanService(
        source_provider=FileSourceProvider(),
        dune_parser=DuneManifestParser(),
        extractor=ModuleDependencyExtractor(),
    )
    result = service.scan_architecture(str(tmp_path))
    edges = [(e.source, e.target) for e in result.graph.edges]
    assert ("My_lib.Worker", "My_lib.Conf") not in edges
    assert len(result.cycles) == 0


def test_functor_type_signature_param_does_not_create_cycle(tmp_path: Path) -> None:
    (tmp_path / "dune-project").write_text("(lang dune 3.0)\n")
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib" / "dune").write_text("(library (name my_lib))\n")
    (tmp_path / "lib" / "store.ml").write_text("include Store_intf\nlet x = 1\n")
    (tmp_path / "lib" / "store_intf.ml").write_text(
        "module type Json_tree = functor (Store : S) -> sig val f : Store.t end\n"
    )

    service = ArchitectureScanService(
        source_provider=FileSourceProvider(),
        dune_parser=DuneManifestParser(),
        extractor=ModuleDependencyExtractor(),
    )
    result = service.scan_architecture(str(tmp_path))
    edges = [(e.source, e.target) for e in result.graph.edges]
    # Store in functor (Store : S) must NOT create an edge from Store_intf to Store
    assert ("My_lib.Store_intf", "My_lib.Store") not in edges
    assert len(result.cycles) == 0


def test_module_type_local_shadows_compilation_unit(tmp_path: Path) -> None:
    (tmp_path / "dune-project").write_text("(lang dune 3.0)\n")
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib" / "dune").write_text("(library (name my_lib))\n")
    (tmp_path / "lib" / "error.ml").write_text("include Error_intf\n")
    (tmp_path / "lib" / "error_intf.ml").write_text(
        "module type Error = sig val x : int end\n"
        "module type S = sig\n"
        "  include Error\n"
        "end\n"
    )

    service = ArchitectureScanService(
        source_provider=FileSourceProvider(),
        dune_parser=DuneManifestParser(),
        extractor=ModuleDependencyExtractor(),
    )
    result = service.scan_architecture(str(tmp_path))
    edges = [(e.source, e.target) for e in result.graph.edges]
    # include Error inside error_intf refers to local module type Error, not sibling unit
    assert ("My_lib.Error_intf", "My_lib.Error") not in edges
    assert len(result.cycles) == 0


def test_ppx_extension_on_module_declaration(tmp_path: Path) -> None:
    (tmp_path / "dune-project").write_text("(lang dune 3.0)\n")
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib" / "dune").write_text("(library (name my_lib))\n")
    (tmp_path / "lib" / "monad.ml").write_text("include Monad_intf\n")
    (tmp_path / "lib" / "monad_intf.ml").write_text(
        "module%template.portable Of_monad (Monad : S) = struct let t = Monad.t end\n"
    )

    service = ArchitectureScanService(
        source_provider=FileSourceProvider(),
        dune_parser=DuneManifestParser(),
        extractor=ModuleDependencyExtractor(),
    )
    result = service.scan_architecture(str(tmp_path))
    edges = [(e.source, e.target) for e in result.graph.edges]
    assert ("My_lib.Monad_intf", "My_lib.Monad") not in edges
    assert len(result.cycles) == 0

