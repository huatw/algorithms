(* 4. Find the number of elements of a list. (easy) *)

let length lst =
  let rec aux acc = function
    | [] -> acc
    | _ :: xs -> aux (acc + 1) xs
  in
  aux 0 lst

length [ "a" ; "b" ; "c"];;
(* - : int = 3 *)
length [];;
(* - : int = 0 *)