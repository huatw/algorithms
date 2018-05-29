let f =
  let g str =
    let rec aux = function
      | x :: y :: xs -> y :: x :: aux xs
      | xs -> xs
    in
    str |> Str.split (Str.regexp "") |> aux |> String.concat ""
  in
  List.map g


let rec read_lines () =
  try let line = read_line () in
    line :: read_lines ()
  with
    End_of_file -> []


let () =
  read_lines ()
    |> List.tl
    |> f
    |> List.iter (fun x -> print_string x; print_newline ())
