"""Clean code smell analyzer for OCaml FUNCTIONS."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.smells.analyzers.base import (
    BaseSmellAnalyzer,
    extract_top_level_functions,
)
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


class FunctionsSmellAnalyzer(BaseSmellAnalyzer):
    """Analyzes OCaml functions for length, complexity, parameters, nesting, and responsibilities."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.FUNCTIONS

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
            top_funcs = extract_top_level_functions(raw_source)

            for fn in top_funcs:
                fn_name = fn.name
                start_line = fn.start_line
                end_line = fn.end_line
                num_lines = end_line - start_line + 1

                # 1. Long_Function (WHEN function_lines > 50)
                if num_lines > thresholds.function_lines:
                    detections.append(
                        SmellDetection(
                            smell_id="Long_Function",
                            category=SmellCategory.FUNCTIONS,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' spans {num_lines} lines of code "
                                f"(threshold: > {thresholds.function_lines})."
                            ),
                            threshold=f"> {thresholds.function_lines} lines",
                            confidence=0.95,
                            suggested_refactoring=(
                                "Extract cohesive sub-blocks into private helper functions or compose "
                                "them using monadic pipelines (let* / >>=/ |>)."
                            ),
                        )
                    )

                # 2. High_Cyclomatic_Complexity (WHEN cyclomatic_complexity > 10)
                # Compute thorough cyclomatic complexity: 1 + if + match/function cases + && + || + try/with
                cc = self._calculate_cyclomatic_complexity(fn.body)
                if cc > thresholds.cyclomatic_complexity:
                    detections.append(
                        SmellDetection(
                            smell_id="High_Cyclomatic_Complexity",
                            category=SmellCategory.FUNCTIONS,
                            severity=SmellSeverity.HIGH,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' has cyclomatic complexity of {cc} "
                                f"(threshold: > {thresholds.cyclomatic_complexity}), exceeding safe reasoning budget."
                            ),
                            threshold=f"> {thresholds.cyclomatic_complexity}",
                            confidence=0.90,
                            suggested_refactoring=(
                                "Decompose branching into polymorphic dispatch, table lookups, or split "
                                "into smaller composable pure functions."
                            ),
                        )
                    )

                # 3. Deep_Nesting (WHEN nesting_depth > 4)
                nesting = self._calculate_nesting_depth(fn.body)
                if nesting > thresholds.nesting_depth:
                    detections.append(
                        SmellDetection(
                            smell_id="Deep_Nesting",
                            category=SmellCategory.FUNCTIONS,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' reaches nesting depth of {nesting} "
                                f"(threshold: > {thresholds.nesting_depth}) in nested let/match/if structures."
                            ),
                            threshold=f"> {thresholds.nesting_depth}",
                            confidence=0.85,
                            suggested_refactoring=(
                                "Flatten control flow using guard clauses, early pattern returns, or "
                                "Railway Monadic error binding (let*)."
                            ),
                        )
                    )

                # 4. Too_Many_Arguments (WHEN function_parameters > 5)
                param_count = len(fn.params)
                if param_count > thresholds.function_parameters:
                    param_names = ", ".join(p.name if hasattr(p, "name") else str(p) for p in fn.params)
                    detections.append(
                        SmellDetection(
                            smell_id="Too_Many_Arguments",
                            category=SmellCategory.FUNCTIONS,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=start_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' accepts {param_count} parameters ({param_names}) "
                                f"(threshold: > {thresholds.function_parameters})."
                            ),
                            threshold=f"> {thresholds.function_parameters} parameters",
                            confidence=0.95,
                            suggested_refactoring=(
                                "Bundle related parameters into an explicit OCaml record (type config = { ... }) "
                                "or pass a context object."
                            ),
                        )
                    )

                # 5. Large_Match (WHEN match_branches > 10)
                max_match_branches = self._find_max_match_branches(fn.body)
                if max_match_branches > thresholds.match_branches:
                    detections.append(
                        SmellDetection(
                            smell_id="Large_Match",
                            category=SmellCategory.FUNCTIONS,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Match construct in '{fn_name}' contains {max_match_branches} branches "
                                f"(threshold: > {thresholds.match_branches})."
                            ),
                            threshold=f"> {thresholds.match_branches} branches",
                            confidence=0.90,
                            suggested_refactoring=(
                                "Refactor large pattern match into sub-variant handlers, map dispatch, "
                                "or hierarchical pattern matching."
                            ),
                        )
                    )

                # 6. Long_Lambda (WHEN lambda_lines > 15)
                long_lambda_lines = self._find_long_lambdas(fn.body)
                if long_lambda_lines > thresholds.lambda_lines:
                    detections.append(
                        SmellDetection(
                            smell_id="Long_Lambda",
                            category=SmellCategory.FUNCTIONS,
                            severity=SmellSeverity.LOW,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Anonymous lambda (fun ... ->) inside '{fn_name}' spans {long_lambda_lines} lines "
                                f"(threshold: > {thresholds.lambda_lines})."
                            ),
                            threshold=f"> {thresholds.lambda_lines} lines",
                            confidence=0.85,
                            suggested_refactoring=(
                                "Promote the anonymous lambda to a named local function (let helper ... in) "
                                "for improved clarity and stack traces."
                            ),
                        )
                    )

                # 7. Multiple_Responsibilities (WHEN function_responsibility_count > 1)
                responsibilities = self._detect_responsibilities(fn.body)
                if len(responsibilities) > 1:
                    resp_str = " + ".join(responsibilities)
                    detections.append(
                        SmellDetection(
                            smell_id="Multiple_Responsibilities",
                            category=SmellCategory.FUNCTIONS,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' mixes {len(responsibilities)} disparate concerns: {resp_str}."
                            ),
                            threshold="> 1 responsibility",
                            confidence=0.80,
                            suggested_refactoring=(
                                "Separate domain business calculations from I/O, state mutation, and format serialization."
                            ),
                        )
                    )

                # 8. Excessive_Return_Logic (WHEN conditional_return_paths > 6)
                return_paths = self._count_conditional_return_paths(fn.body)
                if return_paths > thresholds.conditional_return_paths:
                    detections.append(
                        SmellDetection(
                            smell_id="Excessive_Return_Logic",
                            category=SmellCategory.FUNCTIONS,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' has {return_paths} distinct conditional exit paths "
                                f"(threshold: > {thresholds.conditional_return_paths})."
                            ),
                            threshold=f"> {thresholds.conditional_return_paths} paths",
                            confidence=0.85,
                            suggested_refactoring=(
                                "Consolidate exit points using monadic error composition (Result.bind) "
                                "or centralized error state mapping."
                            ),
                        )
                    )

        return detections

    def _calculate_cyclomatic_complexity(self, body: str) -> int:
        if not body:
            return 1
        score = 1
        score += len(re.findall(r"\bif\b", body))
        score += len(re.findall(r"\bwhile\b", body))
        score += len(re.findall(r"\bfor\b", body))
        score += len(re.findall(r"&&|\|\|", body))
        score += len(re.findall(r"\bwith\s+\||\bmatch\s+.*?\s+with\b", body))
        score += len(re.findall(r"\n\s*\|\s+[A-Za-z0-9_`']+", body))
        return score

    def _calculate_nesting_depth(self, body: str) -> int:
        lines = body.splitlines()
        max_depth = 0
        current_depth = 0
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("let ") and " in" not in stripped:
                current_depth += 1
            if "match " in stripped and "with" in stripped:
                current_depth += 1
            if stripped.startswith("if ") and "then" in stripped:
                current_depth += 1
            if stripped.startswith("begin"):
                current_depth += 1
            if stripped.endswith("end") or stripped == "done" or stripped.startswith("in "):
                current_depth = max(0, current_depth - 1)
            max_depth = max(max_depth, current_depth)
        return max_depth

    def _find_max_match_branches(self, body: str) -> int:
        # Matches blocks like: match ... with ... | ... ->
        match_blocks = re.findall(r"match\s+.*?\s+with\s+(.*?)(?=\blet\b|\bmatch\b|\Z)", body, re.DOTALL)
        max_branches = 0
        for block in match_blocks:
            branches = len(re.findall(r"(?:^|\n)\s*\|\s+[^->]+->", block))
            max_branches = max(max_branches, branches)
        # Also check function | case1 -> | case2 ->
        func_matches = re.findall(r"\bfunction\b\s+(.*?)(?=\blet\b|\Z)", body, re.DOTALL)
        for block in func_matches:
            branches = len(re.findall(r"(?:^|\n)\s*\|\s+[^->]+->", block))
            max_branches = max(max_branches, branches)
        return max_branches

    def _find_long_lambdas(self, body: str) -> int:
        lambda_matches = re.findall(r"\bfun\s+[^->]+->(.*?)(?=\blet\b|\bval\b|\Z)", body, re.DOTALL)
        max_lines = 0
        for lam in lambda_matches:
            lines = len(lam.strip().splitlines())
            max_lines = max(max_lines, lines)
        return max_lines

    def _detect_responsibilities(self, body: str) -> list[str]:
        responsibilities = []
        has_io = bool(re.search(r"\b(print_endline|prerr_endline|output_string|open_out|flush|Printf\.printf|Unix\.)\b", body))
        has_parse = bool(re.search(r"\b(Yojson|Lexing|Parsing|parse|json|yaml)\b", body, re.IGNORECASE))
        has_state = bool(re.search(r"(:=|\.contents|\bref\b)", body))
        has_calc = bool(re.search(r"(\+|\-|\*|\/|\bList\.fold|\bArray\.iter)", body))

        if has_io:
            responsibilities.append("Direct I/O")
        if has_parse:
            responsibilities.append("Parsing / Serialization")
        if has_state:
            responsibilities.append("State Mutation")
        if has_calc:
            responsibilities.append("Pure Data Transformation")
        return responsibilities

    def _count_conditional_return_paths(self, body: str) -> int:
        paths = 1
        paths += len(re.findall(r"\bthen\b", body))
        paths += len(re.findall(r"\belse\b", body))
        paths += len(re.findall(r"(?:^|\n)\s*\|\s+[^->]+->", body))
        return paths
