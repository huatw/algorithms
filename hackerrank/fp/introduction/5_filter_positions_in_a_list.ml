(* 0 *)
let rec f arr = match arr with
  | [] | [_] -> []
  | _ :: y :: xs -> y :: f xs

(* 1 *)
let f arr =
  let rec aux arr' acc = match arr' with
    | [] | [_] -> acc
    | _ :: y :: xs -> aux xs (y :: acc)
  in
    List.rev (aux arr [])

(* 2 *)
let f arr =
  let g i el = match (i mod 2) with
    | 0 -> []
    | _ -> [el]
  in
  arr |> List.mapi g |> List.flatten

let rec read_lines () =
  try let line = read_line () in
    int_of_string line :: read_lines ()
  with
    End_of_file -> []

let () =
  let arr = read_lines () in
  let ans = f arr in
  List.iter (fun x -> print_int x; print_newline ()) ans

