"""OCaml Polymorphic Open Variants Rule."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class PolymorphicVariantsRule(BasePatternRule):
    """Detects Polymorphic Open Variants (`Tag)."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.POLYMORPHIC_VARIANTS

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            src = m.raw_source
            poly_matches = re.findall(r"`[A-Z][a-zA-Z0-9_]*", src)
            if len(poly_matches) >= 3:
                evidences = [
                    Evidence(
                        description=f"Module '{m.name}' adopts Polymorphic Variants (`{poly_matches[0]}, `{poly_matches[1]}) providing open tag subtyping without nominal declarations",
                        weight=0.80,
                        rule_code="POLYMORPHIC_OPEN_VARIANTS",
                        location=m.location,
                    )
                ]
                det = self._create_detection(
                    target_name=m.name,
                    target_kind="polymorphic_variant_module",
                    evidences=evidences,
                    location=m.location,
                )
                detections.append(det)

        return detections
