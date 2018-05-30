(* 7. Flatten a nested list structure. (medium) *)
(* There is no nested list type in OCaml, so we need to define one
   first. A node of a nested list is either an element, or a list of
   nodes. *)
type 'a node =
  | One of 'a
  | Many of 'a node list

let rec flatten = function
  | [] -> []
  | (One x) :: xs -> x :: (flatten xs)
  | (Many lst) :: xs -> (flatten lst) @ (flatten xs)

let flatten lst =
  let rec aux acc = function
    | [] -> acc
    | (One x) :: xs -> aux (x :: acc) xs
    | (Many lst) :: xs -> aux (aux acc lst) xs
  in
  lst |> aux [] |> List.rev

flatten [ One "a" ; Many [ One "b" ; Many [ One "c" ; One "d" ] ; One "e" ] ];;
(* - : string list = ["a"; "b"; "c"; "d"; "e"] *)
