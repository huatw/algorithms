(* 24. Lotto: Draw N different random numbers from the set 1..M. (easy) *)

let lotto_select n bound =
  let rec aux acc n = match n with
    | 0 -> acc
    | n ->
      let x = (Random.int (bound - 1)) + 1 in
      aux (x :: acc) (n - 1)
  in
  aux [] n

lotto_select 6 49;;
(* - : int list = [10; 20; 44; 22; 41; 2] *)