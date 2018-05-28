(* odd negative number mod is -1 ! *)
(* 0 *)
let rec f arr = match arr with
  | [] -> 0
  | x :: xs when x mod 2 = 0 -> (f xs)
  | x :: xs -> x + (f xs)

(* 1 *)
let f arr =
  let rec aux arr' acc = match arr' with
    | [] -> acc
    | x :: xs when x mod 2 = 0 -> aux xs acc
    | x :: xs -> aux xs (acc + x)
  in
    aux arr 0

(* 2 *)
let f =
  let g acc el = match el mod 2 with
    | 0 -> acc
    | _ -> acc + el
  in
  List.fold_left g 0

let rec read_lines () =
  try let line = read_line () in
    int_of_string line :: read_lines ()
  with
    End_of_file -> []

let () =
  let arr = read_lines () in
  let ans = f arr in
  print_int ans
