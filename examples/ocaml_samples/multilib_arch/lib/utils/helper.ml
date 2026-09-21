(* A tiny helper nobody depends on — the orphan module of this fixture. *)

let rec iterate f n x =
  if n <= 0 then x else iterate f (n - 1) (f x)
