"""Clean code smell analyzer for OCaml TESTABILITY."""

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

_NON_DETERMINISTIC_RE = re.compile(
    r"\b(Unix\.gettimeofday|Unix\.time|Random\.int|Random\.float|Random\.bool|"
    r"Sys\.argv|Sys\.time|Sys\.getenv)\b"
)


class TestabilitySmellAnalyzer(BaseSmellAnalyzer):
    """Detects untestable functions, missing boundary/property tests, and test duplication."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.TESTABILITY

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
            is_test_file = "test" in file_path.lower() or "bench" in file_path.lower()

            if not is_test_file:
                for fn_name, fn in mod.functions.items():
                    start_line = fn.location.line if fn.location else 1
                    end_line = start_line + max(1, len(fn.body.splitlines()))

                    # 1. Untestable_Function (WHEN function_depends_on_global_state_or_direct_io)
                    non_det = _NON_DETERMINISTIC_RE.findall(fn.body)
                    if non_det:
                        first_nd = non_det[0]
                        detections.append(
                            SmellDetection(
                                smell_id="Untestable_Function",
                                category=SmellCategory.TESTABILITY,
                                severity=SmellSeverity.MEDIUM,
                                file=file_path,
                                start_line=start_line,
                                end_line=end_line,
                                symbol=f"{mod_name}.{fn_name}",
                                evidence=(
                                    f"Function '{fn_name}' directly accesses non-deterministic system resource '{first_nd}', "
                                    f"hindering deterministic unit testing."
                                ),
                                threshold="direct non-deterministic system call",
                                confidence=0.90,
                                suggested_refactoring=(
                                    f"Inject '{first_nd}' as a parameter function (e.g. ~now:(unit -> float)) "
                                    f"or via an algebraic effect handler."
                                ),
                            )
                        )

                # 2. Missing_Property_Tests (WHEN domain_invariant_has_no_property_based_test)
                # Check for symmetric encoder/decoder pairs without QCheck in repo
                fn_names = set(mod.functions.keys())
                has_to_from_pair = any(
                    (f"to_{name}" in fn_names and f"of_{name}" in fn_names) or
                    (f"encode_{name}" in fn_names and f"decode_{name}" in fn_names)
                    for name in [n[3:] for n in fn_names if n.startswith("to_")]
                )
                if has_to_from_pair:
                    # Check if tests exist in code model referencing QCheck / Crowbar
                    all_sources = " ".join(sources.values())
                    if "QCheck" not in all_sources and "Crowbar" not in all_sources:
                        detections.append(
                            SmellDetection(
                                smell_id="Missing_Property_Tests",
                                category=SmellCategory.TESTABILITY,
                                severity=SmellSeverity.LOW,
                                file=file_path,
                                start_line=1,
                                end_line=1,
                                symbol=mod_name,
                                evidence=(
                                    f"Module '{mod_name}' defines roundtrip serialize/deserialize operations "
                                    f"without property-based testing (QCheck / Crowbar)."
                                ),
                                threshold="roundtrip operations without property test",
                                confidence=0.75,
                                suggested_refactoring="Add QCheck property test verifying: decode(encode(x)) == Ok x.",
                            )
                        )

        return detections
