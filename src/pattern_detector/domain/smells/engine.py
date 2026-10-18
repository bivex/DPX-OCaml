"""Clean Code Smell Detection Engine orchestrating category analyzers and heuristics."""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.smells.analyzers import ALL_SMELL_ANALYZERS
from pattern_detector.domain.smells.models import (
    SmellCategory,
    SmellDetection,
    SmellReport,
    SmellSeverity,
    SmellThresholds,
)

if TYPE_CHECKING:
    from pattern_detector.domain.architecture.models import (
        ArchitectureScanResult,
        ComponentGraph,
    )


class SmellDetectionEngine:
    """Core domain engine for detecting OCaml clean code smells across all 12 categories."""

    def __init__(self, analyzers=None) -> None:
        self.analyzers = analyzers if analyzers is not None else ALL_SMELL_ANALYZERS

    def run(
        self,
        project_path: str,
        code_model: CodeModel,
        sources: dict[str, str],
        thresholds: SmellThresholds | None = None,
        component_graph: ComponentGraph | None = None,
        arch_result: ArchitectureScanResult | None = None,
        category_filter: SmellCategory | None = None,
        min_severity: SmellSeverity | None = None,
    ) -> SmellReport:
        start_time = time.perf_counter()
        active_thresholds = thresholds or SmellThresholds()
        all_detections: list[SmellDetection] = []

        for analyzer in self.analyzers:
            if category_filter and analyzer.category != category_filter:
                continue
            findings = analyzer.analyze(
                code_model=code_model,
                sources=sources,
                thresholds=active_thresholds,
                component_graph=component_graph,
                arch_result=arch_result,
            )
            all_detections.extend(findings)

        # Apply min_severity filter if specified
        if min_severity:
            all_detections = [d for d in all_detections if d.severity.rank >= min_severity.rank]

        # Compute breakdown counts
        category_counts: dict[str, int] = {}
        severity_counts: dict[str, int] = {}

        for d in all_detections:
            cat_key = d.category.value
            sev_key = d.severity.value
            category_counts[cat_key] = category_counts.get(cat_key, 0) + 1
            severity_counts[sev_key] = severity_counts.get(sev_key, 0) + 1

        elapsed = time.perf_counter() - start_time

        return SmellReport(
            project_path=project_path,
            scanned_files_count=len(sources),
            elapsed_seconds=elapsed,
            thresholds=active_thresholds,
            detections=all_detections,
            category_counts=category_counts,
            severity_counts=severity_counts,
        )
