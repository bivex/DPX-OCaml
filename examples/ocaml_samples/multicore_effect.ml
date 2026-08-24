open Effect
open Effect.Deep

type _ Effect.t += Log : string -> unit Effect.t

let perform_log msg =
  Effect.perform (Log msg)

let run_with_logger fn =
  try_with fn () {
    effc = (fun (type a) (eff : a Effect.t) ->
      match eff with
      | Log str -> Some (fun (k : (a, _) continuation) ->
          Printf.printf "[LOG] %s\n" str;
          continue k ())
      | _ -> None)
  }

let parallel_computation chunks =
  let domains = List.map (fun chunk ->
    Domain.spawn (fun () -> List.fold_left (+) 0 chunk)
  ) chunks in
  List.map Domain.join domains
