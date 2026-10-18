"""Clean code smell analyzer for OCaml TYPES."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.rules.base import strip_comments_and_strings
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


class TypesSmellAnalyzer(BaseSmellAnalyzer):
    """Analyzes OCaml types for primitive obsession, boolean parameters, stringly typing, and partial functions."""

    @property
    def category(self) -> SmellCategory:
        return SmellCategory.TYPES

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

            # 1. Inspect Module Types: Large_Variant_Type & Tuple_Overuse
            for type_name, type_model in mod.types.items():
                loc_line = type_model.location.line if type_model.location else 1

                # Large_Variant_Type (WHEN variant_constructor_count > 15)
                constructor_count = len(type_model.variant_constructors)
                if constructor_count > thresholds.variant_constructor_count:
                    detections.append(
                        SmellDetection(
                            smell_id="Large_Variant_Type",
                            category=SmellCategory.TYPES,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=loc_line,
                            end_line=loc_line + constructor_count,
                            symbol=f"{mod_name}.{type_name}",
                            evidence=(
                                f"Variant type '{type_name}' declares {constructor_count} constructors "
                                f"(threshold: > {thresholds.variant_constructor_count})."
                            ),
                            threshold=f"> {thresholds.variant_constructor_count} constructors",
                            confidence=0.95,
                            suggested_refactoring=(
                                "Split large variant into hierarchical sub-variants, compositional polymorphic "
                                "variants ([> `Sub1 ...]), or GADTs."
                            ),
                        )
                    )

            # Find tuple overuse in raw type definitions (e.g. type t = a * b * c * d)
            tuple_matches = re.finditer(
                r"\btype\s+([a-zA-Z0-9_'\s]+?)\s*=\s*([^=\n;]+?\*(?:[^=\n;]+?\*){2,}[^=\n;]+)",
                clean_source,
            )
            for tm in tuple_matches:
                t_name = tm.group(1).split()[-1]
                tuple_expr = tm.group(2).strip()
                elements = tuple_expr.split("*")
                if len(elements) > thresholds.tuple_element_count:
                    line_no = clean_source[:tm.start()].count("\n") + 1
                    detections.append(
                        SmellDetection(
                            smell_id="Tuple_Overuse",
                            category=SmellCategory.TYPES,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=line_no,
                            end_line=line_no,
                            symbol=f"{mod_name}.{t_name}",
                            evidence=(
                                f"Type '{t_name}' defines an anonymous tuple of {len(elements)} elements "
                                f"({tuple_expr[:40]}...) without named fields."
                            ),
                            threshold=f"> {thresholds.tuple_element_count} tuple elements",
                            confidence=0.90,
                            suggested_refactoring=(
                                "Replace anonymous tuple with an explicit OCaml record (type t = { ... }) "
                                "with self-documenting field names."
                            ),
                        )
                    )

            # 2. Inspect Functions: Primitive_Obsession, Boolean_Parameter, Stringly_Typed, Weak_Error_Model, Partial_Function
            top_funcs = extract_top_level_functions(raw_source)
            for fn in top_funcs:
                fn_name = fn.name
                start_line = fn.start_line
                end_line = fn.end_line
                body = fn.body

                # Boolean_Parameter (WHEN function_has_boolean_parameter, SEVERITY = LOW)
                for p_str in fn.params:
                    # Check if parameter has : bool or is named flag, verbose, dry_run, etc.
                    is_bool_name = bool(re.search(r"\b(is_|has_|use_|enable_|flag|dry_run|verbose|recursive|force)\b", p_str, re.IGNORECASE))
                    has_bool_type = "bool" in p_str.lower()
                    if is_bool_name or has_bool_type:
                        detections.append(
                            SmellDetection(
                                smell_id="Boolean_Parameter",
                                category=SmellCategory.TYPES,
                                severity=SmellSeverity.LOW,
                                file=file_path,
                                start_line=start_line,
                                end_line=start_line,
                                symbol=f"{mod_name}.{fn_name}({p_str})",
                                evidence=(
                                    f"Function '{fn_name}' accepts boolean flag parameter '{p_str}', "
                                    f"which obscures call site intent."
                                ),
                                threshold="boolean parameter present",
                                confidence=0.85,
                                suggested_refactoring=(
                                    f"Replace boolean '{p_str}' with an expressive two-state variant "
                                    f"(e.g. type {p_str}_mode = Enable_{p_str} | Disable_{p_str})."
                                ),
                            )
                        )
                        break

                # Primitive_Obsession (WHEN same_primitive_type_repeated_for_domain_concepts)
                if len(fn.params) >= thresholds.primitive_obsession_param_count:
                    str_params = [p for p in fn.params if "str" in p or "name" in p or "path" in p or "id" in p]
                    if len(str_params) >= thresholds.primitive_obsession_param_count:
                        detections.append(
                            SmellDetection(
                                smell_id="Primitive_Obsession",
                                category=SmellCategory.TYPES,
                                severity=SmellSeverity.MEDIUM,
                                file=file_path,
                                start_line=start_line,
                                end_line=start_line,
                                symbol=f"{mod_name}.{fn_name}",
                                evidence=(
                                    f"Function '{fn_name}' accepts {len(str_params)} raw primitive string/id parameters "
                                    f"({', '.join(str_params)}) without domain newtypes."
                                ),
                                threshold=f">= {thresholds.primitive_obsession_param_count} primitive domain parameters",
                                confidence=0.85,
                                suggested_refactoring=(
                                    "Wrap raw primitives in private domain types or unboxed abstract types "
                                    "(e.g. type user_id = private string) to prevent parameter transposition bugs."
                                ),
                            )
                        )

                # Stringly_Typed (WHEN string_used_for_domain_state_or_identifier)
                string_matches = re.findall(r'\|\s*"([a-z_]{3,25})"\s*->', body)
                if len(string_matches) >= 3:
                    detections.append(
                        SmellDetection(
                            smell_id="Stringly_Typed",
                            category=SmellCategory.TYPES,
                            severity=SmellSeverity.MEDIUM,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' matches on {len(string_matches)} raw string literals "
                                f"({', '.join(f'\"{s}\"' for s in string_matches[:4])}) for control state."
                            ),
                            threshold=">= 3 string literal match branches",
                            confidence=0.90,
                            suggested_refactoring=(
                                "Model domain states as a closed OCaml variant or polymorphic variant type "
                                "for compile-time exhaustiveness checking."
                            ),
                        )
                    )

                # Weak_Error_Model (WHEN failwith_or_invalid_arg_used_for_expected_errors)
                weak_error_calls = re.findall(r"\b(failwith|invalid_arg)\b", body)
                if weak_error_calls:
                    detections.append(
                        SmellDetection(
                            smell_id="Weak_Error_Model",
                            category=SmellCategory.TYPES,
                            severity=SmellSeverity.HIGH,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' throws unhandled runtime exception via '{weak_error_calls[0]}' "
                                f"instead of returning a typed Result or Option."
                            ),
                            threshold="failwith or invalid_arg invocation",
                            confidence=0.95,
                            suggested_refactoring=(
                                "Return ('a, error) result or 'a option to enforce explicit error handling "
                                "at compile time."
                            ),
                        )
                    )

                # Partial_Function (WHEN List.hd_or_List.tl_or_Option.get_used_without_proof)
                partial_calls = re.findall(r"\b(List\.hd|List\.tl|Option\.get|List\.find)\b", body)
                if partial_calls:
                    first_call = partial_calls[0]
                    detections.append(
                        SmellDetection(
                            smell_id="Partial_Function",
                            category=SmellCategory.TYPES,
                            severity=SmellSeverity.HIGH,
                            file=file_path,
                            start_line=start_line,
                            end_line=end_line,
                            symbol=f"{mod_name}.{fn_name}",
                            evidence=(
                                f"Function '{fn_name}' calls unsafe partial function '{first_call}', "
                                f"which raises Failure/Not_found exception on unexpected input."
                            ),
                            threshold="partial function invocation",
                            confidence=0.95,
                            suggested_refactoring=(
                                f"Replace '{first_call}' with total pattern matching or safe alternatives "
                                f"(e.g. List.nth_opt, Option.value, Option.bind)."
                            ),
                        )
                    )

        return detections
