"""Clean code smell analyzer for OCaml CONTROL_FLOW."""

from __future__ import annotations

import re
from collections import Counter
from typing import TYPE_CHECKING

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.rules.base import strip_comments_and_strings
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

#: Numeric literals considered benign idiomatic constants
_BENIGN_NUMBERS = {"0", "1", "-1", "2", "0.0", "1.0", "0L", "1L"}


class ControlFlowSmellAnalyzer(BaseSmellAnalyzer):
    """Detects deep match/if nesting, complex booleans, repeated conditions, magic literals, and non-exhaustive matches."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.CONTROL_FLOW

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
            raw_source = sources.get(file_path, mod.raw_source)
            clean_source = strip_comments_and_strings(raw_source)

            # Analyze Magic Numbers and Strings across the module
            self._check_magic_literals(raw_source, clean_source, file_path, mod_name, thresholds, detections)

            for fn_name, fn in mod.functions.items():
                start_line = fn.location.line if fn.location else 1
                end_line = start_line + max(1, len(fn.body.splitlines()))

                # 1. Deep_Match_Nesting (WHEN nested_match_depth > 3)
                match_depth = self._calculate_nested_match_depth(fn.body)
                if match_depth > thresholds.nested_match_depth:
                    detections.append(
                        SmellDetection(
                            smell_id="Deep_Match_Nesting",
                            category=SmellCategory.CONTROL_FLOW,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Nested match expressions in '{fn_name}' reach depth {match_depth} "
                                f"(threshold: > {thresholds.nested_match_depth})."
                            ),
                            threshold=f"> {thresholds.nested_match_depth} match levels",
                            confidence=0.90,
                            suggested_refactoring=(
                                "Combine nested matches into tuple pattern matching (match a, b with ...), "
                                "monadic error chains (Result.bind), or extract inner match blocks."
                            ),
                        )
                    )

                # 2. Nested_If (WHEN nested_if_depth > 3)
                if_depth = self._calculate_nested_if_depth(fn.body)
                if if_depth > thresholds.nested_if_depth:
                    detections.append(
                        SmellDetection(
                            smell_id="Nested_If",
                            category=SmellCategory.CONTROL_FLOW,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Nested if-expressions in '{fn_name}' reach depth {if_depth} "
                                f"(threshold: > {thresholds.nested_if_depth})."
                            ),
                            threshold=f"> {thresholds.nested_if_depth} if levels",
                            confidence=0.90,
                            suggested_refactoring=(
                                "Refactor nested if-then-else pyramids into pattern matching with guards "
                                "or early return pipelines."
                            ),
                        )
                    )

                # 3. Complex_Boolean_Expression (WHEN boolean_operator_count > 5)
                max_bool_ops = self._find_max_boolean_operators(fn.body)
                if max_bool_ops > thresholds.boolean_operator_count:
                    detections.append(
                        SmellDetection(
                            smell_id="Complex_Boolean_Expression",
                            category=SmellCategory.CONTROL_FLOW,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Compound boolean expression in '{fn_name}' contains {max_bool_ops} operators (&& / ||) "
                                f"(threshold: > {thresholds.boolean_operator_count})."
                            ),
                            threshold=f"> {thresholds.boolean_operator_count} boolean operators",
                            confidence=0.85,
                            suggested_refactoring=(
                                "Decompose complex logical condition into self-explanatory local boolean "
                                "predicates (e.g. let is_eligible = ... in let has_quota = ... in)."
                            ),
                        )
                    )

                # 4. Repeated_Conditions (WHEN equivalent_condition_appears_multiple_times)
                repeated_cond = self._find_repeated_conditions(fn.body)
                if repeated_cond:
                    cond_expr, count = repeated_cond
                    detections.append(
                        SmellDetection(
                            smell_id="Repeated_Conditions",
                            category=SmellCategory.CONTROL_FLOW,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Condition '{cond_expr}' is evaluated {count} times redundantly inside '{fn_name}'."
                            ),
                            threshold="equivalent condition appears multiple times",
                            confidence=0.85,
                            suggested_refactoring=(
                                f"Bind condition result to an immutable local let-variable "
                                f"(let is_valid = {cond_expr} in) before branching."
                            ),
                        )
                    )

                # 5. Non_Exhaustive_Match (WHEN pattern_match_is_not_proven_exhaustive, SEVERITY = CRITICAL)
                non_exh = self._check_non_exhaustive_literal_match(fn.body)
                if non_exh:
                    detections.append(
                        SmellDetection(
                            smell_id="Non_Exhaustive_Match",
                            category=SmellCategory.CONTROL_FLOW,
                            severity=SmellSeverity.CRITICAL,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Pattern match on open/literal type in '{fn_name}' ({non_exh}) lacks a catch-all "
                                f"wildcard '_' or complete variant cases, risking Match_failure at runtime."
                            ),
                            threshold="unproven match exhaustiveness",
                            confidence=0.90,
                            suggested_refactoring=(
                                "Add an explicit wildcard branch (_ -> ...) or verify exhaustive coverage "
                                "with typed variant constructors."
                            ),
                        )
                    )

        return detections

    def _calculate_nested_match_depth(self, body: str) -> int:
        lines = body.splitlines()
        max_depth = 0
        current_depth = 0
        for line in lines:
            if re.search(r"\bmatch\b.*?\bwith\b|\bfunction\b", line):
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            # Rough closing heuristic for nested matches
            if line.strip().startswith("in ") or line.strip() == ";;":
                current_depth = max(0, current_depth - 1)
        return max_depth

    def _calculate_nested_if_depth(self, body: str) -> int:
        lines = body.splitlines()
        max_depth = 0
        current_depth = 0
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("if ") and "then" in stripped:
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            if "else" in stripped and not stripped.startswith("else if"):
                current_depth = max(0, current_depth - 1)
        return max_depth

    def _find_max_boolean_operators(self, body: str) -> int:
        # Check within if conditions: if (...) then
        if_conds = re.findall(r"\bif\s+(.*?)\s+then\b", body, re.DOTALL)
        max_ops = 0
        for cond in if_conds:
            ops = len(re.findall(r"&&|\|\|", cond))
            max_ops = max(max_ops, ops)
        return max_ops

    def _find_repeated_conditions(self, body: str) -> tuple[str, int] | None:
        if_conds = [c.strip() for c in re.findall(r"\bif\s+([a-zA-Z0-9_.\(\)\s=<>!+-]+?)\s+then\b", body)]
        counts = Counter(if_conds)
        for cond, count in counts.items():
            if count >= 2 and len(cond) > 4 and not cond.startswith("("):
                return cond, count
        return None

    def _check_non_exhaustive_literal_match(self, body: str) -> str | None:
        # Look for match ... with where branches are numeric or string literals and there is no '| _ ->'
        match_blocks = re.findall(r"match\s+(.*?)\s+with\s+(.*?)(?=\blet\b|\bmatch\b|\Z)", body, re.DOTALL)
        for target, block in match_blocks:
            branches = re.findall(r"\|\s*([^->\n]+)\s*->", block)
            if not branches:
                continue
            has_wildcard = any("_" in b or re.search(r"\b[a-z_][a-zA-Z0-9_']*\b", b) for b in branches)
            has_literals = any(re.match(r'^[0-9]+$|^"[^"]+"$', b.strip()) for b in branches)
            if has_literals and not has_wildcard:
                return f"target: '{target.strip()}', literal branches: {', '.join(b.strip() for b in branches[:3])}"
        return None

    def _check_magic_literals(
        self,
        raw_source: str,
        clean_source: str,
        file_path: str,
        mod_name: str,
        thresholds: SmellThresholds,
        detections: list[SmellDetection],
    ) -> None:
        # Magic Numbers
        # Extract numbers in clean source (no comments/strings)
        numbers = re.findall(r"(?<![a-zA-Z0-9_'])([0-9]+(?:\.[0-9]+)?)(?![a-zA-Z0-9_'])", clean_source)
        num_counts = Counter(n for n in numbers if n not in _BENIGN_NUMBERS)
        for num, count in num_counts.items():
            if count >= thresholds.magic_number_min_occurrences:
                detections.append(
                    SmellDetection(
                        smell_id="Magic_Number",
                        category=SmellCategory.CONTROL_FLOW,
                        severity=SmellSeverity.LOW,
                        file=file_path,
                        start_line=1,
                        end_line=1,
                        symbol=f"{mod_name}.literal_{num}",
                        evidence=(
                            f"Numeric literal '{num}' is repeated {count} times across '{mod_name}' without named binding."
                        ),
                        threshold=f">= {thresholds.magic_number_min_occurrences} occurrences",
                        confidence=0.85,
                        suggested_refactoring=f"Declare named constant (e.g. let default_{num.replace('.', '_')} = {num}).",
                    )
                )

        # Magic Strings (from raw source string literals)
        raw_strings = re.findall(r'"([^"\\]{4,40})"', raw_source)
        str_counts = Counter(s for s in raw_strings if not s.startswith("%") and not s.startswith("/") and len(s) > 3)
        for string_lit, count in str_counts.items():
            if count >= thresholds.magic_string_min_occurrences:
                detections.append(
                    SmellDetection(
                        smell_id="Magic_String",
                        category=SmellCategory.CONTROL_FLOW,
                        severity=SmellSeverity.LOW,
                        file=file_path,
                        start_line=1,
                        end_line=1,
                        symbol=f"{mod_name}.literal_str",
                        evidence=(
                            f"String literal \"{string_lit}\" appears {count} times without named constant."
                        ),
                        threshold=f">= {thresholds.magic_string_min_occurrences} occurrences",
                        confidence=0.85,
                        suggested_refactoring="Bind repeated string to a module-level constant or type constructor.",
                    )
                )
