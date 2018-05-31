(* 12. Decode a run-length encoded list. (medium) *)

type 'a rle = One of 'a | Many of int * 'a

let decode lst =
  let rec gen acc = function
    | 0, _ -> acc
    | n, el -> gen (el :: acc) (n - 1, el)
  in
  let rec aux acc = function
    | [] -> acc
    | One el :: xs -> aux (el :: acc) xs
    | Many (n, el) :: xs -> aux (gen acc (n, el)) xs
  in
  lst |> aux [] |> List.rev

decode [Many (4,"a"); One "b"; Many (2,"c"); Many (2,"a"); One "d"; Many (4,"e")];;
(* - : string list =
["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e"] *)