# Template file: the LaTeX file that ties everything together
TeXtemplate = IntroToGit

# Collect all files with macros
macro_text = $(basename $(wildcard *.m4md))
# Collect all files to be processed directly by pandoc
pandoc_text = $(basename $(wildcard *.txt))

# Uncomment this to preserve intermediate files for debugging
#.SECONDARY:

# Main document rule: run two passes for any annotation in the document
latex: $(TeXtemplate).tex \
					$(foreach ch, $(macro_text), $(ch).tex) \
					$(foreach ch, $(pandoc_text), $(ch).tex)
	pdflatex $(TeXtemplate).tex
	pdflatex $(TeXtemplate).tex

# Process any files with macros
%.txt: %.m4md
	m4 $< > $@

# Generic chapter file rule: parse each *.pmd file into LaTeX format
%.tex: %.txt
	pandoc $< -f markdown -t latex -o $@

# Cleanup rules
.PHONY: clean
clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.out
	rm -f *.pdf
	rm -f $(foreach f, $(macro_text), $(f).txt)
	rm -f $(foreach f, $(macro_text), $(f).tex)
	rm -f $(foreach f, $(pandoc_text), $(f).tex)
	rm -f *.toc
