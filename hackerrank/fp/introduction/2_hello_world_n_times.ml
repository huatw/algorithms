(* 1 *)
let rec f = function
  | 0 -> ()
  | n -> print_string "Hello World"; f (n-1)

let () =
  let n = read_int () in
  f n



(* 2 *)
let f n =
  let rec aux n acc =
    match n with
    | 0 -> print_string (String.concat "\n" acc)
    | n -> aux (n - 1) ("Hello World" :: acc)
  in
  aux n []

let () =
  let n = read_int () in
  f n



(* 3 *)
let f n =
  String.concat "\n" (List.init n (fun _ -> "Hello World"))

let () =
  let n = read_int () in
  print_string (f n)