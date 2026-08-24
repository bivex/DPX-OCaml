let unsafe_division a b =
  if b = 0 then failwith "Division by zero"
  else a / b

let defensive_swallow_routine x =
  try
    if x < 0 then raise (Failure "Negative argument")
    else x * 2
  with _ ->
    0

let buggy_equality_check s1 s2 =
  (* Physical equality comparison pitfall *)
  if s1 == s2 then true else false
