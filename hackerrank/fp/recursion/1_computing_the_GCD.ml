let rec gcd a b =
  if b = 0 then
    a
  else
    gcd b (a mod b)

let () =
  let a, b = Scanf.scanf "%d %d" (fun a b -> a, b)
  in
  print_int (gcd a b)

(*
let () =
  let arr = read_line ()
    |> String.split_on_char ' '
    |> List.map int_of_string
  in
  let ans = gcd (List.nth arr 0) (List.nth arr 1)
  in
  print_int ans
*)