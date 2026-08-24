"""OCaml Functor Parametric Module Rule."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class FunctorParametricModuleRule(BasePatternRule):
    """Detects Functor Parametric Modules (module Make (X : S) = struct ... end)."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.FUNCTOR_PARAMETRIC_MODULE

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            if m.is_functor or "module Make (" in m.raw_source or "module Make(" in m.raw_source:
                evidences = [
                    Evidence(
                        description=f"Module '{m.name}' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection",
                        weight=0.85,
                        rule_code="FUNCTOR_PARAMETRIC_MODULE",
                        location=m.location,
                    )
                ]
                det = self._create_detection(
                    target_name=m.name,
                    target_kind="functor_module",
                    evidences=evidences,
                    location=m.location,
                )
                detections.append(det)

        return detections
