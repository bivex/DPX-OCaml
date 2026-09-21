(* Order lifecycle — deliberately reaches into infrastructure (layer violation:
   DOMAIN must not depend on INFRASTRUCTURE) and opens sibling Types (cycle). *)

open Arch_infra.Db
open Types

type status = Pending | Confirmed | Cancelled

let describe n = Printf.sprintf "order:%d" n

let place o =
  let saved = Db.save "orders" in
  ({ o with amount = o.amount +. 1.0 }, if saved then Confirmed else Pending)
