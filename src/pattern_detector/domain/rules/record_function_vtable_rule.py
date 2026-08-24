"""OCaml Record Function VTable Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class RecordFunctionVTableRule(BasePatternRule):
    """Detects record types containing function fields for object-like VTable dispatch."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.RECORD_FUNCTION_VTABLE

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            for t_name, t in m.types.items():
                if t.is_record:
                    fn_fields = [f for f in t.record_fields if f.is_function or "->" in f.type_str]
                    if len(fn_fields) >= 2:
                        evidences = [
                            Evidence(
                                description=f"Record type '{t_name}' in '{m.name}' implements explicit VTable Virtual Method Table containing {len(fn_fields)} function method(s)",
                                weight=0.85,
                                rule_code="RECORD_VTABLE_METHODS",
                                location=t.location or m.location,
                            )
                        ]
                        det = self._create_detection(
                            target_name=f"{m.name}.{t_name}",
                            target_kind="record_vtable_type",
                            evidences=evidences,
                            location=t.location or m.location,
                        )
                        detections.append(det)

        return detections
