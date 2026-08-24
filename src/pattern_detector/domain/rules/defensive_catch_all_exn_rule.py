"""OCaml Defensive Catch-All Exception Rule."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class DefensiveCatchAllExnRule(BasePatternRule):
    """Detects blanket catch-all exception swallowing (`with _ -> ...`)."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.DEFENSIVE_CATCH_ALL_EXN

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            for fn in m.functions.values():
                if re.search(r"try[\s\S]*?with\s+_\s*->", fn.body) or re.search(r"try[\s\S]*?with\s+Failure\s+_\s*->", fn.body):
                    evidences = [
                        Evidence(
                            description=f"Resilience Smell (Defensive Catch-All): Function '{fn.id_str}' in '{m.name}' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only",
                            weight=0.85,
                            rule_code="DEFENSIVE_CATCH_ALL_SWALLOW",
                            location=fn.location or m.location,
                        )
                    ]
                    det = self._create_detection(
                        target_name=f"{m.name}.{fn.name}",
                        target_kind="defensive_catch_function",
                        evidences=evidences,
                        location=fn.location or m.location,
                    )
                    detections.append(det)

        return detections
