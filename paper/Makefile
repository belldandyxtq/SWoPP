PAPER = paper
REFERENCE = reference.bib


compile:
	latex ${PAPER}.tex
	bibtex ${PAPER}.aux
	latex ${PAPER}.tex
	pdflatex ${PAPER}.tex


clean:
	rm paper.dvi paper.bbl paper.aux paper.pdf paper.log
