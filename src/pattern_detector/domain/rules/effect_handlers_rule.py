"""OCaml Algebraic Effect Handlers (OCaml 5) Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class EffectHandlersRule(BasePatternRule):
    """Detects OCaml 5 Algebraic Effect Handlers (Effect.perform, Effect.Deep.try_with)."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.EFFECT_HANDLERS

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            src = m.raw_source
            if "Effect.perform" in src or "Effect.Deep" in src or "Effect.Shallow" in src or "type _ Effect.t +=" in src:
                evidences = [
                    Evidence(
                        description=f"Module '{m.name}' adopts OCaml 5 Algebraic Effect Handlers for direct-style concurrency, state, and algebraic control flow",
                        weight=0.90,
                        rule_code="ALGEBRAIC_EFFECT_HANDLERS",
                        location=m.location,
                    )
                ]
                det = self._create_detection(
                    target_name=m.name,
                    target_kind="effect_handler_module",
                    evidences=evidences,
                    location=m.location,
                )
                detections.append(det)

        return detections
