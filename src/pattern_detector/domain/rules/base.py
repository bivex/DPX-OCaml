"""Base abstractions and protocol for OCaml pattern detection rules."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Protocol, runtime_checkable

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.pattern import PATTERN_CATALOG
from pattern_detector.domain.value_objects import (
    Confidence,
    Evidence,
    PatternCategory,
    PatternType,
    SourceLocation,
)


@runtime_checkable
class PatternRule(Protocol):
    """Protocol that every OCaml pattern detection rule must satisfy."""

    @property
    def pattern_type(self) -> PatternType:
        ...

    @property
    def pattern_category(self) -> PatternCategory:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def description(self) -> str:
        ...

    def detect(self, model: CodeModel) -> list[Detection]:
        ...


class BasePatternRule(ABC):
    """Base class for OCaml pattern rules."""

    @property
    @abstractmethod
    def pattern_type(self) -> PatternType:
        ...

    @property
    def pattern_category(self) -> PatternCategory:
        entry = PATTERN_CATALOG.get(self.pattern_type)
        if entry:
            return entry.category
        return PatternCategory.STRUCTURAL

    @property
    def name(self) -> str:
        entry = PATTERN_CATALOG.get(self.pattern_type)
        if entry:
            return entry.name
        return self.pattern_type.value.replace("_", " ").title()

    @property
    def description(self) -> str:
        entry = PATTERN_CATALOG.get(self.pattern_type)
        if entry:
            return entry.description
        return ""

    @abstractmethod
    def detect(self, model: CodeModel) -> list[Detection]:
        ...

    def _create_detection(
        self,
        target_name: str,
        target_kind: str,
        evidences: list[Evidence],
        location: SourceLocation | None = None,
        related_locations: list[SourceLocation] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Detection:
        return Detection(
            pattern_type=self.pattern_type,
            pattern_category=self.pattern_category,
            target_name=target_name,
            target_kind=target_kind,
            confidence=Confidence.from_evidences(evidences),
            primary_location=location,
            evidences=evidences,
            related_locations=related_locations or [],
            metadata=metadata or {},
        )


def strip_comments_and_strings(text: str) -> str:
    """Blank out OCaml comments (nested) and string/quoted-string literals.

    Newlines inside comments/strings are preserved so line-based analysis stays stable.
    """
    import re
    out: list[str] = []
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch == "(" and i + 1 < n and text[i + 1] == "*":  # nested comment
            depth = 1
            i += 2
            while i < n and depth > 0:
                if text.startswith("(*", i):
                    depth += 1
                    out.append("  ")
                    i += 2
                elif text.startswith("*)", i):
                    depth -= 1
                    out.append("  ")
                    i += 2
                else:
                    out.append(text[i] if text[i] == "\n" else " ")
                    i += 1
        elif ch == '"':  # string literal with escapes
            out.append(" ")
            i += 1
            while i < n:
                if text[i] == "\\":
                    out.append("  " if text[i + 1 : i + 2] == "\n" else " ")
                    i += 2
                    continue
                if text[i] == '"':
                    out.append(" ")
                    i += 1
                    break
                out.append(text[i] if text[i] == "\n" else " ")
                i += 1
        elif ch == "{":  # quoted string literal {| ... |} or {id| ... |id}
            m = re.match(r"\{([A-Za-z0-9_]*)\|", text[i:])
            if m:
                tag = m.group(1)
                closer = f"|{tag}}}"
                end = text.find(closer, i)
                end = n if end == -1 else end + len(closer)
                chunk = text[i:end]
                out.append("".join(c if c == "\n" else " " for c in chunk))
                i = end
            else:
                out.append(ch)
                i += 1
        else:
            out.append(ch)
            i += 1
    return "".join(out)
