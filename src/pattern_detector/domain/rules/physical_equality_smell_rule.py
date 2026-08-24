"""OCaml Physical Equality (==) Bug Risk Rule."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class PhysicalEqualitySmellRule(BasePatternRule):
    """Detects accidental usage of physical pointer equality (== / !=) instead of structural equality (= / <>)."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.PHYSICAL_EQUALITY_SMELL

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            for fn in m.functions.values():
                if " == " in fn.body or " != " in fn.body:
                    evidences = [
                        Evidence(
                            description=f"Type Safety Hazard (Physical Equality): Function '{fn.id_str}' in '{m.name}' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs",
                            weight=0.80,
                            rule_code="PHYSICAL_EQUALITY_COMPARISON",
                            location=fn.location or m.location,
                        )
                    ]
                    det = self._create_detection(
                        target_name=f"{m.name}.{fn.name}",
                        target_kind="physical_equality_function",
                        evidences=evidences,
                        location=fn.location or m.location,
                    )
                    detections.append(det)

        return detections
