(* 1 *)
let f n arr =
  let rec aux arr' acc = match arr' with
    | [] -> acc
    | x :: xs ->
      let acc' = if x < n then x :: acc else acc
      in aux xs acc'
  in
    List.rev (aux arr [])

(* 2 *)
let f n arr =
  let rec aux arr' acc = match arr' with
    | [] -> acc
    | x :: xs when x < n -> aux xs (x :: acc)
    | x :: xs -> aux xs acc
  in
    List.rev (aux arr [])

(* 3 *)
let f n = List.filter (fun el -> el < n)

let rec read_lines () =
  try let line = read_line () in
    int_of_string line :: read_lines ()
  with
    End_of_file -> []

let () =
  let x :: xs = read_lines () in
  let ans = f x xs in
  List.iter (fun x -> print_int x; print_newline ()) ans
