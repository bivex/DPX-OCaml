"""Outbound port for exporting smell analysis reports."""

from __future__ import annotations

from typing import Protocol

from pattern_detector.domain.smells.models import SmellReport


class SmellExporterPort(Protocol):
    """Consumer-side port: SmellReport -> formatted string output."""

    @property
    def extension(self) -> str:
        """Default file extension (e.g. 'json', 'md', 'html')."""
        ...

    def format(self, report: SmellReport) -> str:
        """Format the smell detection report into target format string."""
        ...
