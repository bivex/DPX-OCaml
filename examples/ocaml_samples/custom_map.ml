module type OrderedType = sig
  type t
  val compare : t -> t -> int
end

module Make (Ord : OrderedType) = struct
  type key = Ord.t
  type 'a t = (key * 'a) list

  let empty = []

  let create () = []

  let add k v m = (k, v) :: m

  let find k m = List.assoc_opt k m
end
