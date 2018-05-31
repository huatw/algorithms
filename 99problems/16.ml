(* 16. Drop every N'th element from a list. (medium) *)

let drop lst n =
  let rec aux acc cnt = function
    | [] -> acc
    | x :: xs ->
      match cnt with
      | 1 -> aux acc n xs
      | _ -> aux (x :: acc) (cnt - 1) xs
  in
  lst |> aux [] n |> List.rev

drop ["a";"b";"c";"d";"e";"f";"g";"h";"i";"j"] 3;;
(* - : string list = ["a"; "b"; "d"; "e"; "g"; "h"; "j"] *)