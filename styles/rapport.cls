\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{rapport}[2014/10/08]

\LoadClass[pdftex,11pt,a4paper,twoside]{report}
\RequirePackage{etex}
\RequirePackage[a4paper,vdivide={*,22cm,4cm}]{geometry}

\usepackage[Bjornstrup]{fncychap}

\makeatletter
  \renewcommand{\DOCH}{%
    \settowidth{\py}{\CNoV\thechapter}%
    \addtolength{\py}{-10pt}%     % Amount of space by which the
%                                  % number is shifted right
    \fboxsep=0pt%
    \colorbox[gray]{.85}{\rule{0pt}{40pt}\parbox[b]{\textwidth}{\hfill}}%
\kern-\myhi
    \kern-\py\raise20pt%
    \hbox{\color[gray]{.5}\CNoV\thechapter}%
%\kern-\myhi
\\%
  }
\makeatother
\oddsidemargin 5mm
\evensidemargin 5mm
\topmargin 0mm
\headheight 0mm
\textheight 225mm


\RequirePackage[usenames, dvipsnames]{xcolor}

\RequirePackage{makeidx} % creation d'index
\RequirePackage[english,french]{babel} % style francais
% pas d'espace automatiques avant les signes de ponctuation doubles !
\NoAutoSpaceBeforeFDP

% graphicx avec la bonne option, le chemin des images 
% et les types d'images valides
\RequirePackage[pdftex]{graphicx}
\graphicspath{{pdfs/}{pngs/}{imgs/}}
\DeclareGraphicsExtensions{.pdf,.png,.mps}
\RequirePackage{array}
\RequirePackage{colortbl}
\RequirePackage{adjustbox}
\RequirePackage{paralist}

% Al�lioration de la gestion des couleurs du pdf
\pdfpageattr {/Group << /S /Transparency /I true /CS /DeviceRGB>>}

\makeatletter
\newcommand\frontmatter{%
    \cleardoublepage
  %\@mainmatterfalse
  \pagenumbering{roman}}

\newcommand\mainmatter{%
    \cleardoublepage
 % \@mainmattertrue
  \pagenumbering{arabic}}

\newcommand\backmatter{%
  \if@openright
    \cleardoublepage
  \else
    \clearpage
  \fi
 % \@mainmatterfalse
   }
\makeatother

\RequirePackage{amsmath,amssymb,amsthm,euscript}
% page de garde
\RequirePackage{pageGardeEnsta}

\RequirePackage{microtype} % Micro ajustement des espacements

\RequirePackage{tabularx}
\RequirePackage{eurosym} % pour le symbole euro
\RequirePackage{float}
\RequirePackage{multicol}

\RequirePackage{tipa}

\RequirePackage{pgf,tikz}
\usetikzlibrary{automata,shapes,plotmarks,chains,positioning,shadows,arrows,trees,calc,matrix}

\RequirePackage{tikz-3dplot}

% aeguill correspond a ea plus les guillemets francais
% \RequirePackage{lmodern}
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}

\RequirePackage[hyphens]{url}
\urlstyle{same}
\RequirePackage[pdftex,backref=page]{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=black,
  filecolor=black,
  citecolor = black,      
  urlcolor=cyan,
}

\RequirePackage[acronymlists={glo},toc]{glossaries} % glossaires
\newglossary{glo}{acr1}{acn1}{Glossaire}
%\newglossary{gloen}{acr2}{acn2}{English glossary}

% Landscape figures
\usepackage{rotating}
\usepackage{float}
\usepackage{subcaption}

\RequirePackage[ruled,vlined, french]{algorithm2e}
\RequirePackage{algorithmic}

\RequirePackage{pgfplots}
\pgfplotsset{compat=1.15}
\RequirePackage[simplified]{pgf-umlcd}

\usepackage{pifont}% http://ctan.org/pkg/pifont
\newcommand{\cmark}{\color{ForestGreen}\ding{51}}%
\newcommand{\xmark}{\color{Red}\ding{55}}%

\RequirePackage{longtable,booktabs}

\unitlength 1cm

\def\nbR{\mathbb{R}}
\def\nbN{\mathbb{N}}
\def\nbQ{\mathbb{Q}}
\def\nbZ{\mathbb{Z}}



\theoremstyle{plain}
\newtheorem{theo}{Th�or�me}
\newtheorem{theoreme}{Th�or�me}
\newtheorem{lemme}{Lemme}
\newtheorem{corollaire}{Corollaire}
\newtheorem*{iremarque}{Remarque}
\newtheorem*{iremarques}{Remarques}
\theoremstyle{definition}
\newtheorem{defi}{Définition}
\theoremstyle{remark}
\newtheorem{exemple}{Exemple}
\newtheorem{exemples}{Exemples}
\newtheorem*{remarque}{Remarque}
\newtheorem*{remarques}{Remarques}
\newtheorem{prop}{Propriété}
\newtheorem*{prop*}{Propriétés}


\RequirePackage{ifthen}
