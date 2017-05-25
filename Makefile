# Uncomment this line if you don't want to rely on the environment for the
# template file name. NOTE: DO NOT include the .tex extension of the filename,
# just the base name for your template file.
#template=[LaTeX TEMPLATE FILE]
#tldiv=default

# Collect all files with macros
macro_text = $(basename $(wildcard *.m4md))
# Collect all files to be processed directly by pandoc
pandoc_text = $(basename $(wildcard *.md))

# Uncomment this to preserve intermediate files for debugging
#.SECONDARY:

# Run two passes for any annotation in the document
latex: $(template).tex \
					$(foreach ch, $(macro_text), $(ch).tex) \
					$(foreach ch, $(pandoc_text), $(ch).tex)
	pdflatex $(template).tex
	pdflatex $(template).tex

# Process any files with macros
%.md: %.m4md
	m4 $< > $@

# Generic chapter file rule: parse each *.md file into LaTeX format
%.tex: %.md
	pandoc --chapters $< -f markdown -t latex -o $@

# Cleanup rules
.PHONY: clean
clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.out
	rm -f *.pdf
	rm -f $(foreach f, $(macro_text), $(f).md)
	rm -f $(foreach f, $(macro_text), $(f).tex)
	rm -f $(foreach f, $(pandoc_text), $(f).tex)
	rm -f *.toc
