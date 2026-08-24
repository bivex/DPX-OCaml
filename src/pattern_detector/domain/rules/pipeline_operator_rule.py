"""OCaml Pipeline Operator Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class PipelineOperatorRule(BasePatternRule):
    """Detects functional data pipelines using `|>` or `@@`."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.PIPELINE_OPERATOR

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            for fn in m.functions.values():
                pipe_count = fn.body.count("|>")
                if pipe_count >= 3:
                    evidences = [
                        Evidence(
                            description=f"Function '{fn.id_str}' composes functional data transformations across a {pipe_count}-stage pipe (`|>`)",
                            weight=0.75,
                            rule_code="PIPELINE_OPERATOR_CHAIN",
                            location=fn.location or m.location,
                        )
                    ]
                    det = self._create_detection(
                        target_name=f"{m.name}.{fn.name}",
                        target_kind="pipeline_function",
                        evidences=evidences,
                        location=fn.location or m.location,
                    )
                    detections.append(det)

        return detections
