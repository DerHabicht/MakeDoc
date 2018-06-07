IDD_MAKEFILE = r'''
%%%SHORT_NAME%%%.pdf: *.tex */*.tex
	lualatex %%%SHORT_NAME%%%.tex
	lualatex %%%SHORT_NAME%%%.tex

.PHONY: clean
clean:
	rm -f *.pdf
	rm -f *.aux
	rm -f *.log
	rm -f *.docx
	rm -f *.pdf
	rm -f *.hst
	rm -f *.ver
	rm -f *.bbl
	rm -f *.bcf
	rm -f *.blg
	rm -f *.glg
	rm -f *.glo
	rm -f *.gls
	rm -f *.idx
	rm -f *.ilg
	rm -f *.ind
	rm -f *.ist
	rm -f *.out
	rm -f *.xml
	rm -f *.toc
	rm -f *.lof
	rm -f *.lot
	rm -f */*.pdf
	rm -f */*.aux
	rm -f */*.log
	rm -f */*.docx
	rm -f */*.pdf
	rm -f */*.hst
	rm -f */*.ver
	rm -f */*.bbl
	rm -f */*.bcf
	rm -f */*.blg
	rm -f */*.glg
	rm -f */*.glo
	rm -f */*.gls
	rm -f */*.idx
	rm -f */*.ilg
	rm -f */*.ind
	rm -f */*.ist
	rm -f */*.out
	rm -f */*.xml
	rm -f */*.toc
	rm -f */*.lof
	rm -f */*.lot
'''  # nopep8

IDD_MAIN = r'''
\documentclass{book}

\usepackage[hidelinks,pdfusetitle]{hyperref}
\usepackage{bookmark}
\usepackage{booktabs}
\usepackage{fancyhdr}
\usepackage{float}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{pdflscape}
\usepackage{pdfpages}
\usepackage{units}
\usepackage{vhistory}
\usepackage[capitalize]{cleveref}

\usepackage[personal]{thusinfosec}

\pagestyle{fancy}
\fancyhf{}
\chead{%%%PROJECT_NAME%%% IDD \vhCurrentVersion}
\cfoot{DRAFT}
\fancyhead[LO, RE]{\ISLevel}
\fancyhead[LE, RO]{\leftmark}
\fancyfoot[LO, RE]{\ISLevel}
\fancyfoot[LE, RO]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\renewcommand{\chaptermark}[1]{\markboth{\MakeUppercase{#1}}{}}

\fancypagestyle{plain}{%
    \fancyhf{}
    \fancyhead[LO, RE]{\ISLevel}
    \fancyfoot[LO, RE]{\ISLevel}
    \fancyfoot[LE, RO]{\thepage}
}

\fancypagestyle{nomark}{%
    \fancyhf{}
}

\title{%%%PROJECT_NAME%%% Initial Design Document}
\author{%%%AUTHOR_NAME%%%}
\date{\vhCurrentDate}

\begin{document}
\frontmatter
\ISCover{}
\maketitle
\input{vhistory}
\tableofcontents

\mainmatter{}
\input{purpose}
\input{components}

\bookmarksetupnext{level=part}
\appendix\addcontentsline{toc}{part}{Appendices}
\end{document}
'''  # nopep8

IDD_MAIN_PARTS = r'''
\part{%%%NAME%%%}
\include{%%%SHORT_NAME%%%/spec}
\include{%%%SHORT_NAME%%%/schema}
\include{%%%SHORT_NAME%%%/processes}
\include{%%%SHORT_NAME%%%/testing}

'''  # nopep8

IDD_VERSION_HISTORY = r'''
\begin{versionhistory}
    \vhEntry{0.0.0}{%%%DATE%%%}{%%%AUTHOR%%%}{Document Created}
\end{versionhistory}
'''  # nopep8

IDD_PURPOSE = r'''
\chapter{Purpose and Principles}\label{chap:purpose}
\section{Motivation}\label{chap:purpose/motivation}

\section{Project Requirements}\label{chap:purpose/requirements}

\section{Ethical Requirements}\label{chap:purpose/ethics}

'''  # nopep8

IDD_COMPONENTS = r'''
\chapter{Major System Components}\label{chap:components}
'''  # nopep8

IDD_COMPONENTS_SECTION = r'''
\section{%%%COMPONENT_NAME%%%}\label{sec:components/%%%SHORT_NAME%%%}
\subsection{Overview}\label{sec:components/%%%SHORT_NAME%%%}

\subsection{Technologies}\label{sec:components/%%%SHORT_NAME%%%}
\begin{itemize}
    \item \verb|LANGUAGE|
    \item \verb|FRAMEWORK|
    \item \verb|LIBRARIES|
\end{itemize}

'''  # nopep8

