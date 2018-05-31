(* 17. Split a list into two parts; the length of the first part is given. (easy) *)

let split lst n =
  let rec aux acc = function
    | 0, l -> (List.rev acc, l)
    | _, [] -> (lst, [])
    | n, x :: xs -> aux (x :: acc) (n - 1, xs)
  in
  aux [] (n, lst)

split ["a";"b";"c";"d";"e";"f";"g";"h";"i";"j"] 3;;
(* - : string list * string list =
(["a"; "b"; "c"], ["d"; "e"; "f"; "g"; "h"; "i"; "j"]) *)
split ["a";"b";"c";"d"] 5;;
(* - : string list * string list = (["a"; "b"; "c"; "d"], []) *)
