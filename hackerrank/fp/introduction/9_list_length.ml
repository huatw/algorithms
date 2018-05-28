(* 0 *)
let rec f = function
  | [] -> 0
  | x :: xs -> 1 + (f xs)

(* 1 *)
let f arr =
  let rec aux arr' acc = match arr' with
    | [] -> acc
    | x :: xs -> aux xs (acc + 1)
  in
    aux arr 0

(* 2 *)
let f = List.length

let rec read_lines () =
  try let line = read_line () in
    int_of_string line :: read_lines ()
  with
    End_of_file -> []

let () =
  let arr = read_lines () in
  let ans = f arr in
  print_int ans
