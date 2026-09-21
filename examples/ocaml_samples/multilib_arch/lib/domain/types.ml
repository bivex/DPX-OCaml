(* Shared domain types. References Order on purpose: part of a deliberate
   intra-library cycle Order <-> Types. *)

type id = int

type t = {
  id : id;
  amount : float;
}

let status_of _ : Order.status = Order.Pending
