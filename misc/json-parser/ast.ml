type expr = [
  | `Assoc of (string * expr) list
  | `Bool of bool
  | `Float of float
  | `Int of int
  | `List of expr list
  | `Null
  | `String of string
]
