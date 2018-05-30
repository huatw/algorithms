(* 10. Run-length encoding of a list. (easy) *)

let encode lst =
  let rec count el acc = function
    | x :: xs when x = el -> count el (acc + 1) xs
    | lst -> ((acc, el), lst)
  in
  let rec aux acc = function
    | [] -> acc
    | x :: xs ->
      let res, rest = count x 1 xs in
      aux (res :: acc) rest
  in
  lst |> aux [] |> List.rev

encode ["a";"a";"a";"a";"b";"c";"c";"a";"a";"d";"e";"e";"e";"e"];;
(* - : (int * string) list =
[(4, "a"); (1, "b"); (2, "c"); (2, "a"); (1, "d"); (4, "e")] *)