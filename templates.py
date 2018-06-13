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
    rm -f *.tdo
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
    rm -f *.bak*
'''  # nopep8

IDD_MAIN = r'''
\documentclass{book}

\usepackage{xcolor}
\usepackage[hidelinks,pdfusetitle]{hyperref}
\usepackage{bookmark}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{float}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{pdflscape}
\usepackage{pdfpages}
\usepackage{titlepic}
\usepackage[colorinlistoftodos,textsize=tiny]{todonotes}
\usepackage{units}
\usepackage{vhistory}
\usepackage[capitalize]{cleveref}

\usepackage[personal]{thusinfosec}

\colorlet{punct}{red!60!black}
\definecolor{background}{HTML}{EEEEEE}
\definecolor{delim}{RGB}{20,105,176}
\colorlet{numb}{magenta!60!black}

\lstdefinelanguage{json}{
    basicstyle=\normalfont\ttfamily,
    numbers=left,
    numberstyle=\scriptsize,
    stepnumber=1,
    numbersep=8pt,
    showstringspaces=false,
    breaklines=true,
    frame=lines,
    backgroundcolor=\color{background},
    literate=
     *{0}{{{\color{numb}0}}}{1}
      {1}{{{\color{numb}1}}}{1}
      {2}{{{\color{numb}2}}}{1}
      {3}{{{\color{numb}3}}}{1}
      {4}{{{\color{numb}4}}}{1}
      {5}{{{\color{numb}5}}}{1}
      {6}{{{\color{numb}6}}}{1}
      {7}{{{\color{numb}7}}}{1}
      {8}{{{\color{numb}8}}}{1}
      {9}{{{\color{numb}9}}}{1}
      {:}{{{\color{punct}{:}}}}{1}
      {,}{{{\color{punct}{,}}}}{1}
      {\{}{{{\color{delim}{\{}}}}{1}
      {\}}{{{\color{delim}{\}}}}}{1}
      {[}{{{\color{delim}{[}}}}{1}
      {]}{{{\color{delim}{]}}}}{1},
}

\pagestyle{fancy}
\fancyhf{}
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
\todototoc
\listoftodos
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

BARNARDS_STAR = b'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'  # nopep8
