(* 18. Extract a slice from a list. (medium) *)

let split lst n =
  let rec aux acc = function
    | 0, l -> (List.rev acc, l)
    | _, [] -> (lst, [])
    | n, x :: xs -> aux (x :: acc) (n - 1, xs)
  in
  aux [] (n, lst)

let slice lst st ed =
  let _, lst' = split lst st in
  let lst'', _ = split lst' (ed - st) in
  lst''

slice ["a";"b";"c";"d";"e";"f";"g";"h";"i";"j"] 2 6;;
(* - : string list = ["c"; "d"; "e"; "f"; "g"] *)