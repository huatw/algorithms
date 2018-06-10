(* 23. Extract a given number of randomly selected elements from a list. (medium) *)

let rec rand_select lst n =
  let rec extract acc n = function
    | [] -> raise Not_found
    | h :: t -> if n = 0 then (h, acc @ t) else extract (h :: acc) (n - 1) t
  in
  let extract_rand lst len =
    extract [] (Random.int len) lst
  in
  let rec aux n acc lst len =
    if n = 0 then acc else
      let picked, rest = extract_rand lst len in
      aux (n - 1) (picked :: acc) rest (len - 1)
  in
  let len = List.length lst in
  aux (min n len) [] lst len;;

rand_select ["a";"b";"c";"d";"e";"f";"g";"h"] 3;;
(* - : string list = ["g"; "d"; "a"] *)