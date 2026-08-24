"""OCaml Mutable Reference Overuse Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class MutableRefOveruseRule(BasePatternRule):
    """Detects excessive use of mutable refs / fields violating functional immutability."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.MUTABLE_REF_OVERUSE

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            ref_count = m.raw_source.count("ref ") + m.raw_source.count("mutable ")
            if ref_count >= 4:
                evidences = [
                    Evidence(
                        description=f"Functional Purity Audit: Module '{m.name}' defines {ref_count} mutable references / fields, breaking immutability; favor pure recursive accumulators",
                        weight=0.75,
                        rule_code="MUTABLE_STATE_OVERUSE",
                        location=m.location,
                    )
                ]
                det = self._create_detection(
                    target_name=m.name,
                    target_kind="mutable_state_module",
                    evidences=evidences,
                    location=m.location,
                )
                detections.append(det)

        return detections
