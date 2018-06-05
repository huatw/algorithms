.PHONY:	all clean byte native profile debug

OCB_FLAGS = -use-menhir -tag thread -use-ocamlfind -quiet -pkg core
OCB = 		ocamlbuild

all: native # byte profile debug

clean:
	$(OCB) -clean

native:
	$(OCB) $(OCB_FLAGS) main.native

byte:
	$(OCB) $(OCB_FLAGS) main.byte

profile:
	$(OCB) -tag profile main.native

debug:
	$(OCB) -tag debug main.byte
