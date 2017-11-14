# Uncomment this line if you don't want to rely on the environment for the
# template file name. NOTE: DO NOT include the .tex extension of the filename,
# just the base name for your template file.
#template=[LaTeX TEMPLATE FILE]
#tldiv=default

# Collect all files with macros
macro_text = $(basename $(wildcard *.m4))
# Collect all files to be processed directly by pandoc
pandoc_text = $(basename $(wildcard *.md))

# Uncomment this to preserve intermediate files for debugging
#.SECONDARY:

pdf: $(template).tex
	ln -s .texmacros macros
	make tex_compile
	rm macros

web:
	ln -s .htmlmacros macros
	make html_compile
	rm macros

doc:
	ln -s .docmacros macros
	make doc_compile
	rm macros

wc:
	@$(mddir)mdwc.py

# Run two passes for any annotation in the document
tex_compile: $(template).tex \
					$(foreach ch, $(macro_text), $(basename $(ch)).tex) \
					$(foreach ch, $(pandoc_text), $(ch).tex)
	lualatex $(template).tex
	lualatex $(template).tex

# Convert to html snippet documents
html_compile: $(foreach ch, $(macro_text), $(basename $(ch)).md) \
		$(foreach ch, $(pandoc_text), $(ch).md)
	$(foreach ch, $(macro_text), pandoc -i $(basename $(ch)).md -o $(basename $(ch)).html;)
	$(foreach ch, $(pandoc_text), pandoc -i $(ch).md -o $(ch).html;)

# Convert to MS Word documents for upload to Google Drive
doc_compile: $(foreach ch, $(macro_text), $(basename $(ch)).md) \
		$(foreach ch, $(pandoc_text), $(ch).md)
	$(foreach ch, $(macro_text), pandoc -i $(basename $(ch)).md -o $(basename $(ch)).docx;)
	$(foreach ch, $(pandoc_text), pandoc -i $(ch).md -o $(ch).docx;)

# Process any files with macros
%.md: %.md.m4
	m4 $< > $@

# Generic chapter file rule: parse each *.md file into LaTeX format
%.tex: %.md
	pandoc --top-level-divisions=$(tldiv) $< -f markdown -t latex -o $@

# Cleanup rules
.PHONY: clean
clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.out
	rm -f *.pdf
	rm -f $(foreach f, $(basename $(macro_text)), $(f).md)
	rm -f $(foreach f, $(basename $(macro_text)), $(f).tex)
	rm -f $(foreach f, $(pandoc_text), $(f).tex)
	rm -f $(foreach f, $(basename $(macro_text)), $(f).html)
	rm -f $(foreach f, $(pandoc_text), $(f).html)
	rm -f *.docx
	rm -f *.toc
	rm -f macros
