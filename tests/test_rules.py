"""Tests for OCaml Design Pattern and Safety Rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_ocaml_parser_adapter import NativeOCamlParserAdapter
from pattern_detector.domain.rules.defensive_catch_all_exn_rule import DefensiveCatchAllExnRule
from pattern_detector.domain.rules.effect_handlers_rule import EffectHandlersRule
from pattern_detector.domain.rules.functor_parametric_module_rule import FunctorParametricModuleRule
from pattern_detector.domain.rules.gadts_expression_eval_rule import GadtsExpressionEvalRule
from pattern_detector.domain.rules.physical_equality_smell_rule import PhysicalEqualitySmellRule
from pattern_detector.domain.rules.railway_monadic_bind_rule import RailwayMonadicBindRule


def test_detect_functor_and_gadts():
    sources = {
        "lib/functor.ml": """
        module Make (X : Sig) = struct
          let compute x = x
        end
        """,
        "lib/gadt.ml": """
        type _ expr =
          | Int : int -> int expr
          | Bool : bool -> bool expr
          | Add : int expr * int expr -> int expr
        """,
    }
    parser = NativeOCamlParserAdapter()
    model = parser.parse_sources(sources)

    functors = FunctorParametricModuleRule().detect(model)
    assert len(functors) >= 1

    gadts = GadtsExpressionEvalRule().detect(model)
    assert len(gadts) >= 1


def test_detect_monad_effects_and_safety_smells():
    source = """
    let process_railway id =
      let* user = find_user id in
      let* token = auth user in
      Ok token

    let effect_routine () =
      Effect.perform (Print "Hello")

    let bad_function a b =
      let is_eq = (a == b) in
      try
        if not is_eq then failwith "mismatch"
      with _ ->
        ()
    """
    parser = NativeOCamlParserAdapter()
    model = parser.parse_sources({"lib/sample.ml": source})

    monads = RailwayMonadicBindRule().detect(model)
    assert len(monads) == 1

    effects = EffectHandlersRule().detect(model)
    assert len(effects) == 1

    phys = PhysicalEqualitySmellRule().detect(model)
    assert len(phys) == 1

    catch_all = DefensiveCatchAllExnRule().detect(model)
    assert len(catch_all) == 1
