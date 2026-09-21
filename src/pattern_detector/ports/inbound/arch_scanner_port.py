"""Inbound (driver) port for the project architecture & dependency graph scanner."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Protocol

from pattern_detector.domain.architecture.models import ArchitectureScanResult


class ArchOutputFormat(str, Enum):
    """Supported deliverable formats of the architecture scan."""

    TERMINAL = "terminal"
    MERMAID = "mermaid"
    DOT = "dot"
    HTML = "html"
    JSON = "json"
    ALL = "all"


class GraphGrouping(str, Enum):
    """How module graph nodes are grouped in visual exports."""

    DUNE_LIBRARY = "dune-library"
    LAYER = "layer"
    DIRECTORY = "directory"


@dataclass
class ArchScanOptions:
    """Configuration options for one architecture scan execution."""

    formats: list[ArchOutputFormat] = field(default_factory=lambda: [ArchOutputFormat.TERMINAL])
    group_by: GraphGrouping = GraphGrouping.DUNE_LIBRARY
    show_cycles_only: bool = False
    with_metrics: bool = True
    output_dir: str | None = None
    exclude_dirs: list[str] = field(default_factory=list)
    verbose: bool = False


class ScanArchitectureUseCase(Protocol):
    """Primary inbound port: build the module dependency DAG and analyse project architecture."""

    def scan_architecture(self, path: str, options: ArchScanOptions | None = None) -> ArchitectureScanResult:
        ...
