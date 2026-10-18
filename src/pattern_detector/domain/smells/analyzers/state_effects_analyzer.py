"""Clean code smell analyzer for OCaml STATE_AND_EFFECTS."""

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

#: Regex matching OCaml I/O operations
_IO_OPERATIONS_RE = re.compile(
    r"\b(print_endline|print_string|prerr_endline|output_string|output_bytes|"
    r"open_out|open_in|close_out|close_in|flush|Printf\.printf|Printf\.eprintf|"
    r"Unix\.connect|Unix\.bind|Unix\.send|Unix\.recv|Unix\.openfile)\b"
)

#: Pure-sounding prefixes
_PURE_NAME_PREFIXES = ("get_", "calc_", "calculate_", "compute_", "to_", "is_", "has_", "find_", "format_")


class StateAndEffectsSmellAnalyzer(BaseSmellAnalyzer):
    """Detects unnecessary mutation, excessive references, hidden side effects, mixed responsibilities, and global state."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.STATE_AND_EFFECTS

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

            # Top-level mutable references (Global_State & Excessive_References)
            top_level_refs = [
                f.name for f in top_funcs if not f.params and f.body.startswith("ref ")
            ]
            if len(top_level_refs) >= thresholds.excessive_references_threshold:
                detections.append(
                    SmellDetection(
                        smell_id="Excessive_References",
                        category=SmellCategory.STATE_AND_EFFECTS,
                        severity=SmellSeverity.MEDIUM,
                        file=file_path,
                        start_line=1,
                        end_line=min(50, len(raw_source.splitlines())),
                        symbol=mod_name,
                        evidence=(
                            f"Module '{mod_name}' declares {len(top_level_refs)} top-level mutable references "
                            f"({', '.join(top_level_refs[:4])}...) violating functional immutability."
                        ),
                        threshold=f">= {thresholds.excessive_references_threshold} module-level references",
                        confidence=0.90,
                        suggested_refactoring="Encapsulate mutable state in explicit record instances or use algebraic effects.",
                    )
                )

            for ref_name in top_level_refs:
                detections.append(
                    SmellDetection(
                        smell_id="Global_State",
                        category=SmellCategory.STATE_AND_EFFECTS,
                        severity=SmellSeverity.HIGH,
                        file=file_path,
                        start_line=1,
                        end_line=1,
                        symbol=f"{mod_name}.{ref_name}",
                        evidence=(
                            f"Top-level mutable reference '{ref_name}' in '{mod_name}' introduces "
                            f"uncontrolled global state prone to race conditions."
                        ),
                        threshold="top-level mutable ref declared",
                        confidence=0.95,
                        suggested_refactoring="Pass state explicitly through function parameters or use a State monad / effect handler.",
                    )
                )

            # Inspect functions for Unnecessary_Mutation, Hidden_Side_Effect, Mixed_Responsibilities
            for fn in top_funcs:
                fn_name = fn.name
                start_line = fn.start_line
                end_line = fn.end_line
                body = fn.body

                # 1. Hidden_Side_Effect (WHEN function_name_suggests_pure_computation_but_performs_io)
                is_pure_name = fn_name.startswith(_PURE_NAME_PREFIXES)
                io_matches = _IO_OPERATIONS_RE.findall(body)
                if is_pure_name and io_matches:
                    first_io = io_matches[0]
                    detections.append(
                        SmellDetection(
                            smell_id="Hidden_Side_Effect",
                            category=SmellCategory.STATE_AND_EFFECTS,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' has pure query name prefix but invokes "
                                f"I/O side effect '{first_io}'."
                            ),
                            threshold="pure naming prefix + direct I/O invocation",
                            confidence=0.90,
                            suggested_refactoring=(
                                "Separate pure query computation from I/O logging/writing, or rename function "
                                "to convey side effects."
                            ),
                        )
                    )

                # 2. Mixed_Responsibilities (WHEN function_combines_business_logic_and_io)
                has_business_calc = bool(re.search(r"(\+|\-|\*|\/|\bList\.map|\bList\.filter|\bList\.fold)\b", body))
                if io_matches and has_business_calc and len(body.splitlines()) > 10:
                    detections.append(
                        SmellDetection(
                            smell_id="Mixed_Responsibilities",
                            category=SmellCategory.STATE_AND_EFFECTS,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' interweaves business transformation logic with direct I/O ({io_matches[0]})."
                            ),
                            threshold="business logic + I/O mixed in function body",
                            confidence=0.85,
                            suggested_refactoring=(
                                "Extract pure transformation into a standalone function and let the outer function "
                                "handle I/O orchestration."
                            ),
                        )
                    )

                # 3. Unnecessary_Mutation (WHEN ref_or_mutable_used_without_required_state_changes)
                local_refs = re.findall(r"\blet\s+([a-zA-Z0-9_]+)\s*=\s*ref\s+", body)
                for local_ref in local_refs:
                    assignments = len(re.findall(rf"\b{re.escape(local_ref)}\s*:=", body))
                    if assignments <= 1:
                        detections.append(
                            SmellDetection(
                                smell_id="Unnecessary_Mutation",
                                category=SmellCategory.STATE_AND_EFFECTS,
                                severity=SmellSeverity.MEDIUM,
                                file=file_path,
                                start_line=start_line,
                                end_line=end_line,
                                symbol=f"{mod_name}.{fn_name}.{local_ref}",
                                evidence=(
                                    f"Mutable reference '{local_ref}' in '{fn_name}' is reassigned {assignments} time(s), "
                                    f"and can be written purely."
                                ),
                                threshold="ref reassigned <= 1 times",
                                confidence=0.85,
                                suggested_refactoring=(
                                    "Replace mutable ref with a tail-recursive function accumulator or List.fold_left."
                                ),
                            )
                        )

        return detections
