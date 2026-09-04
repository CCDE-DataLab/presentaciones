# K-Nearest Neighbors (KNN) — CCDE

Material oficial de la sesión del **Círculo de Ciencia de Datos y Econometría (CCDE)** sobre K-Nearest Neighbors (KNN).

## Archivos

- `presentacion-knn.tex`: presentación Beamer 16:9 con la identidad visual institucional CCDE (portada idéntica a SVM y Árboles de Decisión).
- `sections/`: secciones modulares de la presentación para facilitar mantenimiento y edición por bloques temáticos.
  - `01-fundamentos-intuicion.tex`: aprendizaje basado en instancias, lazy learning y contraste paramétrico vs. no paramétrico.
  - `02-formulacion-matematica.tex`: reglas de decisión en clasificación y regresión, probabilidad a posteriori y cota de Cover-Hart.
  - `03-metricas-geometria.tex`: distancias Minkowski ($L_1$, $L_2$, $L_\infty$), Hamming y geometría de bolas unitarias en 2D.
  - `04-escalamiento-hiperparametros.tex`: necesidad del escalamiento, trade-off sesgo--varianza y regiones de decisión vs. $k$.
  - `05-maldicion-dimensionalidad.tex`: fenómeno del hipervolumen vacío, estructuras de indexación (Brute, KD-Tree, Ball-Tree) y balance metodológico.
  - `06-aplicacion-python.tex`: Pipeline con Scikit-Learn, optimización con GridSearchCV y evaluación en Breast Cancer Wisconsin.
  - `07-cierre-fuentes.tex`: síntesis conceptual y referencias bibliográficas rigurosas.
- `codigo_demo_knn.py`: script reproducible en Python con paleta institucional CCDE; genera las métricas numéricas y las figuras utilizadas por las diapositivas.
- `fig_knn_regions.png`: regiones de decisión de KNN ($k=1, 5, 15$) generadas por el script.
- `fig_distancias_knn.png`: bolas unitarias de distancias Manhattan, Euclidiana y Chebyshev generadas por el script.
- `resultados_knn.txt`: reporte numérico de la validación cruzada y evaluación en test.
- `CCDE-logo-whatsapp-cropped.png`: logotipo oficial institucional del CCDE.
- `presentacion-knn.pdf`: presentación Beamer final compilada y validada visualmente.

## Reproducir localmente

Desde esta carpeta (`KNN`):

```bash
pip install numpy matplotlib scikit-learn
python codigo_demo_knn.py
pdflatex presentacion-knn.tex
pdflatex presentacion-knn.tex
```

> **Nota:** El script debe ejecutarse antes de compilar para generar las figuras PNG y el archivo de resultados. El logo institucional se incluye localmente y dispone de fallbacks a carpetas hermanas del repositorio.

## Bibliografía base

- **James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013).** *An Introduction to Statistical Learning with Applications in R*. Springer. Capítulos 2 y 4.
- **Hastie, T., Tibshirani, R., & Friedman, J. (2009).** *The Elements of Statistical Learning* (2.ª ed.). Springer. Capítulos 2 y 13.
- **Géron, A. (2022).** *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3.ª ed.). O'Reilly Media. Capítulo 3.
- **Cover, T., & Hart, P. (1967).** *Nearest neighbor pattern classification*. IEEE Transactions on Information Theory, 13(1), 21–27.
