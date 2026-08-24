"""OCaml Continuation-Passing Style (CPS) Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class CpsContinuationPassingRule(BasePatternRule):
    """Detects Continuation-Passing Style (CPS) stack-safe recursive routines."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.CPS_CONTINUATION_PASSING

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            for fn in m.functions.values():
                param_names = [p.name for p in fn.params]
                if fn.is_rec and ("k" in param_names or "cont" in param_names or "continuation" in param_names):
                    evidences = [
                        Evidence(
                            description=f"Function '{fn.id_str}' implements Continuation-Passing Style (CPS) ensuring stack-safe tail recursion via callback continuation",
                            weight=0.80,
                            rule_code="CPS_CONTINUATION_PASSING",
                            location=fn.location or m.location,
                        )
                    ]
                    det = self._create_detection(
                        target_name=f"{m.name}.{fn.name}",
                        target_kind="cps_function",
                        evidences=evidences,
                        location=fn.location or m.location,
                    )
                    detections.append(det)

        return detections
