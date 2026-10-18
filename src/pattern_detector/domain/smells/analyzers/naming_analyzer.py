"""Clean code smell analyzer for OCaml NAMING conventions."""

from __future__ import annotations

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

#: Standard OCaml idiom single-letter variables that are mathematically or functionally sound
_ALLOWED_SINGLE_LETTERS = {
    "x", "y", "z",  # Coords / elements
    "i", "j", "k",  # Indices / CPS callback
    "_",            # Wildcard
    "t",            # Standard OCaml module type/value
    "f", "g", "h",  # Higher-order functions
    "n", "m",       # Numbers / lengths
    "a", "b", "c",  # Pairs / tuples / type params
    "v",            # Value
    "p",            # Predicate
    "s",            # State / String
    "e",            # Expression / Element
    "r",            # Result / Ref
}

#: Generic identifiers that lack business domain intent
_GENERIC_IDENTIFIERS = {
    "data", "res", "result_val", "temp", "tmp", "val_",
    "item", "items", "foo", "bar", "baz", "info", "obj", "stuff",
}


class NamingSmellAnalyzer(BaseSmellAnalyzer):
    """Detects single letter names, non-descriptive generic names, and inconsistent casing."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.NAMING

    def analyze(
        self,
        code_model: CodeModel,
        sources: dict[str, str],
        thresholds: SmellThresholds,
        component_graph: ComponentGraph | None = None,
        arch_result: ArchitectureScanResult | None = None,
    ) -> list[SmellDetection]:
        detections: list[SmellDetection] = []

        for mod_name, mod in code_model.modules.items():
            file_path = mod.file_path

            for fn_name, fn in mod.functions.items():
                start_line = fn.location.line if fn.location else 1
                lines = fn.body.splitlines() if fn.body else []
                scope_size = max(1, len(lines))
                end_line = start_line + scope_size

                # 1. Single_Letter_Name (identifier_length == 1 EXCEPT common_pattern_variables)
                # Check top-level function name
                if len(fn_name) == 1 and fn_name not in _ALLOWED_SINGLE_LETTERS:
                    detections.append(
                        SmellDetection(
                            smell_id="Single_Letter_Name",
                            category=SmellCategory.NAMING,
                            severity=SmellSeverity.LOW,
                            file=file_path,
                            start_line=start_line,
                            end_line=start_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' uses a single-letter name outside standard "
                                f"functional idioms ({', '.join(sorted(_ALLOWED_SINGLE_LETTERS))})."
                            ),
                            threshold="identifier_length == 1 and not idiom",
                            confidence=0.90,
                            suggested_refactoring="Rename function to describe its action and domain entity (e.g. format_record).",
                        )
                    )

                # Check parameters in functions with substantial scope
                if scope_size >= thresholds.single_letter_min_scope:
                    for p in fn.params:
                        if len(p.name) == 1 and p.name not in _ALLOWED_SINGLE_LETTERS:
                            detections.append(
                                SmellDetection(
                                    smell_id="Single_Letter_Name",
                                    category=SmellCategory.NAMING,
                                    severity=SmellSeverity.LOW,
                                    file=file_path,
                                    start_line=start_line,
                                    end_line=start_line,
                                    symbol=f"{mod_name}.{fn_name}({p.name})",
                                    evidence=(
                                        f"Parameter '{p.name}' in function '{fn_name}' is a single letter "
                                        f"in a non-trivial scope ({scope_size} lines)."
                                    ),
                                    threshold=f"identifier_length == 1 in scope > {thresholds.single_letter_min_scope} lines",
                                    confidence=0.85,
                                    suggested_refactoring=f"Rename parameter '{p.name}' to represent its semantic domain purpose.",
                                )
                            )

                # 2. Non_Descriptive_Name (identifier_is_generic AND scope_size > 20)
                if fn_name.lower() in _GENERIC_IDENTIFIERS and scope_size > thresholds.non_descriptive_scope:
                    detections.append(
                        SmellDetection(
                            smell_id="Non_Descriptive_Name",
                            category=SmellCategory.NAMING,
                            severity=SmellSeverity.LOW,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' uses generic identifier in a scope of {scope_size} lines "
                                f"(threshold: > {thresholds.non_descriptive_scope})."
                            ),
                            threshold=f"generic name in scope > {thresholds.non_descriptive_scope} lines",
                            confidence=0.90,
                            suggested_refactoring="Replace generic name with a precise domain term describing what is handled.",
                        )
                    )

                # Check local let bindings inside function
                local_lets = re.findall(r"\blet\s+([a-zA-Z0-9_]+)\s*=", fn.body)
                for local_var in local_lets:
                    if local_var.lower() in _GENERIC_IDENTIFIERS and scope_size > thresholds.non_descriptive_scope:
                        detections.append(
                            SmellDetection(
                                smell_id="Non_Descriptive_Name",
                                category=SmellCategory.NAMING,
                                severity=SmellSeverity.LOW,
                                file=file_path,
                                start_line=start_line,
                                end_line=end_line,
                                symbol=f"{mod_name}.{fn_name}.let_{local_var}",
                                evidence=(
                                    f"Local variable '{local_var}' in '{fn_name}' has generic naming in a "
                                    f"{scope_size}-line function."
                                ),
                                threshold=f"generic local name in scope > {thresholds.non_descriptive_scope} lines",
                                confidence=0.80,
                                suggested_refactoring=f"Rename '{local_var}' to specify the concrete data structure or concept.",
                            )
                        )

                # 3. Inconsistent_Naming (same_concept_uses_different_names or camelCase in OCaml)
                # OCaml functions and values are idiomatic snake_case. Detect camelCase functions:
                if re.search(r"^[a-z]+[A-Z][a-zA-Z0-9]*$", fn_name) and not fn_name.startswith("of_"):
                    detections.append(
                        SmellDetection(
                            smell_id="Inconsistent_Naming",
                            category=SmellCategory.NAMING,
                            severity=SmellSeverity.LOW,
                            file=file_path,
                            start_line=start_line,
                            end_line=start_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Identifier '{fn_name}' uses camelCase instead of idiomatic OCaml snake_case."
                            ),
                            threshold="casing == camelCase",
                            confidence=0.95,
                            suggested_refactoring=f"Convert '{fn_name}' to snake_case (e.g. {self._to_snake(fn_name)}).",
                        )
                    )

        return detections

    def _to_snake(self, name: str) -> str:
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
