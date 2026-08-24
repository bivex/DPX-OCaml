"""Domain value objects for the OCaml Pattern Detector."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class PatternCategory(str, Enum):
    """Broad classification of OCaml design patterns, module idioms, effect systems, and safety rules."""

    MODULE_SYSTEM = "module_system"
    FUNCTIONAL_IDIOM = "functional_idiom"
    STRUCTURAL = "structural"
    BEHAVIORAL = "behavioral"
    EFFECT_CONCURRENCY = "effect_concurrency"
    RESILIENCE = "resilience"
    PRINCIPLE = "principle"
    TYPE_SAFETY = "type_safety"


class PatternType(str, Enum):
    """Specific OCaml design pattern, functional idiom, effect handler, and architecture smell identifiers."""

    # Module System & Parametric Modules
    FUNCTOR_PARAMETRIC_MODULE = "functor_parametric_module"
    ABSTRACT_DATA_TYPE_INTERFACE = "abstract_data_type_interface"
    FIRST_CLASS_MODULE = "first_class_module"
    MODULE_INCLUSION_EXTENDER = "module_inclusion_extender"
    RECURSIVE_MODULES = "recursive_modules"

    # Functional Idioms & Data Structures
    GADTS_EXPRESSION_EVAL = "gadts_expression_eval"
    POLYMORPHIC_VARIANTS = "polymorphic_variants"
    RAILWAY_MONADIC_BIND = "railway_monadic_bind"
    PIPELINE_OPERATOR = "pipeline_operator"
    CPS_CONTINUATION_PASSING = "cps_continuation_passing"
    CLOSURE_CURRYING_STRATEGY = "closure_currying_strategy"
    LAZY_MEMOIZATION = "lazy_memoization"
    RECORD_FUNCTION_VTABLE = "record_function_vtable"

    # Multicore, Concurrency & Effects (OCaml 5.x)
    EFFECT_HANDLERS = "effect_handlers"
    DOMAINS_PARALLELISM = "domains_parallelism"
    ASYNC_LWT_PROMISES = "async_lwt_promises"
    ACTOR_MAILBOX_PROCESS = "actor_mailbox_process"

    # Resilience, SOLID & Type Safety Audits
    UNCHECKED_EXCEPTION_RAISE = "unchecked_exception_raise"
    DEFENSIVE_CATCH_ALL_EXN = "defensive_catch_all_exn"
    MUTABLE_REF_OVERUSE = "mutable_ref_overuse"
    PHYSICAL_EQUALITY_SMELL = "physical_equality_smell"
    GOD_MODULE_SRP = "god_module_srp"
    CYCLOMATIC_COMPLEXITY_KISS = "cyclomatic_complexity_kiss"
    DUPLICATE_CODE_DRY = "duplicate_code_dry"
    CIRCULAR_MODULE_DEPENDENCY = "circular_module_dependency"


class ConfidenceLevel(str, Enum):
    """Categorical confidence rating for a pattern detection."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    VERY_HIGH = "very_high"

    @classmethod
    def from_score(cls, score: float) -> ConfidenceLevel:
        if score >= 0.85:
            return cls.VERY_HIGH
        if score >= 0.70:
            return cls.HIGH
        if score >= 0.50:
            return cls.MEDIUM
        return cls.LOW


@dataclass(frozen=True)
class SourceLocation:
    """Represents a precise location in an OCaml source or interface file (.ml / .mli)."""

    file_path: str
    line: int = 1
    column: int = 1
    end_line: int | None = None
    end_column: int | None = None

    def __str__(self) -> str:
        return f"{self.file_path}:{self.line}:{self.column}"


@dataclass(frozen=True)
class Evidence:
    """A single piece of heuristic evidence supporting a pattern detection."""

    description: str
    weight: float
    rule_code: str
    location: SourceLocation | None = None

    def __post_init__(self) -> None:
        if not (0.0 <= self.weight <= 1.0):
            raise ValueError(f"Evidence weight must be between 0.0 and 1.0, got {self.weight}")


@dataclass(frozen=True)
class Confidence:
    """Aggregated confidence score computed from multiple pieces of evidence."""

    score: float
    level: ConfidenceLevel = field(init=False)

    def __post_init__(self) -> None:
        clamped = max(0.0, min(1.0, self.score))
        object.__setattr__(self, "score", clamped)
        object.__setattr__(self, "level", ConfidenceLevel.from_score(clamped))

    @classmethod
    def from_evidences(cls, evidences: list[Evidence]) -> Confidence:
        if not evidences:
            return cls(0.0)
        complement_product = 1.0
        for ev in evidences:
            complement_product *= (1.0 - ev.weight)
        return cls(1.0 - complement_product)

    @property
    def percentage_str(self) -> str:
        return f"{int(self.score * 100)}%"
