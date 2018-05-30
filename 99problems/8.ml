(* 8. Eliminate consecutive duplicates of list elements. (medium) *)

let rec compress = function
  | [] -> []
  | [x] -> [x]
  | x :: (y :: _ as xs) when x = y -> compress xs
  | x :: (y :: _ as xs) -> x :: compress xs

compress ["a";"a";"a";"a";"b";"c";"c";"a";"a";"d";"e";"e";"e";"e"];;
(* - : string list = ["a"; "b"; "c"; "a"; "d"; "e"] *)