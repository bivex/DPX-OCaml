"""OCaml Lwt / Async Cooperative Concurrency Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class AsyncLwtPromisesRule(BasePatternRule):
    """Detects cooperative asynchronous concurrency via Lwt or Jane Street Async."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.ASYNC_LWT_PROMISES

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            src = m.raw_source
            if "Lwt.bind" in src or "Lwt_main.run" in src or "Lwt.return" in src or "let%bind" in src or "Async.Deferred" in src:
                evidences = [
                    Evidence(
                        description=f"Module '{m.name}' coordinates non-blocking asynchronous event I/O via cooperative promise concurrency (Lwt / Async)",
                        weight=0.85,
                        rule_code="COOPERATIVE_PROMISE_ASYNC",
                        location=m.location,
                    )
                ]
                det = self._create_detection(
                    target_name=m.name,
                    target_kind="async_concurrency_module",
                    evidences=evidences,
                    location=m.location,
                )
                detections.append(det)

        return detections
