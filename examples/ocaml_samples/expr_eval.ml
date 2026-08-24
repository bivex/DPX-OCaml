type _ expr =
  | Int : int -> int expr
  | Bool : bool -> bool expr
  | Add : int expr * int expr -> int expr
  | Eq : int expr * int expr -> bool expr

let rec eval : type a. a expr -> a = function
  | Int n -> n
  | Bool b -> b
  | Add (e1, e2) -> eval e1 + eval e2
  | Eq (e1, e2) -> eval e1 = eval e2

module type Printer = sig
  val print_expr : string -> unit
end

let render (module P : Printer) str =
  P.print_expr str
