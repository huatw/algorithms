(* 13. Run-length encoding of a list (direct solution). (medium) *)
type 'a rle = One of 'a | Many of int * 'a

let encode lst =
  let rle n el = if n = 0 then One el else Many (n + 1, el)
  in
  let rec aux n acc = function
    | [] -> acc
    | [x] -> rle n x :: acc
    | x :: (y :: _ as xs) when x = y -> aux (n + 1) acc xs
    | x :: (y :: _ as xs) -> aux 0 (rle n x :: acc) xs
  in
  lst |> aux 0 [] |> List.rev

encode ["a";"a";"a";"a";"b";"c";"c";"a";"a";"d";"e";"e";"e";"e"];;
(* - : string rle list =
[Many (4, "a"); One "b"; Many (2, "c"); Many (2, "a"); One "d";
 Many (4, "e")] *)