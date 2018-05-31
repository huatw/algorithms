(* 19. Rotate a list N places to the left. (medium) *)

let split lst n =
  let rec aux acc = function
    | 0, l -> (List.rev acc, l)
    | _, [] -> (lst, [])
    | n, x :: xs -> aux (x :: acc) (n - 1, xs)
  in
  aux [] (n, lst)

let rotate lst n =
  let len = List.length lst in
    let n = if len = 0 then 0 else (n mod len + len) mod len in
    if n = 0 then
      lst
    else
      let a, b = split lst n in
      b @ a

rotate ["a"; "b"; "c"; "d"; "e"; "f"; "g"; "h"] 3;;
(* - : string list = ["d"; "e"; "f"; "g"; "h"; "a"; "b"; "c"] *)
rotate ["a"; "b"; "c"; "d"; "e"; "f"; "g"; "h"] (-2);;
(* - : string list = ["g"; "h"; "a"; "b"; "c"; "d"; "e"; "f"] *)