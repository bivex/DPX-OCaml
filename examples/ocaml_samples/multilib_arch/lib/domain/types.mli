(* Domain type contracts: one abstract identity, one concrete record. *)

type id

type t = {
  id : id;
  amount : float;
}
