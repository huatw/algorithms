(* 25. Generate a random permutation of the elements of a list. (easy) *)

let rec permutation lst =
  let rec extract acc n = function
    | [] -> raise Not_found
    | h :: t -> if n = 0 then (h, acc @ t) else extract (h :: acc) (n - 1) t
  in
  let extract_rand lst len = extract [] (Random.int len) lst in
  let rec aux acc lst len = match len with
    | 0 -> acc
    | len ->
      let picked, rest = extract_rand lst len in
      aux (picked :: acc) rest (len - 1)
  in
  aux [] lst (List.length lst);;

permutation ["a"; "b"; "c"; "d"; "e"; "f"];;
(* - : string list = ["a"; "e"; "f"; "b"; "d"; "c"] *)