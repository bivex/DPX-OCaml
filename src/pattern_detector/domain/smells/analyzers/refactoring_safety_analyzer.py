"""Clean code smell analyzer for OCaml REFACTORING_SAFETY."""

from __future__ import annotations

import re
from pathlib import Path
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


class RefactoringSafetySmellAnalyzer(BaseSmellAnalyzer):
    """Detects public API breakage, unresolved symbols, and behavior change hazards in OCaml code."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.REFACTORING_SAFETY

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

            # 1. Public_API_Breakage (WHEN refactoring_changes_exported_signature, SEVERITY = CRITICAL)
            # Compare .ml functions against .mli val declarations if .mli exists
            mli_path = Path(file_path).with_suffix(".mli")
            if mli_path.exists() or str(mli_path) in sources:
                mli_content = sources.get(str(mli_path), "")
                if mli_content:
                    # Find all val declarations in mli: val name : ...
                    val_decls = re.findall(r"\bval\s+([a-zA-Z0-9_!]+)\s*:\s*([^;\n]+)", mli_content)
                    for val_name, val_type in val_decls:
                        if val_name not in mod.functions:
                            detections.append(
                                SmellDetection(
                                    smell_id="Public_API_Breakage",
                                    category=SmellCategory.REFACTORING_SAFETY,
                                    severity=SmellSeverity.CRITICAL,
                                    file=str(mli_path),
                                    start_line=1,
                                    end_line=1,
                                    symbol=f"{mod_name}.{val_name}",
                                    evidence=(
                                        f"Public API signature breakage: '{mod_name}.mli' exports 'val {val_name}', "
                                        f"but implementation '{mod_name}.ml' is missing this binding."
                                    ),
                                    threshold="exported val in .mli missing in .ml",
                                    confidence=0.99,
                                    suggested_refactoring="Implement missing function in .ml or deprecate/remove from .mli with version bump.",
                                )
                            )

            # 2. Unresolved_Symbol (WHEN identifier_reference_cannot_be_resolved)
            for fn_name, fn in mod.functions.items():
                start_line = fn.location.line if fn.location else 1
                for call_mod, call_sym in fn.calls:
                    # If call_mod is an unknown module not in standard library and not in project
                    if (
                        call_mod
                        and call_mod not in code_model.modules
                        and call_mod not in mod.submodules
                        and call_mod not in mod.opens
                        and call_mod not in self._stdlib_modules()
                    ):
                        detections.append(
                            SmellDetection(
                                smell_id="Unresolved_Symbol",
                                category=SmellCategory.REFACTORING_SAFETY,
                                severity=SmellSeverity.HIGH,
                                file=file_path,
                                start_line=start_line,
                                end_line=start_line,
                                symbol=f"{call_mod}.{call_sym}",
                                evidence=(
                                    f"Unresolved symbol reference '{call_mod}.{call_sym}' in '{fn_name}': "
                                    f"module '{call_mod}' is not found in Dune project libraries or standard modules."
                                ),
                                threshold="symbol cannot be resolved in project context",
                                confidence=0.85,
                                suggested_refactoring=f"Add missing library to dune (libraries ...) or verify spelling of '{call_mod}'.",
                            )
                        )

                # 3. Behavior_Change_Risk (WHEN refactoring_changes_control_flow_or_effect_order)
                # Detect sequencing of multiple side-effecting statements (e.g. print_endline ... ; do_mut ...)
                effects = len(re.findall(r";\s*(?:print_|output_|Unix\.|[a-zA-Z0-9_]+\s*:=)", fn.body))
                if effects >= 3:
                    detections.append(
                        SmellDetection(
                            smell_id="Behavior_Change_Risk",
                            category=SmellCategory.REFACTORING_SAFETY,
                            severity=SmellSeverity.HIGH,
                            file=file_path,
                            start_line=start_line,
                            end_line=start_line + max(1, len(fn.body.splitlines())),
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' executes {effects} sequential imperative side effects (;), "
                                f"posing high risk of behavior regression if expressions are reordered."
                            ),
                            threshold=">= 3 sequential imperative side effects",
                            confidence=0.80,
                            suggested_refactoring="Enforce order of evaluation using explicit let-bindings instead of semicolons.",
                        )
                    )

        return detections

    def _stdlib_modules(self) -> set[str]:
        return {
            "List", "Array", "String", "Bytes", "Char", "Option", "Result", "Seq",
            "Map", "Set", "Hashtbl", "Queue", "Stack", "Buffer", "Printf", "Format",
            "Scanf", "Sys", "Unix", "Filename", "Marshal", "Int32", "Int64", "Nativeint",
            "Float", "Complex", "Random", "Printexc", "Gc", "Lazy", "Digest",
            "Base", "Core", "Stdlib", "Lwt", "Async", "Effect", "Domain", "Domainslib",
        }
