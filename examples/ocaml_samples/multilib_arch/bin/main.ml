(* Entry point of the multilib architecture sample. *)

let () =
  let tokens = Arch_lex.Lexer.tokenize "dpx" in
  let msg = Arch_domain.Order.describe (List.length tokens) in
  print_endline msg
