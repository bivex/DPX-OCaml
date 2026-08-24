"""Tests for OCaml Domain Models and Value Objects."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel, ModuleModel, FunctionModel
from pattern_detector.domain.value_objects import (
    Confidence,
    ConfidenceLevel,
    Evidence,
    SourceLocation,
)


def test_confidence_calculation():
    evidences = [
        Evidence(description="Found Functor Make", weight=0.8, rule_code="FUNCTOR_MAKE"),
        Evidence(description="Found signature constraint", weight=0.5, rule_code="SIG_CONSTRAINT"),
    ]
    conf = Confidence.from_evidences(evidences)
    # Expected: 1.0 - (1 - 0.8) * (1 - 0.5) = 1.0 - (0.2 * 0.5) = 0.90
    assert abs(conf.score - 0.90) < 1e-4
    assert conf.level == ConfidenceLevel.VERY_HIGH
    assert conf.percentage_str == "90%"


def test_source_location_str():
    loc = SourceLocation(file_path="lib/data_structures/tree.ml", line=42, column=5)
    assert str(loc) == "lib/data_structures/tree.ml:42:5"


def test_circular_module_dependency_detection():
    model = CodeModel()

    mod_a = ModuleModel(name="ModuleA", file_path="lib/a.ml", opens=["ModuleB"])
    mod_b = ModuleModel(name="ModuleB", file_path="lib/b.ml", opens=["ModuleA"])

    model.modules["ModuleA"] = mod_a
    model.modules["ModuleB"] = mod_b

    cycles = model.find_circular_dependencies()
    assert len(cycles) == 1
    assert set(cycles[0]) == {"ModuleA", "ModuleB"}
