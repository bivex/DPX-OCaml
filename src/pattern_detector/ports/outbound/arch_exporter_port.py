"""Outbound (driven) port: exporting architecture scan results (Mermaid, DOT, HTML, Rich, JSON)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from pattern_detector.domain.architecture.models import ArchitectureScanResult


@dataclass
class GraphViewOptions:
    """Presentation options shared by all architecture exporters."""

    group_by: str = "dune-library"  # GraphGrouping value
    show_cycles_only: bool = False
    with_metrics: bool = True


class ArchitectureExporterPort(Protocol):
    """Port for rendering a component graph into a deliverable format."""

    extension: str

    def format(self, result: ArchitectureScanResult, options: GraphViewOptions | None = None) -> str:
        ...
