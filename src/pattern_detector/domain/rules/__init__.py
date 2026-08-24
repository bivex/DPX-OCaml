"""Rule catalog registration for OCaml Pattern Detector."""

from __future__ import annotations

from pattern_detector.domain.rules.abstract_data_type_interface_rule import AbstractDataTypeInterfaceRule
from pattern_detector.domain.rules.actor_mailbox_process_rule import ActorMailboxProcessRule
from pattern_detector.domain.rules.async_lwt_promises_rule import AsyncLwtPromisesRule
from pattern_detector.domain.rules.base import BasePatternRule, PatternRule
from pattern_detector.domain.rules.circular_module_dependency_rule import CircularModuleDependencyRule
from pattern_detector.domain.rules.closure_currying_strategy_rule import ClosureCurryingStrategyRule
from pattern_detector.domain.rules.cps_continuation_passing_rule import CpsContinuationPassingRule
from pattern_detector.domain.rules.cyclomatic_complexity_kiss_rule import CyclomaticComplexityKissRule
from pattern_detector.domain.rules.defensive_catch_all_exn_rule import DefensiveCatchAllExnRule
from pattern_detector.domain.rules.domains_parallelism_rule import DomainsParallelismRule
from pattern_detector.domain.rules.duplicate_code_dry_rule import DuplicateCodeDryRule
from pattern_detector.domain.rules.effect_handlers_rule import EffectHandlersRule
from pattern_detector.domain.rules.first_class_module_rule import FirstClassModuleRule
from pattern_detector.domain.rules.functor_parametric_module_rule import FunctorParametricModuleRule
from pattern_detector.domain.rules.gadts_expression_eval_rule import GadtsExpressionEvalRule
from pattern_detector.domain.rules.god_module_srp_rule import GodModuleSrpRule
from pattern_detector.domain.rules.lazy_memoization_rule import LazyMemoizationRule
from pattern_detector.domain.rules.module_inclusion_extender_rule import ModuleInclusionExtenderRule
from pattern_detector.domain.rules.mutable_ref_overuse_rule import MutableRefOveruseRule
from pattern_detector.domain.rules.physical_equality_smell_rule import PhysicalEqualitySmellRule
from pattern_detector.domain.rules.pipeline_operator_rule import PipelineOperatorRule
from pattern_detector.domain.rules.polymorphic_variants_rule import PolymorphicVariantsRule
from pattern_detector.domain.rules.railway_monadic_bind_rule import RailwayMonadicBindRule
from pattern_detector.domain.rules.record_function_vtable_rule import RecordFunctionVTableRule
from pattern_detector.domain.rules.recursive_modules_rule import RecursiveModulesRule
from pattern_detector.domain.rules.unchecked_exception_raise_rule import UncheckedExceptionRaiseRule

DEFAULT_RULES: list[PatternRule] = [
    # Module System (5)
    FunctorParametricModuleRule(),
    AbstractDataTypeInterfaceRule(),
    FirstClassModuleRule(),
    ModuleInclusionExtenderRule(),
    RecursiveModulesRule(),

    # Functional Idioms & Data Structures (8)
    GadtsExpressionEvalRule(),
    PolymorphicVariantsRule(),
    RailwayMonadicBindRule(),
    PipelineOperatorRule(),
    CpsContinuationPassingRule(),
    ClosureCurryingStrategyRule(),
    LazyMemoizationRule(),
    RecordFunctionVTableRule(),

    # Multicore, Concurrency & Effects (4)
    EffectHandlersRule(),
    DomainsParallelismRule(),
    AsyncLwtPromisesRule(),
    ActorMailboxProcessRule(),

    # Resilience, SOLID & Type Safety (8)
    UncheckedExceptionRaiseRule(),
    DefensiveCatchAllExnRule(),
    MutableRefOveruseRule(),
    PhysicalEqualitySmellRule(),
    GodModuleSrpRule(),
    CyclomaticComplexityKissRule(),
    DuplicateCodeDryRule(),
    CircularModuleDependencyRule(),
]

__all__ = [
    "BasePatternRule",
    "PatternRule",
    "DEFAULT_RULES",
    "FunctorParametricModuleRule",
    "AbstractDataTypeInterfaceRule",
    "FirstClassModuleRule",
    "ModuleInclusionExtenderRule",
    "RecursiveModulesRule",
    "GadtsExpressionEvalRule",
    "PolymorphicVariantsRule",
    "RailwayMonadicBindRule",
    "PipelineOperatorRule",
    "CpsContinuationPassingRule",
    "ClosureCurryingStrategyRule",
    "LazyMemoizationRule",
    "RecordFunctionVTableRule",
    "EffectHandlersRule",
    "DomainsParallelismRule",
    "AsyncLwtPromisesRule",
    "ActorMailboxProcessRule",
    "UncheckedExceptionRaiseRule",
    "DefensiveCatchAllExnRule",
    "MutableRefOveruseRule",
    "PhysicalEqualitySmellRule",
    "GodModuleSrpRule",
    "CyclomaticComplexityKissRule",
    "DuplicateCodeDryRule",
    "CircularModuleDependencyRule",
]
