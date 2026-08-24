let ( let* ) = Result.bind

let validate_input str =
  if String.length str > 0 then Ok str else Error "Empty input"

let parse_number str =
  match int_of_string_opt str with
  | Some n -> Ok n
  | None -> Error "Invalid integer"

let execute_flow raw_text =
  let* text = validate_input raw_text in
  let* num = parse_number text in
  Ok (num * 2)

let transform_data data =
  data
  |> List.map (fun x -> x * 2)
  |> List.filter (fun x -> x > 10)
  |> List.fold_left (+) 0
