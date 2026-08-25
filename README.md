# 🐫 DPX-OCaml: Hexagonal Architecture, Functional Design Patterns & Multicore Detector

<p align="center">
  <img src="https://img.shields.io/badge/Language-OCaml%204.14%20%7C%205.0%20%7C%205.3%2B-orange.svg?style=for-the-badge&logo=ocaml" alt="OCaml" />
  <img src="https://img.shields.io/badge/Architecture-Hexagonal%20Ports%20%26%20Adapters-blueviolet.svg?style=for-the-badge" alt="Hexagonal" />
  <img src="https://img.shields.io/badge/Rules-25%20Patterns-success.svg?style=for-the-badge" alt="Rules" />
  <img src="https://img.shields.io/badge/Output-SARIF%20%7C%20HTML%20%7C%20JSON%20%7C%20Markdown-orange.svg?style=for-the-badge" alt="Outputs" />
</p>

---

## 📖 Overview

**DPX-OCaml** is a static analysis and software design pattern detection engine designed for **OCaml (OCaml 4.14, 5.0, 5.3+ / Multicore / Jane Street Core / Dune)**.

Built on **Hexagonal Architecture (Ports and Adapters)** and **Domain-Driven Design (DDD)** principles, DPX-OCaml identifies higher-order Functor parameterization, Abstract Data Type signatures (`type t`), First-Class Modules, GADT AST evaluators, Railway Monadic Bind error pipelines (`let*`, `Result.bind`), OCaml 5 Algebraic Effect Handlers (`Effect.perform`, `try_with`), Multicore Domains parallelism, and critical type safety / resilience hazards (unchecked `failwith`/`raise`, defensive `with _ ->` exception swallowing, and physical equality `==` bugs).

---

## 🔷 Catalog of 25 Supported OCaml Patterns & Safety Rules

| Category | Pattern / Rule | Rule Code | Description |
|---|---|---|---|
| **Module System** | **Functor Parametric Module** | `FUNCTOR_PARAMETRIC_MODULE` | Higher-order module parameterization (`module Make (X : S) = struct ... end`) for compile-time DI. |
| **Module System** | **Abstract Data Type (ADT)** | `ABSTRACT_DATA_TYPE_INTERFACE` | Opaque type declarations (`type t`) in `.mli` interfaces with constructor/destructor operations. |
| **Module System** | **First-Class Module** | `FIRST_CLASS_MODULE` | Packaging modules as runtime values (`(module M : S)`) for dynamic polymorphism. |
| **Module System** | **Module Inclusion & Extension** | `MODULE_INCLUSION_EXTENDER` | Extending or overriding module signatures via `include Module` (e.g. Jane Street Core/Base). |
| **Module System** | **Mutually Recursive Modules** | `RECURSIVE_MODULES` | Cross-module cyclic types and mutual definitions via `module rec A : ... and B : ...`. |
| **Functional Idiom** | **GADT Type-Safe Evaluator** | `GADTS_EXPRESSION_EVAL` | Generalized Algebraic Data Types (`type _ expr = ...`) ensuring compile-time type-safe evaluation. |
| **Functional Idiom** | **Polymorphic Open Variants** | `POLYMORPHIC_VARIANTS` | Open tag polymorphism (`[> `Ok of 'a | `Error of 'b]`) allowing compositional subtyping. |
| **Functional Idiom** | **Railway Monadic Error Pipeline** | `RAILWAY_MONADIC_BIND` | Monadic error composition via `let*`, `let+`, `>>=`, `Result.bind`, or `Option.bind`. |
| **Functional Idiom** | **Pipeline Operator Transformation**| `PIPELINE_OPERATOR` | Pure functional data transformation chaining using `|>` and `@@`. |
| **Functional Idiom** | **Continuation-Passing Style (CPS)** | `CPS_CONTINUATION_PASSING` | Tail-recursive calls passing explicit continuation callback `k` for stack-safety. |
| **Behavioral** | **Curried Strategy Injection** | `CLOSURE_CURRYING_STRATEGY` | Dynamic strategy configuration through partial application, closures, and curried arguments. |
| **Structural** | **Lazy Evaluation & Memoization**| `LAZY_MEMOIZATION` | Deferred on-demand evaluation and automatic result caching via `lazy` and `Lazy.force`. |
| **Structural** | **Record Function VTable** | `RECORD_FUNCTION_VTABLE` | Structs / records containing function fields for explicit object-like virtual dispatch. |
| **Multicore & Effects**| **Algebraic Effect Handlers** | `EFFECT_HANDLERS` | OCaml 5 direct-style algebraic effects (`type _ Effect.t += ...`, `Effect.perform`, `try_with`). |
| **Multicore & Effects**| **Domains Multicore Parallelism** | `DOMAINS_PARALLELISM` | True shared-memory multicore parallelism in OCaml 5 via `Domain.spawn` / `Domainslib`. |
| **Multicore & Effects**| **Lwt / Async Promise Concurrency**| `ASYNC_LWT_PROMISES` | Cooperative asynchronous concurrency using Lwt or Jane Street Async (`Lwt.bind`, `let%bind`). |
| **Multicore & Effects**| **Actor Mailbox Process** | `ACTOR_MAILBOX_PROCESS` | Message-passing actor event loop processing concurrent message channels. |
| **Type Safety** | **Unchecked Exception (failwith/raise)**| `UNCHECKED_EXCEPTION_RAISE` | Raising unhandled exceptions instead of typed `Result.t` or `Option.t`. |
| **Resilience** | **Defensive Catch-All Exception**| `DEFENSIVE_CATCH_ALL_EXN` | Swallowing all exceptions (`try ... with _ -> ...`) hiding fatal bugs and corruption. |
| **Quality & Principles**| **Mutable Reference Overuse** | `MUTABLE_REF_OVERUSE` | Excessive usage of `ref` or `mutable` fields violating functional immutability. |
| **Type Safety** | **Physical Equality (==) Bug Risk**| `PHYSICAL_EQUALITY_SMELL` | Accidental pointer physical equality (`==` / `!=`) instead of structural equality (`=` / `<>`). |
| **Quality & Principles**| **Single Responsibility (God Module)**| `GOD_MODULE_SRP` | Monolithic OCaml module defining excessive values and types (≥30 functions or ≥800 LOC). |
| **Quality & Principles**| **KISS Complexity** | `CYCLOMATIC_COMPLEXITY_KISS` | Function with excessive pattern matching branches (≥12 branches). |
| **Quality & Principles**| **Don't Repeat Yourself (DRY)** | `DUPLICATE_CODE_DRY` | Duplicated function implementations across modules. |
| **Quality & Principles**| **Circular Module Dependency** | `CIRCULAR_MODULE_DEPENDENCY` | Cyclic cross-module dependencies without explicit `module rec`. |

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/bivex/DPX-OCaml.git
cd DPX-OCaml
uv sync
```

