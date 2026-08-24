"""OCaml Lazy Memoization Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class LazyMemoizationRule(BasePatternRule):
    """Detects on-demand deferred memoization via `lazy` and `Lazy.force`."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.LAZY_MEMOIZATION

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            src = m.raw_source
            if "lazy " in src or "Lazy.force" in src or "Lazy.from_fun" in src:
                evidences = [
                    Evidence(
                        description=f"Module '{m.name}' integrates Lazy Memoization pattern for deferred on-demand computation and caching",
                        weight=0.80,
                        rule_code="LAZY_MEMOIZED_EVALUATION",
                        location=m.location,
                    )
                ]
                det = self._create_detection(
                    target_name=m.name,
                    target_kind="lazy_memoized_module",
                    evidences=evidences,
                    location=m.location,
                )
                detections.append(det)

        return detections
