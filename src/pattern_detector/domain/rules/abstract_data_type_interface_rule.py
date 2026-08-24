"""OCaml Abstract Data Type (ADT) Signature Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class AbstractDataTypeInterfaceRule(BasePatternRule):
    """Detects Abstract Data Type (ADT) signature encapsulation (`type t`)."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.ABSTRACT_DATA_TYPE_INTERFACE

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            has_t_type = "t" in m.types
            create_fn = m.find_function("create") or m.find_function("make") or m.find_function("empty")

            if has_t_type and create_fn:
                evidences = [
                    Evidence(
                        description=f"Module '{m.name}' encapsulates Abstract Data Type (ADT) via primary type `t` with constructor '{create_fn.name}'",
                        weight=0.80,
                        rule_code="ABSTRACT_DATA_TYPE_SIGNATURE",
                        location=m.location,
                    )
                ]
                det = self._create_detection(
                    target_name=m.name,
                    target_kind="adt_module",
                    evidences=evidences,
                    location=m.location,
                )
                detections.append(det)

        return detections