### Usage

```bash
# Terminal scan with rich formatting
uv run dpx-ocaml scan /path/to/ocaml_project

# Generate interactive dark Semantic UI HTML dashboard
uv run dpx-ocaml scan /path/to/ocaml_project -H reports/dashboard.html

# Generate SARIF for GitHub Code Scanning
uv run dpx-ocaml scan /path/to/ocaml_project -S reports/security.sarif

# Export AI Context prompt for LLM refactoring
uv run dpx-ocaml scan /path/to/ocaml_project --llm
```

---

## 🌐 The DPX Suite Family

Cross-language architectural static analysis across all modern programming languages:

| Repository | Language / Ecosystem | Primary Paradigms & Focus |
|---|---|---|
| **[`DPX-Huff`](https://github.com/bivex/DPX-Huff)** | **Huff / EVM Stack Assembly** (0.3.x+ / Cancun) | **Macros, Stack Layout, Jumpdest Labels, Selector Dispatchers, GoF 23** |
| **[`DPX-Yul`](https://github.com/bivex/DPX-Yul)** | **Yul / EVM Assembly** (0.8.x - 0.8.28+ / Cancun) | **Memory Management, Storage Packing, Transient Storage (EIP-1153), GoF 23** |
| **[`DPX-Cairo`](https://github.com/bivex/DPX-Cairo)** | **Cairo** (Cairo 1.0 - 2.8+ / Starknet) | **Components, Storage Mapping, Syscalls, Account Abstraction, Upgrades, GoF 23** |
| **[`DPX-Move`](https://github.com/bivex/DPX-Move)** | **Move** (Move 2024 / Aptos / Sui) | **Linear Resources, Abilities, Sui Objects, Hot Potato, Prover, GoF 23** |
| **[`DPX-Lua`](https://github.com/bivex/DPX-Lua)** | **Lua / Luau** (5.1 - 5.4 / LuaJIT) | **Metatable OOP, Coroutines, LuaJIT FFI, GameDev (Roblox/Neovim), GoF 23** |
| **[`DPX-Solidity`](https://github.com/bivex/DPX-Solidity)** | **Solidity** (0.8.x - 0.8.28+) | **EVM Gas Optimization, Proxies, CEI Reentrancy, Yul, GoF 23, Security** |
| **[`DPX-Zig`](https://github.com/bivex/DPX-Zig)** | **Zig** (0.11 - 0.14+) | **Comptime Generics, Allocator RAII, Defer Cleanup, SIMD, GoF 23** |
| **[`DPX-Gleam`](https://github.com/bivex/DPX-Gleam)** | **Gleam** (1.0 - 1.8+) | **Type-Safe OTP Actors, Algebraic Data Types, Railway Monads, GoF 23** |
| **[`DPX-Mojo`](https://github.com/bivex/DPX-Mojo)** | **Mojo** (24.x - 25.x+) | **SIMD Vectorization, Ownership, Memory Safety, GoF 23, AI Acceleration** |
| **[`DPX-Julia`](https://github.com/bivex/DPX-Julia)** | **Julia** (1.6 - 1.11+) | **Multiple Dispatch, Holy Traits, Metaprogramming, Tasks, GoF 23** |
| **[`DPX-Kotlin`](https://github.com/bivex/DPX-Kotlin)** | **Kotlin** (1.8 - 2.0+) | **Coroutines, Flow, Jetpack Compose, Multiplatform, GoF 23** |
| **[`DPX-Swift`](https://github.com/bivex/DPX-Swift)** | **Swift** (5.5 - 6.0+) | **Protocol-Oriented, Actor Concurrency, SwiftUI, ARC Safety** |
| **[`DPX-CSharp`](https://github.com/bivex/DPX-CSharp)** | **C#** (10 - 13 / .NET 8-9) | **Clean Architecture, CQRS MediatR, Channel Pipelines** |
| **[`DPX-TypeScript`](https://github.com/bivex/DPX-TypeScript)** | **TypeScript / JavaScript** | **Hexagonal DI, Decorator Meta, Reactive Streams, React/NestJS** |
| **[`DPX-Rust`](https://github.com/bivex/DPX-Rust)** | **Rust** (Edition 2021/2024) | **Zero-Cost Abstractions, RAII Lifetimes, Typestate Pattern** |
| **[`DPX-Go`](https://github.com/bivex/DPX-Go)** | **Go** (1.18 - 1.24+) | **Goroutine Channels, CSP Concurrency, Pipeline Streaming** |
| **[`DPX-Py`](https://github.com/bivex/DPX-Py)** | **Python** (3.8 - 3.13+) | **Multi-Paradigm Hexagonal, Data Flow Engine, AsyncIO** |
| **[`DPX-Php`](https://github.com/bivex/DPX-Php)** | **PHP** (8.1 - 8.4+) | **Attribute-driven DDD, Fiber Concurrency, Laravel/Symfony** |
| **[`DPX-Haskell`](https://github.com/bivex/DPX-Haskell)** | **Haskell** (GHC 9.2 - 9.12+) | **Category Theory, Monad Transformers, Free Monads, Optics** |
| **[`DPX-OCaml`](https://github.com/bivex/DPX-OCaml)** | **OCaml** (4.14 - 5.3+ Multicore) | **Functor Modules, Effect Handlers, GADTs, Railway Monads** |
| **[`DPX-Elixir`](https://github.com/bivex/DPX-Elixir)** | **Elixir** (OTP 25 - 27+) | **GenServer, DynamicSupervisor, Actor Fault Tolerance** |
| **[`DPX-Erlang`](https://github.com/bivex/DPX-Erlang)** | **Erlang/OTP** (24 - 27+) | **OTP Behaviors, Supervision Trees, Message Passing** |
| **[`DPX-C`](https://github.com/bivex/DPX-C)** | **C** (C99 - C23) | **Opaque Structs, VTables, MISRA/CERT Safety, Arena Allocators** |
| **[`DPX-Cpp`](https://github.com/bivex/DPX-Cpp)** | **C++** (C++14 - C++20) | **CRTP, Policy-Based Design, RAII Memory Safety, ANTLR4 AST** |
| **[`DPX-Java`](https://github.com/bivex/DPX-Java)** | **Java** (17 - 23+) | **Virtual Threads, Spring Boot / Jakarta EE, GoF Patterns** |
| **[`DPX`](https://github.com/bivex/DPX)** | **Clojure** / Meta Engine | **Pure Functional, Multimethods, Homoiconic Macro Architecture** |
---

## 📄 License

MIT © bivex


## 🌐 The DPX Multi-Language Static Analysis Family (28 Languages)

| # | Language | Repository | Ecosystem & Focus |
|:---:|---|---|---|
| 1 | **Clojure** | [`bivex/DPX`](https://github.com/bivex/DPX) | Lisp S-Expressions, Protocols, Multimethods |
| 2 | **C** | [`bivex/DPX-C`](https://github.com/bivex/DPX-C) | Memory Safety, Struct VTables, Idiomatic C11/C23 |
| 3 | **Cairo** | [`bivex/DPX-Cairo`](https://github.com/bivex/DPX-Cairo) | Starknet Smart Contracts, ZK-Rollup Invariants |
| 4 | **C++** | [`bivex/DPX-Cpp`](https://github.com/bivex/DPX-Cpp) | RAII, CRTP, Concepts, Modern C++20/23 |
| 5 | **C#** | [`bivex/DPX-CSharp`](https://github.com/bivex/DPX-CSharp) | .NET 9, Roslyn AST, Linq, Records |
| 6 | **Dart** | [`bivex/DPX-Dart`](https://github.com/bivex/DPX-Dart) | Dart 3.x, Flutter, BLoC, Riverpod, Isolates |
| 7 | **Elixir** | [`bivex/DPX-Elixir`](https://github.com/bivex/DPX-Elixir) | BEAM OTP, GenServer, Supervisors |
| 8 | **Erlang** | [`bivex/DPX-Erlang`](https://github.com/bivex/DPX-Erlang) | Fault Tolerance, Actor Model, OTP Behaviors |
| 9 | **Gleam** | [`bivex/DPX-Gleam`](https://github.com/bivex/DPX-Gleam) | Type-Safe BEAM, Actor Concurrency |
| 10 | **Go** | [`bivex/DPX-Go`](https://github.com/bivex/DPX-Go) | Goroutines, Channels, Composition, Interfaces |
| 11 | **Haskell** | [`bivex/DPX-Haskell`](https://github.com/bivex/DPX-Haskell) | Pure Functional, Monads, Typeclasses, Arrows |
| 12 | **Huff** | [`bivex/DPX-Huff`](https://github.com/bivex/DPX-Huff) | Low-Level EVM Bytecode & Opcodes |
| 13 | **Java** | [`bivex/DPX-Java`](https://github.com/bivex/DPX-Java) | Spring Boot, Enterprise Java, JVM Invariants |
| 14 | **Julia** | [`bivex/DPX-Julia`](https://github.com/bivex/DPX-Julia) | Multiple Dispatch, Scientific Computing |
| 15 | **Kotlin** | [`bivex/DPX-Kotlin`](https://github.com/bivex/DPX-Kotlin) | Coroutines, Multiplatform, Functional DSLs |
| 16 | **Lua** | [`bivex/DPX-Lua`](https://github.com/bivex/DPX-Lua) | Metatables, Coroutines, LuaJIT, Neovim |
| 17 | **Mojo** | [`bivex/DPX-Mojo`](https://github.com/bivex/DPX-Mojo) | SIMD Hardware, Memory Lifetimes, AI Systems |
| 18 | **Move** | [`bivex/DPX-Move`](https://github.com/bivex/DPX-Move) | Aptos & Sui Resource Safety, Linear Types |
| 19 | **OCaml** | [`bivex/DPX-OCaml`](https://github.com/bivex/DPX-OCaml) | **Algebraic Data Types, Functors, Polymorphism** |
| 20 | **PHP** | [`bivex/DPX-Php`](https://github.com/bivex/DPX-Php) | Modern PHP 8.4, Attributes, Traits, Laravel |
| 21 | **Python** | [`bivex/DPX-Py`](https://github.com/bivex/DPX-Py) | Metaprogramming, Protocols, Hexagonal DDD |
| 22 | **Rust** | [`bivex/DPX-Rust`](https://github.com/bivex/DPX-Rust) | Zero-Cost Abstractions, Borrow Checker, Traits |
| 23 | **Solidity** | [`bivex/DPX-Solidity`](https://github.com/bivex/DPX-Solidity) | DeFi Security, Reentrancy, EVM Yul/Assembly |
| 24 | **SQL** | [`bivex/DPX-SQL`](https://github.com/bivex/DPX-SQL) | PostgreSQL, MySQL, SQLite, T-SQL, PL/SQL |
| 25 | **Swift** | [`bivex/DPX-Swift`](https://github.com/bivex/DPX-Swift) | Protocol-Oriented Programming, Actors |
| 26 | **TypeScript** | [`bivex/DPX-TypeScript`](https://github.com/bivex/DPX-TypeScript) | Generics, Conditional Types, Clean Architecture |
| 27 | **Yul** | [`bivex/DPX-Yul`](https://github.com/bivex/DPX-Yul) | EVM Intermediate Representation Optimization |
| 28 | **Zig** | [`bivex/DPX-Zig`](https://github.com/bivex/DPX-Zig) | Comptime, Manual Memory Allocators, C ABI |
