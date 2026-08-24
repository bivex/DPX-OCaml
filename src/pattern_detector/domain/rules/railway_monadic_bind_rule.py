"""OCaml Railway Monadic Error Pipeline Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class RailwayMonadicBindRule(BasePatternRule):
    """Detects Monadic Railway Error Pipelines (let*, let+, >>=, Result.bind)."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.RAILWAY_MONADIC_BIND

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            for fn in m.functions.values():
                body = fn.body
                bind_count = body.count("let*") + body.count("let+") + body.count(">>=") + body.count("Result.bind") + body.count("Option.bind")
                if bind_count >= 2:
                    evidences = [
                        Evidence(
                            description=f"Function '{fn.id_str}' implements Railway-oriented Monadic pipeline composing {bind_count} sequential bind operation(s)",
                            weight=0.85,
                            rule_code="RAILWAY_MONADIC_BIND_PIPELINE",
                            location=fn.location or m.location,
                        )
                    ]
                    det = self._create_detection(
                        target_name=f"{m.name}.{fn.name}",
                        target_kind="railway_pipeline_function",
                        evidences=evidences,
                        location=fn.location or m.location,
                    )
                    detections.append(det)

        return detections
