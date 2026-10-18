"""Unit and integration tests for Clean Code Smell Detection in OCaml."""

from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from pattern_detector.adapters.inbound.cli.main import app
from pattern_detector.adapters.outbound.parsers.native_ocaml_parser_adapter import (
    NativeOCamlParserAdapter,
)
from pattern_detector.domain.smells.engine import SmellDetectionEngine
from pattern_detector.domain.smells.models import (
    SmellCategory,
    SmellSeverity,
    SmellThresholds,
)

runner = CliRunner()


def test_functions_smell_detection():
    source = """
let long_computation a b c d e f =
  let x1 = a + b in
  let x2 = x1 + c in
  let x3 = x2 + d in
  let x4 = x3 + e in
  let x5 = x4 + f in
  let x6 = x5 + 1 in
  let x7 = x6 + 2 in
  let x8 = x7 + 3 in
  let x9 = x8 + 4 in
  let x10 = x9 + 5 in
  let x11 = x10 + 6 in
  let x12 = x11 + 7 in
  let x13 = x12 + 8 in
  let x14 = x13 + 9 in
  let x15 = x14 + 10 in
  let x16 = x15 + 11 in
  let x17 = x16 + 12 in
  let x18 = x17 + 13 in
  let x19 = x18 + 14 in
  let x20 = x19 + 15 in
  let x21 = x20 + 16 in
  let x22 = x21 + 17 in
  let x23 = x22 + 18 in
  let x24 = x23 + 19 in
  let x25 = x24 + 20 in
  let x26 = x25 + 21 in
  let x27 = x26 + 22 in
  let x28 = x27 + 23 in
  let x29 = x28 + 24 in
  let x30 = x29 + 25 in
  let x31 = x30 + 26 in
  let x32 = x31 + 27 in
  let x33 = x32 + 28 in
  let x34 = x33 + 29 in
  let x35 = x34 + 30 in
  let x36 = x35 + 31 in
  let x37 = x36 + 32 in
  let x38 = x37 + 33 in
  let x39 = x38 + 34 in
  let x40 = x39 + 35 in
  let x41 = x40 + 36 in
  let x42 = x41 + 37 in
  let x43 = x42 + 38 in
  let x44 = x43 + 39 in
  let x45 = x44 + 40 in
  let x46 = x45 + 41 in
  let x47 = x46 + 42 in
  let x48 = x47 + 43 in
  let x49 = x48 + 44 in
  let x50 = x49 + 45 in
  let x51 = x50 + 46 in
  x51
"""
    parser = NativeOCamlParserAdapter()
    model = parser.parse_sources({"/tmp/sample.ml": source})
    engine = SmellDetectionEngine()
    report = engine.run(
        project_path="/tmp",
        code_model=model,
        sources={"/tmp/sample.ml": source},
        thresholds=SmellThresholds(function_lines=40, function_parameters=5),
        category_filter=SmellCategory.FUNCTIONS,
    )

    ids = [d.smell_id for d in report.detections]
    assert "Long_Function" in ids
    assert "Too_Many_Arguments" in ids


def test_naming_and_types_smells():
    source = """
type color =
  | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10
  | C11 | C12 | C13 | C14 | C15 | C16

let processData (is_dry_run : bool) =
  let item = List.hd [1; 2; 3] in
  failwith "expected error"
"""
    parser = NativeOCamlParserAdapter()
    model = parser.parse_sources({"/tmp/naming_types.ml": source})
    engine = SmellDetectionEngine()
    report = engine.run(
        project_path="/tmp",
        code_model=model,
        sources={"/tmp/naming_types.ml": source},
        thresholds=SmellThresholds(variant_constructor_count=15),
    )

    ids = [d.smell_id for d in report.detections]
    assert "Large_Variant_Type" in ids
    assert "Boolean_Parameter" in ids
    assert "Partial_Function" in ids
    assert "Weak_Error_Model" in ids
    assert "Inconsistent_Naming" in ids  # camelCase processData


