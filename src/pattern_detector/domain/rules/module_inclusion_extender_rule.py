"""OCaml Module Inclusion & Extension Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class ModuleInclusionExtenderRule(BasePatternRule):
    """Detects module composition and interface extension via `include Module`."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.MODULE_INCLUSION_EXTENDER

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            if m.includes:
                evidences = [
                    Evidence(
                        description=f"Module '{m.name}' extends and composes functionality from {len(m.includes)} included module(s) ({', '.join(m.includes)})",
                        weight=0.80,
                        rule_code="MODULE_INCLUSION_EXTENSION",
                        location=m.location,
                    )
                ]
                det = self._create_detection(
                    target_name=m.name,
                    target_kind="extended_module",
                    evidences=evidences,
                    location=m.location,
                )
                detections.append(det)

        return detections
