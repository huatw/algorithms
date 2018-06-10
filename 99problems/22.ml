(* 22. Create a list containing all integers within a given range. (easy) *)

let rec range st ed =
  if st < ed then st :: range (st + 1) ed
  else if st > ed then st :: range (st - 1) ed
  else [st]

range 4 9;;
(* - : int list = [4; 5; 6; 7; 8; 9] *)
range 9 4;;
(* - : int list = [9; 8; 7; 6; 5; 4] *)