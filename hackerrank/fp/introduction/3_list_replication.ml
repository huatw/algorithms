let rec read_lines () =
  try let line = read_line () in
    int_of_string (line) :: read_lines()
  with
    End_of_file -> []

let f n arr =
  let rec repeat el n' acc = match n' with
    | 0 -> acc
    | x -> repeat el (n' - 1) (el :: acc)
  and aux arr' acc = match arr' with
    | [] -> acc
    | x :: xs -> aux xs (acc @ repeat x n [])
  in
    aux arr []

let () =
  let n::arr = read_lines() in
  let ans = f n arr in
  List.iter (fun x -> print_int x; print_newline ()) ans;;


(* 2 *)
let f n arr =
  let make n' el = List.init n' (fun _ -> el) in
  List.map (make n) arr |> List.flatten
