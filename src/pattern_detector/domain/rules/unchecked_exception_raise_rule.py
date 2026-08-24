"""OCaml Unchecked Exception Raise Rule."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class UncheckedExceptionRaiseRule(BasePatternRule):
    """Detects raw exception throwing (failwith, raise) instead of typed Result.t/Option.t."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.UNCHECKED_EXCEPTION_RAISE

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            for fn in m.functions.values():
                body = fn.body
                if "failwith " in body or "raise " in body or "raise_notrace " in body:
                    evidences = [
                        Evidence(
                            description=f"Type Safety Audit: Function '{fn.id_str}' in '{m.name}' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead",
                            weight=0.80,
                            rule_code="UNCHECKED_EXCEPTION_THROW",
                            location=fn.location or m.location,
                        )
                    ]
                    det = self._create_detection(
                        target_name=f"{m.name}.{fn.name}",
                        target_kind="throwing_function",
                        evidences=evidences,
                        location=fn.location or m.location,
                    )
                    detections.append(det)

        return detections
