"""JSON exporter: machine-readable dump of the full architecture scan result."""

from __future__ import annotations

from pattern_detector.domain.architecture.models import ArchitectureScanResult
from pattern_detector.ports.outbound.arch_exporter_port import (
    ArchitectureExporterPort,
    GraphViewOptions,
)


class JsonArchitectureFormatter(ArchitectureExporterPort):
    """Serialises the scan result (graph, cycles, metrics, issues) as JSON."""

    extension = "json"

    def format(self, result: ArchitectureScanResult, options: GraphViewOptions | None = None) -> str:
        _ = options  # grouping/filtering are presentation concerns of visual exporters
        return result.model_dump_json(indent=2)
