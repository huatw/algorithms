let f =
  let rec calc n el prev acc =
    if n = 11 then acc else calc (n + 1) el (prev *. el /. (float_of_int n)) (acc +. prev)
  in
  List.map (fun el -> calc 1 el 1.0 0.0)


let rec read_lines () =
  try let line = read_line () in
    line :: read_lines ()
  with
    End_of_file -> []


let () =
  let _ :: xs = read_lines () in
  let arr = List.map float_of_string xs in
  let ans = f arr in
  List.iter (fun x -> print_float x; print_newline ()) ans
