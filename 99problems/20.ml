(* 20. Remove the K'th element from a list. (easy) *)

let remove_at n = function
  | [] -> []
  | x :: xs -> if n = 0 then xs else x :: remove_at (n - 1) xs

remove_at 1 ["a";"b";"c";"d"];;
(* - : string list = ["a"; "c"; "d"] *)