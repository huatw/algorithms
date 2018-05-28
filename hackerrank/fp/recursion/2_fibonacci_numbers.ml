(* 0 *)
let rec f n = match n with
  | 1 -> 0
  | 2 -> 1
  | n -> f (n - 1) + f (n - 2)

(* 1 *)
let f n =
  let rec aux i prev1 prev2 = match i with
    | n -> prev1 + prev2
    | _ -> aux (i + 1) (prev1 + prev2) prev1
  in
  match n with
  | 1 -> 0
  | 2 -> 1
  | n -> aux 3 1 0


let () =
  let n = read_int () in
  let ans = f n in
  print_int ans