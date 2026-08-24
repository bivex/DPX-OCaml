"""Pattern metadata, catalog definitions, and architectural descriptions for OCaml."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from pattern_detector.domain.value_objects import PatternCategory, PatternType


@dataclass(frozen=True)
class PatternCatalogEntry:
    """Catalog entry describing an OCaml pattern, module idiom, or rule."""

    pattern_type: PatternType
    category: PatternCategory
    name: str
    description: str
    idiomatic_example: str


PATTERN_CATALOG: Mapping[PatternType, PatternCatalogEntry] = {
    # Module System
    PatternType.FUNCTOR_PARAMETRIC_MODULE: PatternCatalogEntry(
        pattern_type=PatternType.FUNCTOR_PARAMETRIC_MODULE,
        category=PatternCategory.MODULE_SYSTEM,
        name="Functor Parametric Module",
        description="Higher-order module parameterization (`module Make (X : S) = struct ... end`) providing type-safe code reuse and dependency injection.",
        idiomatic_example="module Make (Ord : OrderedType) = struct\n  type t = ...\n  let empty = ...\nend",
    ),
    PatternType.ABSTRACT_DATA_TYPE_INTERFACE: PatternCatalogEntry(
        pattern_type=PatternType.ABSTRACT_DATA_TYPE_INTERFACE,
        category=PatternCategory.MODULE_SYSTEM,
        name="Abstract Data Type (ADT) Signature",
        description="Information hiding via opaque abstract type declarations (`type t`) in `.mli` interfaces with paired constructor/destructor operations.",
        idiomatic_example="(* buffer.mli *)\ntype t\nval create : int -> t\nval push : t -> char -> unit",
    ),
    PatternType.FIRST_CLASS_MODULE: PatternCatalogEntry(
        pattern_type=PatternType.FIRST_CLASS_MODULE,
        category=PatternCategory.MODULE_SYSTEM,
        name="First-Class Module Dynamic Dispatch",
        description="Packaging modules as first-class values (`(module M : S)`) enabling runtime polymorphism, dynamic configuration, and dependency injection.",
        idiomatic_example="let select_backend (module B : Storage_sig) = B.write data",
    ),
    PatternType.MODULE_INCLUSION_EXTENDER: PatternCatalogEntry(
        pattern_type=PatternType.MODULE_INCLUSION_EXTENDER,
        category=PatternCategory.MODULE_SYSTEM,
        name="Module Inclusion & Signature Extension",
        description="Extends, composes, or overrides base module functionality and interfaces via `include Module` (e.g. Jane Street Core/Base extensions).",
        idiomatic_example="module ExtendedList = struct\n  include List\n  let sum l = List.fold_left (+) 0 l\nend",
    ),
    PatternType.RECURSIVE_MODULES: PatternCatalogEntry(
        pattern_type=PatternType.RECURSIVE_MODULES,
        category=PatternCategory.MODULE_SYSTEM,
        name="Mutually Recursive Modules",
        description="Cross-module cyclic data type definitions and mutual dependencies via `module rec A : ... and B : ...`.",
        idiomatic_example="module rec Node : sig type t = Leaf | Node of Tree.t end\nand Tree : sig type t = Node.t list end",
    ),

    # Functional Idioms & Data Structures
    PatternType.GADTS_EXPRESSION_EVAL: PatternCatalogEntry(
        pattern_type=PatternType.GADTS_EXPRESSION_EVAL,
        category=PatternCategory.FUNCTIONAL_IDIOM,
        name="GADT Type-Safe Interpreter / AST",
        description="Generalized Algebraic Data Types (`type _ expr = Int : int -> int expr`) enabling type-safe DSL evaluation and type equalities.",
        idiomatic_example="type _ expr =\n  | Int : int -> int expr\n  | Add : int expr * int expr -> int expr\nlet rec eval : type a. a expr -> a = function ...",
    ),
    PatternType.POLYMORPHIC_VARIANTS: PatternCatalogEntry(
        pattern_type=PatternType.POLYMORPHIC_VARIANTS,
        category=PatternCategory.FUNCTIONAL_IDIOM,
        name="Polymorphic Open Variants",
        description="Extensible open tag polymorphism (`[> `Ok of 'a | `Error of 'b]`) allowing compositional subtyping without nominal declarations.",
        idiomatic_example="type error = [ `NotFound | `PermissionDenied ]\nlet handle_err : [ error | `Timeout ] -> unit = function ...",
    ),
    PatternType.RAILWAY_MONADIC_BIND: PatternCatalogEntry(
        pattern_type=PatternType.RAILWAY_MONADIC_BIND,
        category=PatternCategory.FUNCTIONAL_IDIOM,
        name="Railway Monadic Error Pipeline",
        description="Monadic railway composition via `let*`, `let+`, `>>=`, `Result.bind`, or `Option.bind` chaining operations cleanly without exceptions.",
        idiomatic_example="let ( let* ) = Result.bind in\nlet* user = find_user id in\nlet* token = auth user in\nOk token",
    ),
    PatternType.PIPELINE_OPERATOR: PatternCatalogEntry(
        pattern_type=PatternType.PIPELINE_OPERATOR,
        category=PatternCategory.FUNCTIONAL_IDIOM,
        name="Pipeline Operator Transformation",
        description="Idiomatic OCaml data transformation chaining using `|>` and `@@` composing pure functional operations linearly.",
        idiomatic_example="data |> parse |> validate |> persist",
    ),
    PatternType.CPS_CONTINUATION_PASSING: PatternCatalogEntry(
        pattern_type=PatternType.CPS_CONTINUATION_PASSING,
        category=PatternCategory.FUNCTIONAL_IDIOM,
        name="Continuation-Passing Style (CPS)",
        description="Tail-recursive call transformation passing an explicit continuation callback `k` to ensure stack-safe recursion.",
        idiomatic_example="let rec map_cps l f k = match l with\n  | [] -> k []\n  | x :: xs -> map_cps xs f (fun acc -> k (f x :: acc))",
    ),
    PatternType.CLOSURE_CURRYING_STRATEGY: PatternCatalogEntry(
        pattern_type=PatternType.CLOSURE_CURRYING_STRATEGY,
        category=PatternCategory.BEHAVIORAL,
        name="Curried Function Strategy Injection",
        description="Dynamic strategy configuration through partial application, closures, and higher-order function arguments.",
        idiomatic_example="let make_sorter comparator = List.sort comparator\nlet sort_by_age = make_sorter (fun a b -> compare a.age b.age)",
    ),
    PatternType.LAZY_MEMOIZATION: PatternCatalogEntry(
        pattern_type=PatternType.LAZY_MEMOIZATION,
        category=PatternCategory.STRUCTURAL,
        name="Lazy Evaluation & Memoization",
        description="Deferred on-demand evaluation and automatic result caching via `lazy expr` and `Lazy.force`.",
        idiomatic_example="let memoized_calc = lazy (expensive_computation input)\nlet get_result () = Lazy.force memoized_calc",
    ),
    PatternType.RECORD_FUNCTION_VTABLE: PatternCatalogEntry(
        pattern_type=PatternType.RECORD_FUNCTION_VTABLE,
        category=PatternCategory.STRUCTURAL,
        name="Record VTable (Object-like Dispatch)",
        description="Struct / record containing function fields providing explicit object-like virtual method table dispatch.",
        idiomatic_example="type 'a storage = {\n  read: key -> 'a option;\n  write: key -> 'a -> unit;\n}",
    ),

    # Multicore, Concurrency & Effects (OCaml 5.x)
    PatternType.EFFECT_HANDLERS: PatternCatalogEntry(
        pattern_type=PatternType.EFFECT_HANDLERS,
        category=PatternCategory.EFFECT_CONCURRENCY,
        name="Algebraic Effect Handlers (OCaml 5)",
        description="Direct-style algebraic effect systems (`type _ Effect.t += ...`, `Effect.perform`, `Effect.Deep.try_with`) in OCaml 5+.",
        idiomatic_example="type _ Effect.t += Get : string Effect.t\nlet v = Effect.perform Get\nEffect.Deep.try_with fn () { effc = ... }",
    ),
    PatternType.DOMAINS_PARALLELISM: PatternCatalogEntry(
        pattern_type=PatternType.DOMAINS_PARALLELISM,
        category=PatternCategory.EFFECT_CONCURRENCY,
        name="Domains Multicore Parallelism",
        description="True shared-memory multicore parallelism in OCaml 5 using `Domain.spawn`, `Domain.join`, or `Domainslib.Task`.",
        idiomatic_example="let d = Domain.spawn (fun () -> compute_chunk data) in\nDomain.join d",
    ),
    PatternType.ASYNC_LWT_PROMISES: PatternCatalogEntry(
        pattern_type=PatternType.ASYNC_LWT_PROMISES,
        category=PatternCategory.EFFECT_CONCURRENCY,
        name="Lwt / Async Promise Concurrency",
        description="Cooperative asynchronous concurrency using Lwt or Jane Street Async (`Lwt.bind`, `Lwt_main.run`, `let%bind`).",
        idiomatic_example="let%bind response = Cohttp_lwt_unix.Client.get uri in\nLwt.return response",
    ),
    PatternType.ACTOR_MAILBOX_PROCESS: PatternCatalogEntry(
        pattern_type=PatternType.ACTOR_MAILBOX_PROCESS,
        category=PatternCategory.EFFECT_CONCURRENCY,
        name="Actor Mailbox Event Loop",
        description="Message-passing actor loop processing a synchronized queue or channel mailbox.",
        idiomatic_example="let rec actor_loop mailbox = match Queue.pop mailbox with ...",
    ),

    # Resilience, SOLID & Type Safety Audits
    PatternType.UNCHECKED_EXCEPTION_RAISE: PatternCatalogEntry(
        pattern_type=PatternType.UNCHECKED_EXCEPTION_RAISE,
        category=PatternCategory.TYPE_SAFETY,
        name="Unchecked Exception (failwith/raise)",
        description="Raising unhandled exceptions (`failwith`, `raise (Failure ...)`) instead of typed `Result.t` or `Option.t` return values.",
        idiomatic_example="Return `Result.Error err` instead of throwing `failwith \"error\"`.",
    ),
    PatternType.DEFENSIVE_CATCH_ALL_EXN: PatternCatalogEntry(
        pattern_type=PatternType.DEFENSIVE_CATCH_ALL_EXN,
        category=PatternCategory.RESILIENCE,
        name="Defensive Catch-All Exception Smell",
        description="Catching all exceptions (`try ... with _ -> ...` or `with Failure _ -> ...`) hiding fatal defects and memory corruption.",
        idiomatic_example="Catch only specific expected exceptions or use explicit `Result.catch`.",
    ),
    PatternType.MUTABLE_REF_OVERUSE: PatternCatalogEntry(
        pattern_type=PatternType.MUTABLE_REF_OVERUSE,
        category=PatternCategory.PRINCIPLE,
        name="Mutable Reference Overuse",
        description="Excessive usage of `ref` or `mutable` record fields in functional domains violating immutability.",
        idiomatic_example="Use pure functional recursion and accumulator state instead of mutable refs.",
    ),
    PatternType.PHYSICAL_EQUALITY_SMELL: PatternCatalogEntry(
        pattern_type=PatternType.PHYSICAL_EQUALITY_SMELL,
        category=PatternCategory.TYPE_SAFETY,
        name="Physical Equality (==) Bug Risk",
        description="Using pointer physical equality (`==` / `!=`) instead of value structural equality (`=` / `<>`).",
        idiomatic_example="Use `=` for structural value equality unless pointer identity is specifically required.",
    ),
    PatternType.GOD_MODULE_SRP: PatternCatalogEntry(
        pattern_type=PatternType.GOD_MODULE_SRP,
        category=PatternCategory.PRINCIPLE,
        name="Single Responsibility (God Module)",
        description="Monolithic OCaml module defining excessive values and types (≥30 functions or ≥800 LOC).",
        idiomatic_example="Decompose large modules into cohesive sub-modules or functors.",
    ),
    PatternType.CYCLOMATIC_COMPLEXITY_KISS: PatternCatalogEntry(
        pattern_type=PatternType.CYCLOMATIC_COMPLEXITY_KISS,
        category=PatternCategory.PRINCIPLE,
        name="KISS Complexity (Pattern Matching)",
        description="Function with excessive pattern matching branches or complex nested conditional logic (≥12 branches).",
        idiomatic_example="Decompose complex pattern matches into smaller helper functions.",
    ),
    PatternType.DUPLICATE_CODE_DRY: PatternCatalogEntry(
        pattern_type=PatternType.DUPLICATE_CODE_DRY,
        category=PatternCategory.PRINCIPLE,
        name="Don't Repeat Yourself (DRY)",
        description="Duplicated function implementations across modules.",
        idiomatic_example="Extract shared logic into a common module or functor.",
    ),
    PatternType.CIRCULAR_MODULE_DEPENDENCY: PatternCatalogEntry(
        pattern_type=PatternType.CIRCULAR_MODULE_DEPENDENCY,
        category=PatternCategory.PRINCIPLE,
        name="Circular Module Dependency",
        description="Cyclic cross-module dependencies without explicit `module rec`.",
        idiomatic_example="Decouple modules using signatures or parameterized functors.",
    ),
}
