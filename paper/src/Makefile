PAPER = paper
REFERENCE = reference.bib


compile:
	latex ${PAPER}.tex
	bibtex ${PAPER}.aux
	latex ${PAPER}.tex
	dvipdfmx ${PAPER}.dvi

clean:
	rm paper.dvi paper.bbl paper.aux paper.pdf paper.log
