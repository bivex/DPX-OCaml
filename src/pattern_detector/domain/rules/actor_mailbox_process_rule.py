"""OCaml Actor Mailbox Process Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class ActorMailboxProcessRule(BasePatternRule):
    """Detects Actor mailbox message queues and event processing loops."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.ACTOR_MAILBOX_PROCESS

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            for fn in m.functions.values():
                if fn.is_rec and ("mailbox" in fn.body or "msg_queue" in fn.body or "channel" in fn.body) and ("Queue.pop" in fn.body or "Event.receive" in fn.body or "Event.sync" in fn.body):
                    evidences = [
                        Evidence(
                            description=f"Function '{fn.id_str}' in '{m.name}' implements Actor Mailbox Message Loop processing concurrent message channels",
                            weight=0.85,
                            rule_code="ACTOR_MAILBOX_LOOP",
                            location=fn.location or m.location,
                        )
                    ]
                    det = self._create_detection(
                        target_name=f"{m.name}.{fn.name}",
                        target_kind="actor_mailbox_function",
                        evidences=evidences,
                        location=fn.location or m.location,
                    )
                    detections.append(det)

        return detections
