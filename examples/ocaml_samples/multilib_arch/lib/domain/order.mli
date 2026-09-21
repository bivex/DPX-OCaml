(* Order lifecycle contract. *)

type status = Pending | Confirmed | Cancelled

val describe : int -> string
val place : Types.t -> Types.t * status
