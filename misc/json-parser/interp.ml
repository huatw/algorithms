open Ast

let rec eval_prog = function
  | `Assoc pair_lst -> pair_lst
    |> List.map (fun (k, v) -> "\"" ^ k ^ "\"" ^ ": " ^ eval_prog v)
    |> String.concat ",\n"
    |> fun s -> "{\n" ^ s ^ "\n}\n"
  | `List lst -> lst
    |> List.map (fun e -> eval_prog e)
    |> String.concat ", "
    |> fun s -> "[" ^ s ^ "]"
  | `Bool b -> string_of_bool b
  | `String s -> "\"" ^ s ^ "\""
  | `Float n -> string_of_float n
  | `Int n -> string_of_int n
  | `Null -> "null"
  | _ -> failwith "not implemented"