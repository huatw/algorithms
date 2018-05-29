let make_list prev_list =
  let rec aux prev acc = match prev with
    | [] -> acc
    | [_] -> aux [] (1 :: acc)
    | x :: y :: xs -> aux (y :: xs) ((x + y) :: acc)
  in
    aux prev_list [1]


let f n =
  let rec make_lists n prev_list acc = match n with
    | 0 -> acc
    | _ ->
      let new_list = make_list prev_list
      in
      make_lists (n - 1) new_list (new_list :: acc)
  in
  List.rev (make_lists n [] [])


let () =
  let n = read_int () in
  let ans = f n in
  ans
    |> List.map (fun el -> el |> List.map string_of_int |> String.concat " ")
    |> List.iter (fun el -> print_string el; print_newline ())

