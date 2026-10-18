"""Clean Code Smell Detection domain package for OCaml."""

from pattern_detector.domain.smells.models import (
    SmellCategory,
    SmellDetection,
    SmellReport,
    SmellSeverity,
    SmellThresholds,
)

__all__ = [
    "SmellCategory",
    "SmellDetection",
    "SmellReport",
    "SmellSeverity",
    "SmellThresholds",
]
