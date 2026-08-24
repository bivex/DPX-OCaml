"""OCaml Single Responsibility (God Module) Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class GodModuleSrpRule(BasePatternRule):
    """Detects God Modules in OCaml (excessive functions ≥30 or LOC ≥800)."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.GOD_MODULE_SRP

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            fn_count = len(m.functions)
            loc_count = m.raw_source.count("\n") + 1

            if fn_count >= 30 or loc_count >= 800:
                evidences = [
                    Evidence(
                        description=f"SRP Violation (God Module): Module '{m.name}' defines {fn_count} functions across {loc_count} lines of code, indicating multiple mixed domain responsibilities",
                        weight=0.85,
                        rule_code="SRP_GOD_MODULE",
                        location=m.location,
                    )
                ]
                det = self._create_detection(
                    target_name=m.name,
                    target_kind="god_module",
                    evidences=evidences,
                    location=m.location,
                )
                detections.append(det)

        return detections
