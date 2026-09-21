(* Cross-library cycle, side B: parser depends on lexer. *)

let parse tokens =
  let open Arch_lex.Lexer in
  List.filter (fun t -> t != Lexer.Eof) tokens

let rules src =
  let chars = Arch_lex.Lexer.tokenize src in
  List.map (fun _ -> 'x') chars
