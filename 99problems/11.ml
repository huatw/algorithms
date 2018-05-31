(* 11. Modified run-length encoding. (easy) *)

type 'a rle = One of 'a | Many of int * 'a

let encode lst =
  let rec count el acc = function
    | x :: xs when x = el -> count el (acc + 1) xs
    | lst -> if acc = 1 then ((One el), lst) else ((Many (acc, el)), lst)
  in
  let rec aux acc = function
    | [] -> acc
    | x :: xs ->
      let res, rest = count x 1 xs in
      aux (res :: acc) rest
  in
  lst |> aux [] |> List.rev

encode ["a";"a";"a";"a";"b";"c";"c";"a";"a";"d";"e";"e";"e";"e"];;
(* - : string rle list =
[Many (4, "a"); One "b"; Many (2, "c"); Many (2, "a"); One "d";
 Many (4, "e")] *)