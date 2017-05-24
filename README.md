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

There are three options for setting up this makefile.

 1. Download the makefile from the repo into your project directory.
 2. Clone this repo into your project directory. If your project is in Git
 (and, if it's complicated enough that this makefile makes sense, then your
 project should probably be in Git), add this repo as a submodule. Then symlink
 the makefile to your main project directory.
 3. Clone the repo somewhere centralish on your system and symlink the makefile
 to any/all projects that might need it.

I personally do #3. By default, the makefile is going to look for an
environment variable called "template." In each of the projects I use this
makefile in, I will create a .makedoc file that looks something like:

~~~~
export template=foo
~~~~

I will then source .makedoc before invoking make in that directory.

This isn't always the best approach and can be problematic in some cases. You
can always set the template variable At the top of the makefile if you have
trouble getting the template file name from the environment.

NOTE: When setting the template variable, DO NOT include the file extension.
The makefile appends extensions for various purposes throughout its execution.

### Using MakeDoc

Using the MakeDoc file (should) be easy. Create a directory for your project
and make sure the makefile (or a symbolic link to the makefile) is in your
project directory. Create a LaTeX file for your formatting (will include some
basic formats eventually). By default, this file is called "main.tex" (this
can be changed with the "TeXtemplate" varable near the top of the makefile).

Then create .md files for each section (or chapter) of your document. Be sure
these are included in the template file with \include or \input commands. I do
plan to streamline this process eventually.

If you want to use macros in your file, save it as a .m4md file and add
"include(\`main.m4')" at the beginning of the file (NOTE: if you change the
name of the template file, you will need to use that name instead of main).
Then save your macros in a file called "main.tex.m4". This might seem overly
complex right now, but this is done to support different macro sets in the
future.

When you are ready to compile your document, just open a terminal, navigate to
your project directory and type:

~~~~
source .makedoc
make
~~~~

If you set template at the top of the makefile, or you've already sourced
.makedoc in your current terminal, then you can skip that step.

### Contribution Guidelines
I am always open to comments and suggestions, but I am unlikely to acknowledge
pull requests for this repository, unless it is a very significant change.

### Contact Information
This repo is a project of Robert Hawk, who may be contacted for questions or
comments at robert.hawk@the-hawk.us
