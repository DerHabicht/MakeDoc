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
'''  # nopep8

IDD_MAIN = r'''
\documentclass{book}

\usepackage[hidelinks,pdfusetitle]{hyperref}
\usepackage{bookmark}
\usepackage{fancyhdr}
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
