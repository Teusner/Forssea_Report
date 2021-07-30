\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{rapport}[2014/10/08]

\LoadClass[pdftex,11pt,a4paper,twoside,openright]{report}

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
\graphicspath{{pdfs/}{pngs/}{imgs/}{build/gantt/}{build/imgs/}}
\DeclareGraphicsExtensions{.pdf,.png,.mps}
\usepackage{svg}
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
\RequirePackage{stmaryrd}
\RequirePackage{nicematrix}

\newcommand\inputpgf[2]{{
  \let\pgfimageWithoutPath\pgfimage
  \renewcommand{\pgfimage}[2][]{\pgfimageWithoutPath[##1]{#1/##2}}
  \input{#1/#2}
}}


\RequirePackage{tipa}

\RequirePackage{pgf,tikz}
\usetikzlibrary{automata,shapes,plotmarks,chains,positioning,shadows,arrows,trees,calc,matrix,arrows.meta}

\RequirePackage{tikz-3dplot}

% aeguill correspond a ea plus les guillemets francais
% \RequirePackage{lmodern}
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}

\RequirePackage[hyphens]{url}
\urlstyle{same}
\RequirePackage[pdftex,backref=page]{hyperref}
\hypersetup{
  colorlinks=false,
  linkbordercolor = black,
  filebordercolor = black,
  citebordercolor = YellowOrange,
  urlbordercolor = RoyalBlue,
}

\RequirePackage[acronymlists={glo},toc]{glossaries} % glossaires
\newglossary{glo}{acr1}{acn1}{Glossaire}
%\newglossary{gloen}{acr2}{acn2}{English glossary}

% Landscape figures
\RequirePackage{rotating}
\RequirePackage{float}
\RequirePackage{subcaption}

\RequirePackage{enumitem}

\RequirePackage[ruled,vlined, french]{algorithm2e}
\RequirePackage{algorithmic}
\RequirePackage[outputdir=build]{minted}

\RequirePackage{pgfplots}
\pgfplotsset{compat=1.15}
\RequirePackage[simplified]{pgf-umlcd}

\usepackage{pifont}% http://ctan.org/pkg/pifont
\newcommand{\cmark}{\textcolor{ForestGreen}{\ding{51}}}%
\newcommand{\xmark}{\textcolor{Red}{\ding{55}}}%
\newcommand{\pmark}{\textcolor{NavyBlue}{\ding{118}}}% 93 118

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

\RequirePackage{forsseamacro}

\RequirePackage{fancyhdr}
\pagestyle{fancy}

\setcounter{secnumdepth}{5}
\setcounter{tocdepth}{5}

\makeatletter
\newcommand\subsubsubsection{\@startsection{paragraph}{4}{\z@}{-2.5ex\@plus -1ex \@minus -.25ex}{1.25ex \@plus .25ex}{\normalfont\normalsize\bfseries}}
\newcommand\subsubsubsubsection{\@startsection{subparagraph}{5}{\z@}{-2.5ex\@plus -1ex \@minus -.25ex}{1.25ex \@plus .25ex}{\normalfont\normalsize\bfseries}}
\makeatother

\newcommand*\cleartoleftpage{%
  \clearpage
  \ifodd\value{page}\hbox{}\newpage\fi
}

\makeatletter
\tikzoption{canvas is xy plane at z}[]{%
  \def\tikz@plane@origin{\pgfpointxyz{0}{0}{#1}}%
  \def\tikz@plane@x{\pgfpointxyz{1}{0}{#1}}%
  \def\tikz@plane@y{\pgfpointxyz{0}{1}{#1}}%
  \tikz@canvas@is@plane
}
\makeatother

% 3D Arrows
\pgfkeys{
  /pgf/arrow keys/.cd,
  pitch/.code={%
    \pgfmathsetmacro\pgfarrowpitch{#1}
    \pgfmathsetmacro\pgfarrowsinpitch{abs(sin(\pgfarrowpitch))}
    \pgfmathsetmacro\pgfarrowcospitch{abs(cos(\pgfarrowpitch))}
  },
}

\pgfdeclarearrow{
  name = Cone,
  defaults = {       % inherit from Kite
    length     = +3.6pt +5.4,
    width'     = +0pt +0.5,
    line width = +0pt 1 1,
    pitch      = +0, % lie on screen
  },
  cache = false,     % no need cache
  setup code = {},   % so no need setup
  drawing code = {   % but still need math
    % draw the base
    \pgfmathsetmacro\pgfarrowhalfwidth{.5\pgfarrowwidth}
    \pgfmathsetmacro\pgfarrowhalfwidthsin{\pgfarrowhalfwidth*\pgfarrowsinpitch}
    \pgfpathellipse{\pgfpointorigin}{\pgfqpoint{\pgfarrowhalfwidthsin pt}{0pt}}{\pgfqpoint{0pt}{\pgfarrowhalfwidth pt}}
    \pgfusepath{fill}
    % test if the cone part visible
    \pgfmathsetmacro\pgfarrowlengthcos{\pgfarrowlength*\pgfarrowcospitch}
    \pgfmathparse{\pgfarrowlengthcos>\pgfarrowhalfwidthsin}
    \ifnum\pgfmathresult=1
      % it is visible, so draw
      \pgfmathsetmacro\pgfarrowlengthtemp{\pgfarrowhalfwidthsin*\pgfarrowhalfwidthsin/\pgfarrowlengthcos}
      \pgfmathsetmacro\pgfarrowwidthtemp{\pgfarrowhalfwidth/\pgfarrowlengthcos*sqrt(\pgfarrowlengthcos*\pgfarrowlengthcos-\pgfarrowhalfwidthsin*\pgfarrowhalfwidthsin)}
      \pgfpathmoveto{\pgfqpoint{\pgfarrowlengthcos pt}{0pt}}
      \pgfpathlineto{\pgfqpoint{\pgfarrowlengthtemp pt}{ \pgfarrowwidthtemp pt}}
      \pgfpathlineto{\pgfqpoint{\pgfarrowlengthtemp pt}{-\pgfarrowwidthtemp pt}}
      \pgfpathclose
      \pgfusepath{fill}
    \fi
    \pgfpathmoveto{\pgfpointorigin}
  }
}