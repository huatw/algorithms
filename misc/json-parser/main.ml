open Core
open Lexer
open Lexing

let print_position outx lexbuf =
  let pos = lexbuf.lex_curr_p in
  fprintf outx "%s: %d: %d" pos.pos_fname
    pos.pos_lnum (pos.pos_cnum - pos.pos_bol + 1)

let parse_with_error lexbuf =
  try Parser.prog Lexer.read lexbuf with
  | SyntaxError msg ->
    fprintf stderr "%a: %s\n" print_position lexbuf msg;
    None
  | Parser.Error ->
    fprintf stderr "%a: syntax error\n" print_position lexbuf;
    exit (-1)

let rec parse_and_print lexbuf =
  match parse_with_error lexbuf with
  | Some value ->
    parse_and_print lexbuf
  | None ->  ()

(*
let () =
  let filename = Sys.argv.(1) in
  let inx = In_channel.create filename in
  let lexbuf = Lexing.from_channel inx in
  lexbuf.lex_curr_p <- { lexbuf.lex_curr_p with pos_fname = filename};
  parse_and_print lexbuf;
  print_endline "No Error...";
  In_channel.close inx
 *)

let lex s = s |> Lexing.from_string |> Lexer.read

let parse s = s |> Lexing.from_string |> Parser.prog Lexer.read

let interp s = match parse s with
  | Some exp -> Interp.eval_prog exp
  | None -> "empty string"
