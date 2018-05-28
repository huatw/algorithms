(* 0 *)
let rec f arr = match arr with
  | [] -> []
  | x :: xs -> (f xs) @ [x]

(* 1 *)
let f arr =
  let rec aux arr' acc = match arr' with
    | [] -> acc
    | x :: xs -> aux xs (x :: acc)
  in
    aux arr []

(* 2 *)
let f = List.rev

let rec read_lines () =
  try let line = read_line () in
    int_of_string line :: read_lines ()
  with
    End_of_file -> []

let () =
  let arr = read_lines () in
  let ans = f arr in
  List.iter (fun x -> print_int x; print_newline ()) ans
