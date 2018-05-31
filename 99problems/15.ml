(* 15. Replicate the elements of a list a given number of times. (medium) *)

let replicate lst n = lst |> List.map (fun el -> List.init n (fun _ -> el)) |> List.flatten

let rec replicate lst n =
  let rec prepend acc el = function
    | 0 -> acc
    | n -> prepend (el :: acc) el (n - 1)
  in
  let rec aux acc = function
    | [] -> acc
    | x :: xs -> aux (prepend acc x n) xs
  in
  lst |> aux [] |> List.rev

replicate ["a";"b";"c"] 3;;
(* - : string list = ["a"; "a"; "a"; "b"; "b"; "b"; "c"; "c"; "c"] *)