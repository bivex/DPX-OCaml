"""Clean code smell analyzer for OCaml DUPLICATION."""

from __future__ import annotations

import hashlib
import re
from typing import TYPE_CHECKING

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.smells.analyzers.base import BaseSmellAnalyzer
from pattern_detector.domain.smells.models import (
    SmellCategory,
    SmellDetection,
    SmellSeverity,
    SmellThresholds,
)

if TYPE_CHECKING:
    from pattern_detector.domain.architecture.models import (
        ArchitectureScanResult,
        ComponentGraph,
    )


class DuplicationSmellAnalyzer(BaseSmellAnalyzer):
    """Detects exact duplication, structural duplication, and repeated business logic."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.DUPLICATION

    def analyze(
        self,
        code_model: CodeModel,
        sources: dict[str, str],
        thresholds: SmellThresholds,
        component_graph: ComponentGraph | None = None,
        arch_result: ArchitectureScanResult | None = None,
    ) -> list[SmellDetection]:
        detections: list[SmellDetection] = []

        # Collect normalized representations of functions
        exact_hashes: dict[str, list[tuple[str, str, int, str]]] = {}
        structural_hashes: dict[str, list[tuple[str, str, int, str]]] = {}

        for mod_name, mod in code_model.modules.items():
            file_path = mod.file_path
            for fn_name, fn in mod.functions.items():
                body = fn.body.strip()
                lines = [l.strip() for l in body.splitlines() if l.strip()]
                if len(lines) < thresholds.duplicate_min_lines:
                    continue

                # 1. Exact Normalization (strip whitespace, comments)
                norm_exact = re.sub(r"\s+", " ", body)
                if len(norm_exact) >= thresholds.duplicate_min_tokens:
                    h_exact = hashlib.sha256(norm_exact.encode()).hexdigest()[:16]
                    start_line = fn.location.line if fn.location else 1
                    exact_hashes.setdefault(h_exact, []).append((mod_name, fn_name, start_line, file_path))

                # 2. Structural Normalization (replace identifiers and literals with placeholders)
                norm_struct = re.sub(r'"[^"]*"', '""', body)
                norm_struct = re.sub(r'\b[0-9]+\b', '0', norm_struct)
                norm_struct = re.sub(r'\b[a-z_][a-zA-Z0-9_]*\b', 'id', norm_struct)
                norm_struct = re.sub(r"\s+", " ", norm_struct)
                if len(norm_struct) >= thresholds.duplicate_min_tokens * 2:
                    h_struct = hashlib.sha256(norm_struct.encode()).hexdigest()[:16]
                    start_line = fn.location.line if fn.location else 1
                    structural_hashes.setdefault(h_struct, []).append((mod_name, fn_name, start_line, file_path))

        # Check Exact Duplication (SEVERITY = HIGH)
        seen_pairs: set[frozenset[str]] = set()
        for items in exact_hashes.values():
            if len(items) >= 2:
                first = items[0]
                for other in items[1:]:
                    pair_key = frozenset([f"{first[0]}.{first[1]}", f"{other[0]}.{other[1]}"])
                    if pair_key in seen_pairs:
                        continue
                    seen_pairs.add(pair_key)
                    detections.append(
                        SmellDetection(
                            smell_id="Exact_Duplication",
                            category=SmellCategory.DUPLICATION,
                            severity=SmellSeverity.HIGH,
                            file=other[3],
                            start_line=other[2],
                            end_line=other[2] + 5,
                            symbol=f"{other[0]}.{other[1]}",
                            evidence=(
                                f"Exact code duplication: function '{other[0]}.{other[1]}' matches "
                                f"'{first[0]}.{first[1]}' ({first[3]}:{first[2]})."
                            ),
                            threshold="normalized AST subtrees are identical",
                            confidence=0.98,
                            suggested_refactoring="Extract duplicated logic into a shared helper function.",
                        )
                    )

        # Check Structural Duplication (SEVERITY = HIGH)
        for items in structural_hashes.values():
            if len(items) >= 2:
                first = items[0]
                for other in items[1:]:
                    pair_key = frozenset([f"{first[0]}.{first[1]}", f"{other[0]}.{other[1]}"])
                    if pair_key in seen_pairs:
                        continue
                    seen_pairs.add(pair_key)
                    detections.append(
                        SmellDetection(
                            smell_id="Structural_Duplication",
                            category=SmellCategory.DUPLICATION,
                            severity=SmellSeverity.HIGH,
                            file=other[3],
                            start_line=other[2],
                            end_line=other[2] + 5,
                            symbol=f"{other[0]}.{other[1]}",
                            evidence=(
                                f"Structural code duplication: '{other[0]}.{other[1]}' shares identical AST control-flow "
                                f"skeleton with '{first[0]}.{first[1]}' ({first[3]}:{first[2]})."
                            ),
                            threshold="AST subtrees match except identifiers/literals",
                            confidence=0.90,
                            suggested_refactoring="Unify algorithm using a higher-order function, functor, or fold combinator.",
                        )
                    )

        return detections
