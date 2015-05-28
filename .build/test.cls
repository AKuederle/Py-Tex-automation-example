\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{test}
\LoadClass[12pt,a4paper]{article}

\RequirePackage[left=2.5cm,right=2.5cm,top=3.5cm,bottom=3.5cm]{geometry}
\RequirePackage[ngerman]{babel}
\RequirePackage[T1]{fontenc}
\RequirePackage[latin1]{inputenc}

\let\ori@document=\document
\renewcommand{\document}{
  \ori@document  % Begin document
  \Name\\
  \Address\\
  \Notes\\
  \Contact\\
  }

\endinput