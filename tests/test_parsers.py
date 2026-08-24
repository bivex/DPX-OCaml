"""Tests for Native OCaml Parser Adapter."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_ocaml_parser_adapter import NativeOCamlParserAdapter


def test_parse_ocaml_types_and_functions():
    source = """
    open Base

    type 'a tree =
      | Leaf
      | Node of 'a * 'a tree * 'a tree

    type buffer = {
      data : string;
      mutable pos : int;
    }

    let rec insert x = function
      | Leaf -> Node (x, Leaf, Leaf)
      | Node (v, l, r) ->
        if x < v then Node (v, insert x l, r)
        else Node (v, l, insert x r)
    """
    parser = NativeOCamlParserAdapter()
    model = parser.parse_sources({"lib/tree.ml": source})

    assert "Tree" in model.modules
    m = model.modules["Tree"]
    assert "Base" in m.opens
    assert "tree" in m.types
    assert m.types["tree"].is_variant is True
    assert "buffer" in m.types
    assert m.types["buffer"].is_record is True
    assert m.types["buffer"].record_fields[1].is_mutable is True
    assert "insert" in m.functions
    assert m.functions["insert"].is_rec is True


def test_parse_functors_and_submodules():
    source = """
    module Make (Ord : Map.OrderedType) = struct
      type key = Ord.t
      type 'a t = (key * 'a) list

      let empty = []
      let add k v t = (k, v) :: t
    end
    """
    parser = NativeOCamlParserAdapter()
    model = parser.parse_sources({"lib/custom_map.ml": source})

    m = model.modules["Custom_map"]
    assert "Make" in m.submodules
    sub = m.submodules["Make"]
    assert sub.is_functor is True
    assert "Ord" in sub.functor_param
