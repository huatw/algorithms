let f =
  let g line =
    let k chs =
      let rec aux n chs acc = match n with
        | 0 -> acc
        | n ->
          let nchs = (List.tl chs) @ [List.hd chs]
          in aux (n - 1) nchs (nchs :: acc)
      in aux (List.length chs) chs []
    in line
      |> Str.split (Str.regexp "")
      |> k
      |> List.map (String.concat "")
      |> List.rev
      |> String.concat " "
  in List.map g

let rec read_lines () =
  try
    let line = read_line () in
    line :: read_lines ()
  with
    End_of_file -> []

let () = read_lines ()
  |> List.tl
  |> f
  |> List.iter (fun el -> print_string el; print_newline ())
