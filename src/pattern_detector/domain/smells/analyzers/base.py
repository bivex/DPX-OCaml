"""Base interface and utilities for Clean Code Smell Analyzers."""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.smells.models import (
    SmellCategory,
    SmellDetection,
    SmellThresholds,
)

if TYPE_CHECKING:
    from pattern_detector.domain.architecture.models import (
        ArchitectureScanResult,
        ComponentGraph,
    )


@dataclass
class TopLevelFunction:
    """Represents an extracted top-level OCaml function with complete body span."""

    name: str
    params: list[str] = field(default_factory=list)
    start_line: int = 1
    end_line: int = 1
    body: str = ""
    raw_source: str = ""


def extract_top_level_functions(source_text: str) -> list[TopLevelFunction]:
    """Extract top-level functions from raw source preserving full multi-line bodies."""
    fn_pattern = re.compile(
        r"^([ \t]*)let\s+(?:rec\s+)?([a-zA-Z0-9_!?]+)\s*([^=;\n]*?)=",
        re.MULTILINE,
    )
    matches = list(fn_pattern.finditer(source_text))
    if not matches:
        return []

    valid_matches = [
        m for m in matches if m.group(2) not in ("open", "in", "and", "module", "type", "exception")
    ]
    if not valid_matches:
        return []

    min_indent = min(len(m.group(1)) for m in valid_matches)
    top_matches = [m for m in valid_matches if len(m.group(1)) == min_indent]

    results: list[TopLevelFunction] = []
    for i, m in enumerate(top_matches):
        name = m.group(2)
        params_str = m.group(3).strip()
        start_pos = m.start()
        next_pos = top_matches[i + 1].start() if i + 1 < len(top_matches) else len(source_text)

        start_line = source_text[:start_pos].count("\n") + 1
        end_line = source_text[:next_pos].count("\n") + 1
        body = source_text[m.end():next_pos].strip()

        params = [p.strip("()") for p in params_str.split() if p.strip("()")]
        results.append(
            TopLevelFunction(
                name=name,
                params=params,
                start_line=start_line,
                end_line=end_line,
                body=body,
                raw_source=source_text,
            )
        )
    return results


class BaseSmellAnalyzer(ABC):
    """Abstract base class for OCaml clean code smell category analyzers."""

    @property
    @abstractmethod
    def category(self) -> SmellCategory:
        """The smell category this analyzer inspects."""
        ...

    @abstractmethod
    def analyze(
        self,
        code_model: CodeModel,
        sources: dict[str, str],
        thresholds: SmellThresholds,
        component_graph: ComponentGraph | None = None,
        arch_result: ArchitectureScanResult | None = None,
    ) -> list[SmellDetection]:
        """Run smell detection heuristics and return identified smells."""
        ...
