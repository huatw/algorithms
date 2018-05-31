(* 14. Duplicate the elements of a list. (easy) *)

let duplicate lst = lst |> List.map (fun el -> [el; el]) |> List.flatten

let rec duplicate = function
  | [] -> []
  | x :: xs -> x :: x :: duplicate xs

duplicate ["a";"b";"c";"c";"d"];;
(* - : string list = ["a"; "a"; "b"; "b"; "c"; "c"; "c"; "c"; "d"; "d"] *)