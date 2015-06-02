# MakeDoc
A makefile for creating different kinds of documents.

### Summary
I use LaTeX for just about everything from documents to PowerPoint
presentations. However, LaTeX doesn't always live up to its promise of making
one focus on content rather than presentation (which I forgive because it is a
very strong formatting markup language). However, I do like separating content
from format, which is why tools like Pandoc and Pandoc's flavor of Markdown are
powerful to me. The makefile in this repository is intended to take a collection
of Markdown files and a .tex template file (which holds all of your formatting
instructions) and translate and combine them into one PDF document.

Ultimately I hope to expand this, using the power of Pandoc, to be able to
output various types of documents such as webpages and presentations from the
same set of source files (for situations when it is desirable to have one
document in multiple formats; if you want the same _information_ in various
formats, its probably better to generate different sets of sources).

### Setting Up MakeDoc
First you need to have these programs installed:

 1.	GNU Make
 2. Pandoc
 3. GNU M4 (For macro support)
 4. pdflatex (I recommend the TeXLive installation)

It's probably good practice to use Git on any project large enough to warrant
this makefile, but if you're not using Git on your project, go ahead and clone
this repository into your project directory. Otherwise, add this repo as a
submodule.

You may, also, just download the makefile from this repo. I recommend cloning
(or submoduling) this repo, though, so you can get the latest changes.

After you have the Makefile, simply change the "template" variable at the top to
point to the template .tex file in your project.

### Using MakeDoc

Using the MakeDoc file (should) be easy. Create a directory for your project
and make sure the makefile (or a symbolic link to the makefile) is in your
project directory. Create a LaTeX file for your formatting (will include some
basic formats eventually). By default, this file is called "main.tex" (this
can be changed with the "TeXtemplate" varable near the top of the makefile).

Then create .txt files for each section (or chapter) of your document. Be sure
these are included in the template file with \include or \input commands. I do
plan to streamline this process eventually.

If you want to use macros in your file, save it as a .m4md file and add
"include(\`main.m4')" at the beginning of the file (NOTE: if you change the
name of the template file, you will need to use that name instead of main).
Then save your macros in a file called "main.tex.m4". This might seem overly
complex right now, but this is done to support different macro sets in the
future.

When you are ready to compile your document, just open a terminal, navigate to
your project directory and type "make".

### Contribution Guidelines
I am always open to comments and suggestions, but I am unlikely to acknowledge
pull requests for this repository, unless it is a very significant change.

### Contact Information
This repo is a project of Robert Hawk, who may be contacted for questions or
comment at robert@the-hawk.us
