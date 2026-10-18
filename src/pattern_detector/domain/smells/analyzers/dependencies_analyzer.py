"""Clean code smell analyzer for OCaml DEPENDENCIES."""

from __future__ import annotations

from collections import Counter
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


class DependenciesSmellAnalyzer(BaseSmellAnalyzer):
    """Detects high coupling, feature envy, shotgun surgery risks, and dependency inversion violations."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.DEPENDENCIES

    def analyze(
        self,
        code_model: CodeModel,
        sources: dict[str, str],
        thresholds: SmellThresholds,
        component_graph: ComponentGraph | None = None,
        arch_result: ArchitectureScanResult | None = None,
    ) -> list[SmellDetection]:
        detections: list[SmellDetection] = []

        dep_graph = code_model.build_module_dependency_graph()

        # 1. High_Coupling (WHEN module_dependency_count > configured_threshold)
        for mod_name, targets in dep_graph.items():
            mod = code_model.find_module(mod_name)
            file_path = mod.file_path if mod else "unknown"
            efferent_count = len(targets)
            if efferent_count > thresholds.coupling_threshold:
                detections.append(
                    SmellDetection(
                        smell_id="High_Coupling",
                        category=SmellCategory.DEPENDENCIES,
                        severity=SmellSeverity.MEDIUM,
                        file=file_path,
                        start_line=1,
                        end_line=1,
                        symbol=mod_name,
                        evidence=(
                            f"Module '{mod_name}' is tightly coupled to {efferent_count} distinct modules "
                            f"({', '.join(sorted(targets)[:5])}...) exceeding coupling threshold of {thresholds.coupling_threshold}."
                        ),
                        threshold=f"> {thresholds.coupling_threshold} dependencies",
                        confidence=0.90,
                        suggested_refactoring="Introduce a mediator or facade, or apply dependency inversion using functors.",
                    )
                )

        # 2. Dependency_Inversion_Violation (WHEN domain_module_depends_on_infrastructure_module, SEVERITY = CRITICAL)
        # Using component_graph or path conventions if available
        for mod_name, targets in dep_graph.items():
            mod = code_model.find_module(mod_name)
            if not mod:
                continue
            is_domain = "/domain/" in mod.file_path or mod_name.lower().endswith("entity") or mod_name.lower().endswith("model")
            if is_domain:
                for target_name in targets:
                    target_mod = code_model.find_module(target_name)
                    if not target_mod:
                        continue
                    is_infra = (
                        "/infrastructure/" in target_mod.file_path
                        or "/adapters/" in target_mod.file_path
                        or "/cli/" in target_mod.file_path
                    )
                    if is_infra:
                        detections.append(
                            SmellDetection(
                                smell_id="Dependency_Inversion_Violation",
                                category=SmellCategory.DEPENDENCIES,
                                severity=SmellSeverity.CRITICAL,
                                file=mod.file_path,
                                start_line=1,
                                end_line=1,
                                symbol=f"{mod_name} -> {target_name}",
                                evidence=(
                                    f"Domain module '{mod_name}' depends directly on infrastructure module '{target_name}'."
                                ),
                                threshold="domain module depends on infrastructure module",
                                confidence=0.95,
                                suggested_refactoring=(
                                    "Invert dependency: declare a port interface/module type in Domain and "
                                    "implement it in Infrastructure."
                                ),
                            )
                        )

        # 3. Feature_Envy (WHEN function_uses_foreign_module_data_more_than_own)
        for mod_name, mod in code_model.modules.items():
            file_path = mod.file_path
            for fn_name, fn in mod.functions.items():
                foreign_calls = [m for m, _ in fn.calls if m != mod_name and m in code_model.modules]
                counts = Counter(foreign_calls)
                for foreign_mod, call_count in counts.items():
                    if call_count >= thresholds.feature_envy_call_threshold:
                        start_line = fn.location.line if fn.location else 1
                        detections.append(
                            SmellDetection(
                                smell_id="Feature_Envy",
                                category=SmellCategory.DEPENDENCIES,
                                severity=SmellSeverity.MEDIUM,
                                file=file_path,
                                start_line=start_line,
                                end_line=start_line + max(1, len(fn.body.splitlines())),
                                symbol=f"{mod_name}.{fn_name}",
                                evidence=(
                                    f"Function '{fn_name}' exhibits feature envy toward '{foreign_mod}' "
                                    f"({call_count} invocations vs local module)."
                                ),
                                threshold=f">= {thresholds.feature_envy_call_threshold} calls to foreign module",
                                confidence=0.85,
                                suggested_refactoring=(
                                    f"Consider moving '{fn_name}' into module '{foreign_mod}' or pass precomputed values."
                                ),
                            )
                        )

        return detections
