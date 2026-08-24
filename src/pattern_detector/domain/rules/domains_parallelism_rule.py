"""OCaml Multicore Domains Parallelism Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class DomainsParallelismRule(BasePatternRule):
    """Detects OCaml 5 Multicore Domains shared-memory parallelism (Domain.spawn, Domainslib)."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.DOMAINS_PARALLELISM

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for m in model.all_modules():
            src = m.raw_source
            if "Domain.spawn" in src or "Domain.join" in src or "Domainslib.Task" in src or "Domain.DLS" in src:
                evidences = [
                    Evidence(
                        description=f"Module '{m.name}' leverages OCaml 5 Multicore Domains parallelism for shared-memory parallel thread execution",
                        weight=0.85,
                        rule_code="DOMAINS_MULTICORE_PARALLELISM",
                        location=m.location,
                    )
                ]
                det = self._create_detection(
                    target_name=m.name,
                    target_kind="domains_parallel_module",
                    evidences=evidences,
                    location=m.location,
                )
                detections.append(det)

        return detections
