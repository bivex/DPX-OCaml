"""Inbound port for Clean Code Smell Detection."""

from __future__ import annotations

from enum import Enum
from typing import Protocol

from pydantic import BaseModel, Field

from pattern_detector.domain.smells.models import (
    SmellCategory,
    SmellReport,
    SmellSeverity,
    SmellThresholds,
)


class SmellOutputFormat(str, Enum):
    """Output format choices for smell scan results."""

    TERMINAL = "terminal"
    JSON = "json"
    MARKDOWN = "markdown"
    HTML = "html"
    ALL = "all"


class SmellScanOptions(BaseModel):
    """Execution options for clean code smell scanning."""

    formats: list[SmellOutputFormat] = Field(default_factory=lambda: [SmellOutputFormat.TERMINAL])
    category: SmellCategory | None = None
    min_severity: SmellSeverity = SmellSeverity.LOW
    thresholds: SmellThresholds = Field(default_factory=SmellThresholds)
    output_path: str | None = None
    exclude_dirs: list[str] = Field(default_factory=list)
    fail_on_critical: bool = False
    verbose: bool = False


class ScanSmellsUseCase(Protocol):
    """Inbound use case protocol for scanning OCaml code smells."""

    def scan_smells(self, path: str, options: SmellScanOptions | None = None) -> SmellReport:
        ...
