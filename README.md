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

### How do I get set up?
First you need to have these programs installed:

 1.	GNU Make
 2. Pandoc
 3. GNU M4 (For macro replacement support later)
 4. pdflatex (I recommend the TeXLive installation)

It's probably good practice to use Git on any project large enough to warrant
this makefile, but if you're not using Git on your project, go ahead and clone
this repository into your project directory. Otherwise, add this repo as a
submodule.

You may, also, just download the makefile from this repo. I recommend cloning
(or submoduling) this repo, though, so you can get the latest changes.

After you have the Makefile, simply change the "template" variable at the top to
point to the template .tex file in your project.

### Contribution Guidelines
I am always open to comments and suggestions, but I am unlikely to acknowledge
pull requests for this repository, unless it is a very significant change.

### Who do I talk to?
This repo is a project of Robert Hawk, who may be contacted for questions or
comment at robert@the-hawk.us
