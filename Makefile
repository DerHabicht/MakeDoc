# Template file: the LaTeX file that ties everything together
template = IntroToGit

# Collect all *.pmd files to be parsed by Pandoc Markdown rules
chapters = $(basename $(wildcard *.pmd))

# Main document rule: run two passes for any annotation in the document
$(template).pdf: $(template).tex $(foreach ch, $(chapters), $(ch).tex)
	pdflatex $(template).tex
	pdflatex $(template).tex

# Generic chapter file rule: parse each *.pmd file into LaTeX format
%.tex: %.pmd
	pandoc $< -f markdown -t latex -o $@

# Cleanup rules
.PHONY: clean
clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.out
	rm -f *.pdf
	rm -f $(foreach f, $(chapters), $(f).tex)
	rm -f *.toc
