"""Domain Code Model for OCaml (OCaml 4.14 - 5.3+ / Multicore) Static Architecture and Pattern Analysis."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from typing import Any, Sequence

from pattern_detector.domain.value_objects import SourceLocation


@dataclass
class TypeRecordField:
    """Represents a field in an OCaml record type."""

    name: str
    type_str: str = ""
    is_mutable: bool = False
    is_function: bool = False


@dataclass
class TypeVariantConstructor:
    """Represents a constructor in an OCaml variant or GADT type."""

    name: str
    args: list[str] = field(default_factory=list)
    return_type: str = ""
    is_gadt: bool = False


@dataclass
class TypeModel:
    """Represents an OCaml type definition (`type ...`)."""

    name: str
    params: list[str] = field(default_factory=list)
    is_abstract: bool = False
    is_record: bool = False
    is_variant: bool = False
    is_gadt: bool = False
    is_polymorphic_variant: bool = False
    record_fields: list[TypeRecordField] = field(default_factory=list)
    variant_constructors: list[TypeVariantConstructor] = field(default_factory=list)
    location: SourceLocation | None = None


@dataclass
class FunctionParamModel:
    """Represents a parameter in an OCaml function."""

    name: str
    is_labeled: bool = False
    is_optional: bool = False
    type_annotation: str = ""


@dataclass
class FunctionModel:
    """Represents an OCaml function / value definition (`let ... = ...`)."""

    name: str
    params: list[FunctionParamModel] = field(default_factory=list)
    is_rec: bool = False
    body: str = ""
    cyclomatic_complexity: int = 1
    calls: list[tuple[str, str]] = field(default_factory=list)  # [(module_name, func_name), ...]
    has_raise: bool = False
    has_try_with: bool = False
    has_ref: bool = False
    has_physical_eq: bool = False
    has_pipe: bool = False
    has_monadic_bind: bool = False
    location: SourceLocation | None = None

    @property
    def id_str(self) -> str:
        return f"{self.name}"

    @property
    def arity(self) -> int:
        return len(self.params)


@dataclass
class ModuleModel:
    """Represents an OCaml module (`module Name = struct ... end` or top-level file)."""

    name: str
    file_path: str
    is_functor: bool = False
    functor_param: str = ""
    functor_sig: str = ""
    is_recursive: bool = False
    includes: list[str] = field(default_factory=list)  # include Module
    opens: list[str] = field(default_factory=list)  # open Module
    types: dict[str, TypeModel] = field(default_factory=dict)
    functions: dict[str, FunctionModel] = field(default_factory=dict)
    submodules: dict[str, ModuleModel] = field(default_factory=dict)
    raw_source: str = ""
    location: SourceLocation | None = None

    def find_function(self, name: str) -> FunctionModel | None:
        return self.functions.get(name)


@dataclass
class CodeModel:
    """Aggregated semantic domain model of an OCaml codebase."""

    modules: dict[str, ModuleModel] = field(default_factory=dict)
    project_path: str = ""

    def all_modules(self) -> list[ModuleModel]:
        res = list(self.modules.values())
        for m in self.modules.values():
            res.extend(m.submodules.values())
        return res

    def all_functions(self) -> list[FunctionModel]:
        res = []
        for m in self.all_modules():
            res.extend(m.functions.values())
        return res

    def find_module(self, name: str) -> ModuleModel | None:
        return self.modules.get(name)

    # -------------------------------------------------------------------------
    # Cross-Module Dependency Graph
    # -------------------------------------------------------------------------

    def build_module_dependency_graph(self) -> dict[str, set[str]]:
        graph: dict[str, set[str]] = {mod_name: set() for mod_name in self.modules}

        for mod_name, mod in self.modules.items():
            for inc in mod.includes:
                if inc in self.modules and inc != mod_name:
                    graph[mod_name].add(inc)
            for op in mod.opens:
                if op in self.modules and op != mod_name:
                    graph[mod_name].add(op)
            for fn in mod.functions.values():
                for call_mod, _ in fn.calls:
                    if call_mod and call_mod in self.modules and call_mod != mod_name:
                        graph[mod_name].add(call_mod)

        return graph

    def find_circular_dependencies(self, max_depth: int = 8, max_cycles: int = 50) -> list[list[str]]:
        graph = self.build_module_dependency_graph()
        cycles: list[list[str]] = []
        visited: set[str] = set()

        def _dfs(current: str, path: list[str], path_set: set[str]) -> None:
            if len(cycles) >= max_cycles:
                return
            path.append(current)
            path_set.add(current)

            for neighbor in sorted(graph.get(current, set())):
                if neighbor == path[0] and len(path) > 1:
                    canonical = tuple(path)
                    rotations = [canonical[i:] + canonical[:i] for i in range(len(canonical))]
                    min_rot = list(min(rotations))
                    if min_rot not in cycles:
                        cycles.append(min_rot)
                elif neighbor not in path_set and neighbor not in visited and len(path) < max_depth:
                    _dfs(neighbor, path, path_set)

            path.pop()
            path_set.remove(current)

        for node in sorted(graph.keys()):
            _dfs(node, [], set())
            visited.add(node)

        return cycles
