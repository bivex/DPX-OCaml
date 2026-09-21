(* Repository port implementation: functor parameterised by backend. *)

module type BACKEND = sig
  type t
  val put : string -> t -> unit
end

module Make (B : BACKEND) = struct
  type t = { backend : B.t }

  let save k v = B.put k v
end