def test_control_flow_smells():
    source = """
let check_flow x y =
  if x > 100 && y > 100 && x < 500 && y < 500 && x != y && x + y > 200 then
    match x with
    | 0 -> "zero"
    | 1 -> "one"
  else
    "other"
"""
    parser = NativeOCamlParserAdapter()
    model = parser.parse_sources({"/tmp/flow.ml": source})
    engine = SmellDetectionEngine()
    report = engine.run(
        project_path="/tmp",
        code_model=model,
        sources={"/tmp/flow.ml": source},
        thresholds=SmellThresholds(boolean_operator_count=4),
        category_filter=SmellCategory.CONTROL_FLOW,
    )

    ids = [d.smell_id for d in report.detections]
    assert "Complex_Boolean_Expression" in ids
    assert "Non_Exhaustive_Match" in ids


def test_state_and_effects_smells():
    source = """
let global_counter = ref 0

let compute_hash data =
  print_endline "Side effect inside pure naming!";
  let temp = ref 0 in
  !temp
"""
    parser = NativeOCamlParserAdapter()
    model = parser.parse_sources({"/tmp/state.ml": source})
    engine = SmellDetectionEngine()
    report = engine.run(
        project_path="/tmp",
        code_model=model,
        sources={"/tmp/state.ml": source},
        category_filter=SmellCategory.STATE_AND_EFFECTS,
    )

    ids = [d.smell_id for d in report.detections]
    assert "Global_State" in ids
    assert "Hidden_Side_Effect" in ids
    assert "Unnecessary_Mutation" in ids


def test_error_handling_swallowed_exception():
    source = """
let safe_read path =
  try
    let ch = open_in path in
    input_line ch
  with _ -> ""
"""
    parser = NativeOCamlParserAdapter()
    model = parser.parse_sources({"/tmp/err.ml": source})
    engine = SmellDetectionEngine()
    report = engine.run(
        project_path="/tmp",
        code_model=model,
        sources={"/tmp/err.ml": source},
        category_filter=SmellCategory.ERROR_HANDLING,
    )

    ids = [d.smell_id for d in report.detections]
    assert "Swallowed_Exception" in ids
    sev = next(d.severity for d in report.detections if d.smell_id == "Swallowed_Exception")
    assert sev == SmellSeverity.HIGH


def test_cli_smells_command_terminal():
    result = runner.invoke(app, ["smells", "examples/ocaml_samples/antipatterns.ml"])
    assert result.exit_code == 0
    assert "Clean Code Smell Detector" in result.output
    assert "Weak_Error_Model" in result.output
    assert "Swallowed_Exception" in result.output


def test_cli_smells_command_json_format(tmp_path: Path):
    out_json = tmp_path / "smells.json"
    result = runner.invoke(app, [
        "smells",
        "examples/ocaml_samples/antipatterns.ml",
        "-f", "json",
        "-o", str(out_json),
    ])
    assert result.exit_code == 0
    assert out_json.exists()

    data = json.loads(out_json.read_text(encoding="utf-8"))
    assert "findings" in data
    assert len(data["findings"]) >= 2
    finding = data["findings"][0]
    assert "smell_id" in finding
    assert "category" in finding
    assert "severity" in finding
    assert "evidence" in finding
    assert "threshold" in finding
    assert "suggested_refactoring" in finding


def test_cli_smells_fail_on_critical():
    # File without critical smells
    result = runner.invoke(app, [
        "smells",
        "examples/ocaml_samples/antipatterns.ml",
        "--fail-on-critical",
    ])
    assert result.exit_code == 0


def test_cli_smells_directory_scan():
    result = runner.invoke(app, ["smells", "examples/ocaml_samples"])
    assert result.exit_code == 0
    assert "Clean Code Smell Detector" in result.output


def test_cli_smells_fail_on_critical_triggered():
    # Directory contains multilib_arch with Public_API_Breakage (CRITICAL)
    result = runner.invoke(app, [
        "smells",
        "examples/ocaml_samples",
        "--fail-on-critical",
    ])
    assert result.exit_code == 1

