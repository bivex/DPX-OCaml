"""OCaml First-Class Module Dynamic Dispatch Rule."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class FirstClassModuleRule(BasePatternRule):
    """Detects First-Class Modules ((module M : S)) used for dynamic polymorphism."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.FIRST_CLASS_MODULE

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            src = m.raw_source
            if re.search(r"\(\s*module\s+[A-Z][a-zA-Z0-9_]*\s*:\s*[A-Z][a-zA-Z0-9_]*\s*\)", src) or "(val " in src:
                evidences = [
                    Evidence(
                        description=f"Module '{m.name}' utilizes First-Class Modules for dynamic runtime dispatch and pluggable strategy injection",
                        weight=0.85,
                        rule_code="FIRST_CLASS_MODULE_DISPATCH",
                        location=m.location,
                    )
                ]
                det = self._create_detection(
                    target_name=m.name,
                    target_kind="first_class_module",
                    evidences=evidences,
                    location=m.location,
                )
                detections.append(det)

        return detections
