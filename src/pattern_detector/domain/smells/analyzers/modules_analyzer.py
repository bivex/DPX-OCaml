"""Clean code smell analyzer for OCaml MODULES."""

from __future__ import annotations

import re
from pathlib import Path
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


class ModulesSmellAnalyzer(BaseSmellAnalyzer):
    """Analyzes OCaml modules for size, God Module characteristics, opens, circular dependencies, and interfaces."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.MODULES

    def analyze(
        self,
        code_model: CodeModel,
        sources: dict[str, str],
        thresholds: SmellThresholds,
        component_graph: ComponentGraph | None = None,
        arch_result: ArchitectureScanResult | None = None,
    ) -> list[SmellDetection]:
        detections: list[SmellDetection] = []

        # 1. Module-level checks (Large_Module, Too_Many_Public_Functions, Excessive_Open, Unused_Open, God_Module, Missing_Interface)
        for mod_name, mod in code_model.modules.items():
            file_path = mod.file_path
            raw_source = sources.get(file_path, mod.raw_source)
            clean_source = strip_comments_and_strings(raw_source)
            lines = raw_source.splitlines()
            loc = len(lines)
            exported_fn_count = len(mod.functions)
            type_count = len(mod.types)

            # Large_Module (WHEN module_lines > 500)
            if loc > thresholds.module_lines:
                detections.append(
                    SmellDetection(
                        smell_id="Large_Module",
                        category=SmellCategory.MODULES,
                        severity=SmellSeverity.MEDIUM,
                        file=file_path,
                        start_line=1,
                        end_line=loc,
                        symbol=mod_name,
                        evidence=f"Module '{mod_name}' spans {loc} lines of code (threshold: > {thresholds.module_lines}).",
                        threshold=f"> {thresholds.module_lines} lines",
                        confidence=0.95,
                        suggested_refactoring="Decompose module into cohesive nested submodules or separate compilation units.",
                    )
                )

            # Too_Many_Public_Functions (WHEN exported_value_count > 30)
            if exported_fn_count > thresholds.exported_value_count:
                detections.append(
                    SmellDetection(
                        smell_id="Too_Many_Public_Functions",
                        category=SmellCategory.MODULES,
                        severity=SmellSeverity.MEDIUM,
                        file=file_path,
                        start_line=1,
                        end_line=loc,
                        symbol=mod_name,
                        evidence=(
                            f"Module '{mod_name}' exports {exported_fn_count} functions/values "
                            f"(threshold: > {thresholds.exported_value_count})."
                        ),
                        threshold=f"> {thresholds.exported_value_count} exported values",
                        confidence=0.90,
                        suggested_refactoring="Narrow exported surface via .mli interface file or group into submodules.",
                    )
                )

            # Excessive_Open (WHEN open_count > 10)
            open_count = len(mod.opens)
            if open_count > thresholds.open_count:
                detections.append(
                    SmellDetection(
                        smell_id="Excessive_Open",
                        category=SmellCategory.MODULES,
                        severity=SmellSeverity.MEDIUM,
                        file=file_path,
                        start_line=1,
                        end_line=min(30, loc),
                        symbol=mod_name,
                        evidence=(
                            f"Module '{mod_name}' contains {open_count} 'open' directives "
                            f"({', '.join(mod.opens[:5])}...) polluting top-level namespace."
                        ),
                        threshold=f"> {thresholds.open_count} opens",
                        confidence=0.90,
                        suggested_refactoring="Use local opens (let open M in ... or M.(...)) or qualified references.",
                    )
                )

            # Unused_Open (WHEN opened_module_has_no_referenced_identifiers)
            for opened_mod in mod.opens:
                # Check if opened module name or its typical symbols are referenced anywhere in clean source
                # e.g., if open Foo, check if Foo. or any unqualified identifier could come from Foo
                qual_ref = f"{opened_mod}."
                if qual_ref not in clean_source and not self._is_standard_open(opened_mod):
                    # Check if any function call matches tokens
                    call_targets = [call_m for fn in mod.functions.values() for call_m, _ in fn.calls]
                    if opened_mod not in call_targets:
                        # Find open line
                        m_open = re.search(rf"\bopen\s+{re.escape(opened_mod)}\b", clean_source)
                        line_no = clean_source[:m_open.start()].count("\n") + 1 if m_open else 1
                        detections.append(
                            SmellDetection(
                                smell_id="Unused_Open",
                                category=SmellCategory.MODULES,
                                severity=SmellSeverity.LOW,
                                file=file_path,
                                start_line=line_no,
                                end_line=line_no,
                                symbol=f"{mod_name}.open_{opened_mod}",
                                evidence=f"Opened module '{opened_mod}' has no apparent references in '{mod_name}'.",
                                threshold="opened module has no referenced identifiers",
                                confidence=0.75,
                                suggested_refactoring=f"Remove unnecessary 'open {opened_mod}' to keep scope clean.",
                            )
                        )

            # God_Module (WHEN module_has_multiple_unrelated_responsibilities, SEVERITY = HIGH)
            if (
                loc >= thresholds.god_module_loc
                and type_count >= thresholds.god_module_types
                and exported_fn_count >= thresholds.god_module_functions
            ):
                detections.append(
                    SmellDetection(
                        smell_id="God_Module",
                        category=SmellCategory.MODULES,
                        severity=SmellSeverity.HIGH,
                        file=file_path,
                        start_line=1,
                        end_line=loc,
                        symbol=mod_name,
                        evidence=(
                            f"Module '{mod_name}' centralizes excessive responsibilities: "
                            f"{loc} LOC, {type_count} type definitions, and {exported_fn_count} functions."
                        ),
                        threshold=f">= {thresholds.god_module_loc} LOC, >= {thresholds.god_module_types} types, >= {thresholds.god_module_functions} functions",
                        confidence=0.95,
                        suggested_refactoring="Split God Module along domain boundaries into cohesive ports, entities, and services.",
                    )
                )

            # Missing_Interface (WHEN module_has_no_mli AND public_api_is_large)
            mli_path = Path(file_path).with_suffix(".mli")
            has_mli = mli_path.exists() or str(mli_path) in sources
            if not has_mli and exported_fn_count > thresholds.missing_interface_function_count:
                detections.append(
                    SmellDetection(
                        smell_id="Missing_Interface",
                        category=SmellCategory.MODULES,
                        severity=SmellSeverity.MEDIUM,
                        file=file_path,
                        start_line=1,
                        end_line=loc,
                        symbol=mod_name,
                        evidence=(
                            f"Module '{mod_name}' exports {exported_fn_count} functions without a .mli interface file."
                        ),
                        threshold=f"no .mli and > {thresholds.missing_interface_function_count} exported functions",
                        confidence=0.90,
                        suggested_refactoring="Create an explicit .mli interface file to encapsulate internal helper functions.",
                    )
                )

            # Leaky_Abstraction (WHEN implementation_details_exposed_in_mli)
            if has_mli:
                mli_content = sources.get(str(mli_path), "")
                if mli_content and "type t = {" in mli_content:
                    detections.append(
                        SmellDetection(
                            smell_id="Leaky_Abstraction",
                            category=SmellCategory.MODULES,
                            severity=SmellSeverity.MEDIUM,
                            file=str(mli_path),
                            start_line=1,
                            end_line=1,
                            symbol=f"{mod_name}.t",
                            evidence=f"Interface '{mod_name}.mli' exposes concrete record representation of 'type t'.",
                            threshold="concrete record fields exposed in .mli for type t",
                            confidence=0.85,
                            suggested_refactoring="Make 'type t' abstract in .mli and export constructor/accessor functions.",
                        )
                    )

        # 2. Circular_Dependency (WHEN module_dependency_graph_contains_cycle, SEVERITY = CRITICAL)
        cycles = code_model.find_circular_dependencies()
        for cycle in cycles:
            cycle_str = " -> ".join(cycle + [cycle[0]])
            first_mod = code_model.find_module(cycle[0])
            f_path = first_mod.file_path if first_mod else "dune"
            detections.append(
                SmellDetection(
                    smell_id="Circular_Dependency",
                    category=SmellCategory.MODULES,
                    severity=SmellSeverity.CRITICAL,
                    file=f_path,
                    start_line=1,
                    end_line=1,
                    symbol=" <-> ".join(cycle),
                    evidence=f"Cyclic module dependency detected across compilation units: {cycle_str}.",
                    threshold="module dependency cycle > 0",
                    confidence=0.99,
                    suggested_refactoring="Break circular dependency by extracting shared types to a common module or using functors.",
                )
            )

        return detections

    def _is_standard_open(self, mod_name: str) -> bool:
        return mod_name in {"Base", "Core", "StdLabels", "Result", "Option", "List", "Array"}
