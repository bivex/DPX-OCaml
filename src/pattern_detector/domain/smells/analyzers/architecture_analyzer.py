"""Clean code smell analyzer for OCaml ARCHITECTURE."""

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


class ArchitectureSmellAnalyzer(BaseSmellAnalyzer):
    """Detects architecture layer violations, abstraction leaks, wrong module ownership, orphans, and excessive indirection."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.ARCHITECTURE

    def analyze(
        self,
        code_model: CodeModel,
        sources: dict[str, str],
        thresholds: SmellThresholds,
        component_graph: ComponentGraph | None = None,
        arch_result: ArchitectureScanResult | None = None,
    ) -> list[SmellDetection]:
        detections: list[SmellDetection] = []

        # 1. Layer_Violation (WHEN dependency_direction_breaks_architecture_rules, SEVERITY = CRITICAL)
        if arch_result:
            for issue in arch_result.issues:
                if issue.kind.value == "layer_violation":
                    detections.append(
                        SmellDetection(
                            smell_id="Layer_Violation",
                            category=SmellCategory.ARCHITECTURE,
                            severity=SmellSeverity.CRITICAL,
                            file=issue.subject,
                            start_line=1,
                            end_line=1,
                            symbol=issue.subject,
                            evidence=issue.message,
                            threshold="forbidden hexagonal layer dependency",
                            confidence=0.98,
                            suggested_refactoring="Introduce a Port interface in the inner layer and implement it in the outer adapter.",
                        )
                    )
                elif issue.kind.value == "orphan_module":
                    detections.append(
                        SmellDetection(
                            smell_id="Orphan_Module",
                            category=SmellCategory.ARCHITECTURE,
                            severity=SmellSeverity.LOW,
                            file=issue.subject,
                            start_line=1,
                            end_line=1,
                            symbol=issue.subject,
                            evidence=issue.message,
                            threshold="0 incoming module dependencies",
                            confidence=0.85,
                            suggested_refactoring="Remove unused orphan module or link it into public library stanzas.",
                        )
                    )

        # 2. Wrong_Module_Ownership (WHEN domain_logic_lives_in_cli_or_infrastructure)
        for mod_name, mod in code_model.modules.items():
            is_outer = "/cli/" in mod.file_path or "/adapters/" in mod.file_path or mod_name.lower().endswith("cli")
            if is_outer:
                # Check if it defines business entity types or heavy pure calculation algorithms
                has_domain_types = any(t.is_record or t.is_variant for t in mod.types.values())
                if has_domain_types and len(mod.types) >= 3:
                    detections.append(
                        SmellDetection(
                            smell_id="Wrong_Module_Ownership",
                            category=SmellCategory.ARCHITECTURE,
                            severity=SmellSeverity.MEDIUM,
                            file=mod.file_path,
                            start_line=1,
                            end_line=1,
                            symbol=mod_name,
                            evidence=(
                                f"Module '{mod_name}' in outer layer defines {len(mod.types)} core domain types, "
                                f"violating architectural ownership."
                            ),
                            threshold="domain type declarations in CLI/adapter",
                            confidence=0.85,
                            suggested_refactoring="Move domain entities and business types into the core domain layer.",
                        )
                    )

            # 3. Excessive_Indirection (WHEN wrappers_add_no_validation_or_domain_value)
            for fn_name, fn in mod.functions.items():
                body = fn.body.strip()
                # Check for single line trivial pass-through: let f x = Other.f x
                m_wrap = re.match(r"^([A-Z][a-zA-Z0-9_]*)\.([a-z_][a-zA-Z0-9_]*)\s+([a-zA-Z0-9_\s]+)$", body)
                if m_wrap and len(body.splitlines()) == 1:
                    target_mod, target_fn = m_wrap.group(1), m_wrap.group(2)
                    start_line = fn.location.line if fn.location else 1
                    detections.append(
                        SmellDetection(
                            smell_id="Excessive_Indirection",
                            category=SmellCategory.ARCHITECTURE,
                            severity=SmellSeverity.LOW,
                            file=mod.file_path,
                            start_line=start_line,
                            end_line=start_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' is a pure pass-through wrapper for '{target_mod}.{target_fn}' "
                                f"without validation, error handling, or transformation."
                            ),
                            threshold="trivial 1-line wrapper with identical arguments",
                            confidence=0.80,
                            suggested_refactoring=f"Inline wrapper or use direct module aliasing (let {fn_name} = {target_mod}.{target_fn}).",
                        )
                    )

        return detections
