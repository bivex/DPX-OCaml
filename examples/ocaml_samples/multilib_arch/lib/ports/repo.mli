(* Repository port expressed as a functor over the storage backend. *)

module type BACKEND = sig
  type t
  val put : string -> t -> unit
end

module Make (B : BACKEND) : sig
  type t
  val save : string -> t -> unit
end
