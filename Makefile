#!/usr/bin/makefile

LATEX=xelatex
BIB=bibtex

PARTES = $(wildcard partes/*.tex)
PARTES = $(wildcard figuras/*)

all: main.pdf
	$(MAKE) clean

main.pdf: main.tex referencias.bib $(PARTES) $(FIGURAS)
	$(LATEX) main.tex
	$(BIB) main.aux
	$(LATEX) main.tex
	$(LATEX) main.tex

clean:
	rm -f *.aux *.bbl *.blg *.bcf *.run.xml *.log *.toc *.out *.lof *.lot *.fls

cleanall: clean
	rm -f main.pdf main.xdv main.synctex.gz main.fdb_latexmk

.PHONY: all clean cleanall

