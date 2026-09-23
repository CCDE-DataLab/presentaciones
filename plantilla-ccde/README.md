# plantilla-ccde — Plantilla canónica Beamer (sin fecha)

El diseño único del repo vive en **`assets/ccde-beamer.sty`**. Basado en la
versión más pulida (**knn**): mismos colores, tipografías, pie, portada y
componentes (`ccdebox`, `keybox`, `contrastbox`, `source`, `sourceright`,
`tagpill`, `refentry`, estilo `ccdepython`).

## Regla anti-hardcodeo

- **Prohibido `\date{...}` con texto.** Usar siempre `\date{}` (ya viene en `ccde-beamer.sty`).
- **Prohibida la fecha en portada.** Usar `\ccdeportada{Título}{Subtítulo}{Sigla}`.
- **No rutas absolutas.** Logo centralizado en `assets/` (ver `\ccdelogofile`
  en el `.sty`); si se reutiliza otro, usar ruta **relativa** vía `\renewcommand{\ccdelogofile}{...}`.
- **No duplicar el preámbulo.** Todo el diseño vive en `assets/ccde-beamer.sty`.
  Cada presentación solo define `\ccdefootlabel`, `\title`, `\subtitle`, `\author`.
- **Parámetros ML en Python** (`random_state`, `test_size`, `k`) van como constantes
  nombradas (`RANDOM_STATE = 42`), nunca como literales sueltos ni rutas `C:\`.

## Uso

```latex
\documentclass[aspectratio=169,11pt,table]{beamer}
\usepackage{../assets/ccde-beamer}
\renewcommand{\ccdefootlabel}{CCDE -- Mi Tema}
\title{Mi Tema}
\subtitle{Descripción corta}
\author{Círculo de Ciencia de Datos y Econometría}
\date{}
\begin{document}
\ccdeportada{Mi Tema}{Descripción corta}{MT}
% ... secciones ...
\end{document}
```

Compilar:

```bash
cd plantilla-ccde
pdflatex presentacion-plantilla.tex
pdflatex presentacion-plantilla.tex
```

## Diferencias incorporadas desde KNN (vs. versiones viejas)

- `amsmath,amssymb` + librería TikZ `decorations.pathreplacing`.
- Color extra `purplex`.
- `\source` / `\sourceright` en overlay (no empujan el layout).
- Logo con fallback (círculo con sigla) para compilar sin el PNG.
- Pie sin fecha: solo etiqueta + logo + `framenumber/total`.
