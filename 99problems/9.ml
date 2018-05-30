(* 9. Pack consecutive duplicates of list elements into sublists. (medium) *)

let pack lst =
  let rec group el acc = function
    | x :: xs when x = el -> group el (x :: acc) xs
    | lst -> (acc, lst)
  in
  let rec aux acc = function
    | [] -> acc
    | x :: xs ->
      let g, rest = group x [x] xs in
      aux (g :: acc) rest
  in
  lst |> aux [] |> List.rev

pack ["a";"a";"a";"a";"b";"c";"c";"a";"a";"d";"d";"e";"e";"e";"e"];;
(* - : string list list =
[["a"; "a"; "a"; "a"]; ["b"]; ["c"; "c"]; ["a"; "a"]; ["d"; "d"];
 ["e"; "e"; "e"; "e"]] *)