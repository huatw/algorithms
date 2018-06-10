(* 21. Insert an element at a given position into a list. (easy) *)

let rec insert_at s n = function
  | [] -> [s]
  | x :: xs as l -> if n = 0 then s :: l else x :: insert_at s (n - 1) xs

insert_at "alfa" 1 ["a";"b";"c";"d"];;
(* - : string list = ["a"; "alfa"; "b"; "c"; "d"] *)
insert_at "alfa" 3 ["a";"b";"c";"d"];;
(* - : string list = ["a"; "b"; "c"; "alfa"; "d"] *)
insert_at "alfa" 4 ["a";"b";"c";"d"];;
(* - : string list = ["a"; "b"; "c"; "d"; "alfa"] *)
