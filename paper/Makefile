PAPER = paper
REFERENCE = reference.bib


compile:
	latex ${PAPER}.tex
	bibtex ${PAPER}.aux
	latex ${PAPER}.tex
	pdflatex ${PAPER}.tex
