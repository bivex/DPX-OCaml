"""Application service orchestrating OCaml Clean Code Smell Detection."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from pattern_detector.domain.smells.engine import SmellDetectionEngine
from pattern_detector.domain.smells.models import SmellReport
from pattern_detector.ports.inbound.smell_scanner_port import (
    ScanSmellsUseCase,
    SmellScanOptions,
)
from pattern_detector.ports.outbound import ParserPort, SourceProviderPort

if TYPE_CHECKING:
    from pattern_detector.ports.inbound.arch_scanner_port import ScanArchitectureUseCase


class SmellDetectionService(ScanSmellsUseCase):
    """Orchestrates source discovery, AST parsing, architectural topology, and smell detection."""

    def __init__(
        self,
        source_provider: SourceProviderPort,
        parser: ParserPort,
        arch_service: ScanArchitectureUseCase | None = None,
        engine: SmellDetectionEngine | None = None,
    ) -> None:
        self.source_provider = source_provider
        self.parser = parser
        self.arch_service = arch_service
        self.engine = engine or SmellDetectionEngine()

    def scan_smells(self, path: str, options: SmellScanOptions | None = None) -> SmellReport:
        opts = options or SmellScanOptions()
        target = Path(path).resolve()

        # 1. Collect sources
        if target.is_file():
            sources = {str(target): target.read_text(encoding="utf-8", errors="replace")}
        else:
            sources = self.source_provider.get_sources(
                str(target),
                exclude_dirs=opts.exclude_dirs,
            )

        # 2. Parse CodeModel
        code_model = self.parser.parse_sources(sources)

        # 3. Architecture Scan (if available and not single file)
        arch_result = None
        component_graph = None
        if self.arch_service and target.is_dir():
            try:
                from pattern_detector.ports.inbound.arch_scanner_port import (
                    ArchOutputFormat,
                    ArchScanOptions,
                )
                arch_opts = ArchScanOptions(
                    formats=[ArchOutputFormat.TERMINAL],
                    exclude_dirs=opts.exclude_dirs,
                )
                arch_result = self.arch_service.scan_architecture(str(target), options=arch_opts)
                component_graph = arch_result.graph
            except Exception:  # noqa: BLE001, S110
                pass

        # 4. Run Smell Engine
        report = self.engine.run(
            project_path=str(target),
            code_model=code_model,
            sources=sources,
            thresholds=opts.thresholds,
            component_graph=component_graph,
            arch_result=arch_result,
            category_filter=opts.category,
            min_severity=opts.min_severity,
        )

        return report
