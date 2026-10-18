"""Clean code smell analyzer for OCaml ERROR_HANDLING."""

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


class ErrorHandlingSmellAnalyzer(BaseSmellAnalyzer):
    """Detects swallowed exceptions, broad catch-all handlers, and inconsistent error models."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.ERROR_HANDLING

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
            has_result_return = False
            has_exception_raise = False
            top_funcs = extract_top_level_functions(raw_source)

            for fn in top_funcs:
                fn_name = fn.name
                start_line = fn.start_line
                end_line = fn.end_line
                raw_body = fn.body

                if "Ok " in raw_body or "Error " in raw_body or "Result." in raw_body:
                    has_result_return = True
                if "raise " in raw_body or "failwith " in raw_body:
                    has_exception_raise = True

                # 1. Swallowed_Exception (WHEN exception_caught_and_ignored, SEVERITY = HIGH)
                swallowed = re.search(r"\bwith\s+_\s*->\s*(\(\)|None|false|0|\"\"\s*|\[\])", raw_body)
                if swallowed:
                    detections.append(
                        SmellDetection(
                            smell_id="Swallowed_Exception",
                            category=SmellCategory.ERROR_HANDLING,
                            severity=SmellSeverity.HIGH,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' catches all exceptions and silently swallows error "
                                f"by returning default value '{swallowed.group(1)}'."
                            ),
                            threshold="with _ -> default_value",
                            confidence=0.95,
                            suggested_refactoring=(
                                "Propagate error via Result.error or log failure; do not silently swallow unexpected crashes."
                            ),
                        )
                    )

                # 2. Broad_Exception_Handler (WHEN exception_handler_catches_all_exceptions_without_reason)
                # Catch-all: with _ ->
                broad = re.findall(r"\bwith\s+_\s*->", raw_body)
                if broad and not swallowed:
                    detections.append(
                        SmellDetection(
                            smell_id="Broad_Exception_Handler",
                            category=SmellCategory.ERROR_HANDLING,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' uses indiscriminate catch-all exception handler ('with _ ->'), "
                                f"which masks Out_of_memory and asynchronous exceptions."
                            ),
                            threshold="catch-all 'with _ ->' handler",
                            confidence=0.90,
                            suggested_refactoring="Catch specific expected exception types (e.g. 'with Not_found ->' or 'Failure msg ->').",
                        )
                    )

                # 3. Exception_For_Normal_Control_Flow (WHEN exception_used_for_expected_business_branch)
                if re.search(r"\braise\s+Not_found\b", raw_body) and ("find" in fn_name or "lookup" in fn_name or "get" in fn_name):
                    detections.append(
                        SmellDetection(
                            smell_id="Exception_For_Normal_Control_Flow",
                            category=SmellCategory.ERROR_HANDLING,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' raises 'Not_found' exception for ordinary missing item search."
                            ),
                            threshold="raise Not_found in lookup operation",
                            confidence=0.85,
                            suggested_refactoring="Return 'a option (None when not found) rather than raising an exception.",
                        )
                    )

            # 4. Inconsistent_Error_Handling (WHEN similar_operations_use_incompatible_error_models)
            if has_result_return and has_exception_raise:
                detections.append(
                    SmellDetection(
                        smell_id="Inconsistent_Error_Handling",
                        category=SmellCategory.ERROR_HANDLING,
                        severity=SmellSeverity.MEDIUM,
                        file=file_path,
                        start_line=1,
                        end_line=min(30, len(mod.raw_source.splitlines())),
                        symbol=mod_name,
                        evidence=(
                            f"Module '{mod_name}' mixes incompatible error strategies: some functions return "
                            f"Result.t while sibling functions raise runtime exceptions."
                        ),
                        threshold="module mixes Result and unchecked exception raising",
                        confidence=0.85,
                        suggested_refactoring="Harmonize API error strategy across the entire module on Result.t or Option.t.",
                    )
                )

        return detections
