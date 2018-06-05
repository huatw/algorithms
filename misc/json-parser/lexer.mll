{
open Lexing (* The lexbuf is defined in Lexing.mli *)
open Parser (* The type token is defined in parser.mli *)

exception SyntaxError of string

let next_line lexbuf =
  let pos = lexbuf.lex_curr_p in
  lexbuf.lex_curr_p <-
    { pos with pos_bol = lexbuf.lex_curr_pos;
      pos_lnum = pos.pos_lnum + 1 }
}

let digit = ['0'-'9']
let frac = '.' digit*
let e_notation = ['e' 'E'] ['-' '+']? digit+
let int = '-'? digit+
let float = int frac? e_notation?
let white = [' ' '\t']+
let newline = '\r' | '\n' | "\r\n"
let id = ['a'-'z' 'A'-'Z' '_'] ['a'-'z' 'A'-'Z' '0'-'9' '_']*
let str = [^'"' '\n']+

rule read = parse
  | white        { read lexbuf } (* skip blanks *)
  | newline      { next_line lexbuf; read lexbuf } (* inc #line *)
  | int as lxm   { INT (int_of_string lxm) }
  | float as lxm { FLOAT (float_of_string lxm) } (* lxm = (Lexing.lexeme lexbuf) *)
  | "true"       { TRUE }
  | "false"      { FALSE }
  | "null"       { NULL }
  | '"'          { read_string (Buffer.create 17) lexbuf }
  | '{'          { LEFT_BRACE }
  | '}'          { RIGHT_BRACE }
  | '['          { LEFT_BRACK }
  | ']'          { RIGHT_BRACK }
  | ':'          { COLON }
  | ','          { COMMA }
  | _ as lxm     { raise (SyntaxError ("Unexpected char: " ^ (Char.escaped lxm))) }
  | eof          { EOF }

and read_string buf = parse
  | '"'          { STRING (Buffer.contents buf) }
  | '\\' '"'     { Buffer.add_char buf '"'; read_string buf lexbuf }
  | str as lxm   { Buffer.add_string buf lxm; read_string buf lexbuf }
  | _ as lxm     { raise (SyntaxError ("Illegal string character: " ^ (Char.escaped lxm))) }
  | eof          { raise (SyntaxError ("String is not terminated")) }
