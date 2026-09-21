(* Cross-library cycle, side A: lexer depends on parser. *)

open Arch_parse.Parser

type token =
  | Ident of string
  | Number of int
  | Eof

let tokenize src =
  match rules src with
  | [] -> [ Eof ]
  | chars -> List.map (fun c -> Ident (String.make 1 c)) chars
