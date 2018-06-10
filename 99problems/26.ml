(* 26. Generate the combinations of K distinct objects chosen from the N elements of a list. (medium) *)

let rec extract n lst = match n, lst with
  | 0, _ -> [[]]
  | _, [] -> []
  | n, x :: xs ->
    let with_h = List.map (fun acc -> x :: acc) (extract (n - 1) xs) in
    let without_h = extract n xs in
    with_h @ without_h


extract 2 ["a";"b";"c";"d"];;
(* - : string list list =
[["a"; "b"]; ["a"; "c"]; ["a"; "d"]; ["b"; "c"]; ["b"; "d"]; ["c"; "d"]]*)