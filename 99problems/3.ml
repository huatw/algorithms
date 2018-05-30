(* 3. Find the k'th element of a list. (easy) *)

let rec at n lst =
  if n <= 0 then None
  else match n, lst with
    | 1, x :: _ -> Some x
    | _, [] -> None
    | n, _ :: xs -> at (n - 1) xs

at 3 [ "a" ; "b"; "c"; "d"; "e" ];;
(* - : string option = Some "c" *)
at 3 [ "a" ];;
(* - : string option = None *)
