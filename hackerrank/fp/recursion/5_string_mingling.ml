let f (s1, s2) =
  let rec aux = function
    | x :: xs, y :: ys -> x :: y :: aux (xs, ys)
    | _ -> []
  in
  let sl1, sl2 = (Str.split (Str.regexp "") s1, Str.split (Str.regexp "") s2)
  in
  String.concat "" (aux (sl1, sl2))

let () =
  Scanf.scanf ("%s\n%s") (fun a b -> (a, b))
    |> f
    |> print_string
