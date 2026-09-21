(* In-memory persistence adapter. Applies the repository functor from the
   ports layer: Arch_ports.Repo.Make (Store) — a functor application edge. *)

module Store = struct
  type t = (string, string) Hashtbl.t

  let put tbl k v = Hashtbl.replace tbl k v
end

module Backend = Arch_ports.Repo.Make (Store)

let save name =
  let repo = { Backend.backend = Hashtbl.create 16 } in
  Backend.save name repo;
  true