IDD_SPECIFICATION = r'''
\chapter{Functional Specification}\label{chap:%%%SHORT_NAME%%%/spec}
\section{Interface}\label{sec:%%%SHORT_NAME%%%/spec/interface}

\section{Desired Behaviors}\label{sec:%%%SHORT_NAME%%%/spec/behavior}

\section{Error Handling}\label{sec:%%%SHORT_NAME%%%/spec/errors}

'''  # nopep8

IDD_SCHEMA = r'''
\chapter{Data Schema}\label{chap:%%%SHORT_NAME%%%/schema}
'''  # nopep8

IDD_PROCESSES = r'''
\chapter{Tricky Processes and Algorithms}\label{chap:%%%SHORT_NAME%%%/processes}
'''  # nopep8

IDD_TEST_CASES = r'''
\chapter{Test Cases}\label{chap:%%%SHORT_NAME%%%/testing}
'''  # nopep8

# https://github.com/github/gitignore/blob/master/TeX.gitignore
TEX_GITIGNORE = r'''
## Core latex/pdflatex auxiliary files:
*.aux
*.lof
*.log
*.lot
*.fls
*.out
*.toc
*.fmt
*.fot
*.cb
*.cb2
.*.lb

## Intermediate documents:
*.dvi
*.xdv
*-converted-to.*
# these rules might exclude image files for figures etc.
# *.ps
# *.eps
# *.pdf

## Generated if empty string is given at Please type another file name for output:
.pdf

## Bibliography auxiliary files (bibtex/biblatex/biber):
*.bbl
*.bcf
*.blg
*-blx.aux
*-blx.bib
*.run.xml

## Build tool auxiliary files:
*.fdb_latexmk
*.synctex
*.synctex(busy)
*.synctex.gz
*.synctex.gz(busy)
*.pdfsync

## Build tool directories for auxiliary files
# latexrun
latex.out/

## Auxiliary and intermediate files from other packages:
# algorithms
*.alg
*.loa

# achemso
acs-*.bib

# amsthm
*.thm

# beamer
*.nav
*.pre
*.snm
*.vrb

# changes
*.soc

# cprotect
*.cpt

# elsarticle (documentclass of Elsevier journals)
*.spl

# endnotes
*.ent

# fixme
*.lox

# feynmf/feynmp
*.mf
*.mp
*.t[1-9]
*.t[1-9][0-9]
*.tfm

#(r)(e)ledmac/(r)(e)ledpar
*.end
*.?end
*.[1-9]
*.[1-9][0-9]
*.[1-9][0-9][0-9]
*.[1-9]R
*.[1-9][0-9]R
*.[1-9][0-9][0-9]R
*.eledsec[1-9]
*.eledsec[1-9]R
*.eledsec[1-9][0-9]
*.eledsec[1-9][0-9]R
*.eledsec[1-9][0-9][0-9]
*.eledsec[1-9][0-9][0-9]R

# glossaries
*.acn
*.acr
*.glg
*.glo
*.gls
*.glsdefs

# gnuplottex
*-gnuplottex-*

# gregoriotex
*.gaux
*.gtex

# htlatex
*.4ct
*.4tc
*.idv
*.lg
*.trc
*.xref

# hyperref
*.brf

# knitr
*-concordance.tex
# TODO Comment the next line if you want to keep your tikz graphics files
*.tikz
*-tikzDictionary

# listings
*.lol

# makeidx
*.idx
*.ilg
*.ind
*.ist

# minitoc
*.maf
*.mlf
*.mlt
*.mtc[0-9]*
*.slf[0-9]*
*.slt[0-9]*
*.stc[0-9]*

# minted
_minted*
*.pyg

# morewrites
*.mw

# nomencl
*.nlg
*.nlo
*.nls

# pax
*.pax

# pdfpcnotes
*.pdfpc

# sagetex
*.sagetex.sage
*.sagetex.py
*.sagetex.scmd

# scrwfile
*.wrt

# sympy
*.sout
*.sympy
sympy-plots-for-*.tex/

# pdfcomment
*.upa
*.upb

# pythontex
*.pytxcode
pythontex-files-*/

# thmtools
*.loe

# TikZ & PGF
*.dpth
*.md5
*.auxlock

# todonotes
*.tdo

# easy-todo
*.lod

# xmpincl
*.xmpi

# xindy
*.xdy

# xypic precompiled matrices
*.xyc

# endfloat
*.ttt
*.fff

# Latexian
TSWLatexianTemp*

## Editors:
# WinEdt
*.bak
*.sav

# Texpad
.texpadtmp

# Kile
*.backup

# KBibTeX
*~[0-9]*

# auto folder when using emacs and auctex
./auto/*
*.el

# expex forward references with \gathertags
*-tags.tex

# standalone packages
*.sta

# generated if using elsarticle.cls
*.spl

'''  # nopep8
