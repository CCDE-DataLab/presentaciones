# CCDE — Materiales y Presentaciones Académicas
### Círculo de Ciencia de Datos y Econometría

Repositorio oficial con las presentaciones, artículos, código fuente en LaTeX (Beamer) y scripts interactivos en Python desarrollados para las sesiones del **Círculo de Ciencia de Datos y Econometría (CCDE)**.

---

## 📑 Contenido del Repositorio

```
CCDE/
├── assets/
│   ├── ccde-beamer.sty                  # Plantilla canónica (única fuente de diseño Beamer)
│   └── CCDE-logo-whatsapp-cropped.png   # Logo institucional (copia única)
│
├── arboles-decision/
│   ├── presentacion-arboles-decision.pdf # Presentación final (Diapositivas Beamer)
│   ├── presentacion-arboles-decision.tex # Código fuente (usa ../assets/ccde-beamer)
│   └── codigo_demo_arboles_ensambles.py  # Script interactivo con Scikit-Learn
│
├── ciencia-datos-econometria/
│   ├── presentacion-ciencia-datos-econometria.pdf # Diapositivas de la ponencia
│   ├── presentacion-ciencia-datos-econometria.tex # Código fuente Beamer
│   ├── Ciencia de datos y econometría.pdf         # Artículo / Paper base
│   ├── articulo-ciencia-datos-econometria.tex     # Código fuente del artículo
│   ├── deep-research-report.md                    # Reporte de investigación y marco teórico
│   └── foto-sesion-julio-2026.jpeg                # Foto de la sesión
│
├── svm/
│   ├── presentacion-svm.tex              # Archivo maestro Beamer
│   ├── sections/                         # Secciones modulares para edición
│   ├── codigo_demo_svm.py                # Demo reproducible + figuras
│   ├── fig_svm_*.png                     # Figuras generadas por el script
│   └── README.md                         # Guía de compilación y fuentes
│
├── knn/
│   ├── presentacion-knn.pdf              # Diapositivas finales compiladas (18 láminas)
│   ├── presentacion-knn.tex              # Archivo maestro Beamer (16:9)
│   ├── sections/                         # 7 secciones modulares en LaTeX
│   ├── codigo_demo_knn.py                # Demo reproducible con scikit-learn + figuras
│   ├── fig_knn_regions.png / fig_distancias_knn.png # Figuras generadas por el script
│   ├── resultados_knn.txt                # Métricas reproducibles
│   └── README.md                         # Guía y ficha técnica del módulo
│
├── plantilla-ccde/
│   ├── presentacion-plantilla.tex        # Ejemplo mínimo de uso de la plantilla
│   ├── presentacion-plantilla.pdf        # Ejemplo compilado
│   └── README.md                         # Norma anti-hardcodeo y guía de uso
│
├── .github/workflows/build-pdfs.yml      # CI: regenera figuras y PDFs en cada push
├── .gitattributes                        # Normalización LF y binarios
├── .gitignore
└── README.md
```

---

## 🎯 Módulos y Sesiones

### 1. Árboles de Decisión y Métodos de Ensamble
* **Ubicación:** `arboles-decision/`
* **Temas abordados:**
  * Algoritmo CART (Clasificación y Regresión), función de costo y complejidad computacional.
  * Criterios de división: Impureza de Gini vs. Entropía.
  * Regularización e hiperparámetros (`max_depth`, `min_samples_split`, `min_samples_leaf`, `max_leaf_nodes`).
  * Sensibilidad a rotación de ejes e inestabilidad/alta varianza de árboles individuales.
  * Métodos de Ensamble: Bagging, estimación Out-of-Bag (OOB) e importancia de características.
  * Random Forests y Boosting (Gradient Boosting / AdaBoost).
  * **Demostración práctica:** `codigo_demo_arboles_ensambles.py` con datasets de Scikit-Learn.

#### 📚 Referencias Bibliográficas Base:
* **Géron, A. (2022).** *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3.ª ed.). O'Reilly Media. (Capítulo 6: *Decision Trees*).
* **James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013).** *An Introduction to Statistical Learning with Applications in R*. Springer. (Capítulo 8: *Tree-Based Methods*).
* **Breiman, L. (1996).** *Bagging Predictors*. Machine Learning, 24, 123–140.
* **Breiman, L. (2001).** *Random Forests*. Machine Learning, 45, 5–32.

---

### 2. Ciencia de Datos vs. Econometría: Convergencias, Divergencias y Causalidad
* **Ubicación:** `ciencia-datos-econometria/`
* **Temas abordados:**
  * **Econometría:** Identificación causal, inferencia estadística creíble, diseño de investigación y validez interna.
  * **Ciencia de Datos:** Predicción flexible out-of-sample, minimización del error empírico, escalabilidad y CRISP-DM.
  * **El puente moderno:** Aprendizaje automático causal (*Causal ML*), *Double/Debiased Machine Learning* (DML), efectos de tratamiento heterogéneos (HTE).
  * **Riesgos y Gobernanza:** Sesgo algorítmico, interpretabilidad vs. explicabilidad (*black box* vs. modelos inherentemente interpretables) y marcos de riesgo (NIST AI RMF).

#### 📚 Referencias Bibliográficas Base:
* **Shmueli, G. (2010).** *To Explain or to Predict?* Statistical Science, 25(3), 289–310.
* **Breiman, L. (2001).** *Statistical Modeling: The Two Cultures*. Statistical Science, 16(3), 199–231.
* **Mullainathan, S., & Spiess, J. (2017).** *Machine Learning: An Applied Econometric Approach*. Journal of Economic Perspectives, 31(2), 87–106.
* **Chernozhukov, V. et al. (2018).** *Double/debiased machine learning for treatment and structural parameters*. The Econometrics Journal, 21(1), C1–C68.
* **Athey, S., & Imbens, G. W. (2019).** *Machine Learning Methods That Economists Should Know About*. Annual Review of Economics, 11, 685–725.
* **Rudin, C. (2019).** *Stop explaining black box machine learning models for high-stakes decisions and use interpretable models instead*. Nature Machine Intelligence, 1(5), 206–215.
* **Lechner, M. (2023).** *Causal Machine Learning and its Use for Public Policy*. Swiss Journal of Economics and Statistics, 159(1), 1–17.
* **Donoho, D. (2017).** *50 Years of Data Science*. Journal of Computational and Graphical Statistics, 26(4), 745–766.
* **NIST (2023).** *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. National Institute of Standards and Technology.

---

### 3. Support Vector Machines (SVM)
* **Ubicación:** `svm/`
* **Temas abordados:**
  * Geometría del hiperplano y principio de margen máximo.
  * Hard margin y soft margin con variables de holgura.
  * Formulación primal y dual; papel de los support vectors.
  * Hiperparámetro `C` y trade-off sesgo-varianza.
  * Kernel trick, cambio de dimensionalidad y matriz de Gram.
  * Kernels lineal, polinómico, RBF/Gaussiano y sigmoide.
  * Hiperparámetros `gamma`, `degree`, `coef0` y `class_weight`.
  * Escalamiento con `StandardScaler`, `Pipeline` y ajuste mediante `GridSearchCV`.
  * **Demostración práctica:** `codigo_demo_svm.py`, que compara SVM lineal vs. RBF y genera las figuras de la presentación.

#### 📚 Referencias Bibliográficas Base:
* **Géron, A. (2022).** *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3.ª ed.). O'Reilly Media. (Capítulo 5: *Support Vector Machines*).
* **James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013).** *An Introduction to Statistical Learning with Applications in R*. Springer. (Capítulo 9: *Support Vector Machines*).
* **Hastie, T., Tibshirani, R., & Friedman, J. (2009).** *The Elements of Statistical Learning* (2.ª ed.). Springer. (Capítulo 12: *Support Vector Machines and Flexible Discriminants*).

---

### 4. K-Nearest Neighbors (KNN)
* **Ubicación:** `knn/`
* **Temas abordados:**
  * Fundamentos del aprendizaje perezoso (*lazy learning*) y modelos basados en instancias.
  * Regla de decisión de mayoría, votación ponderada y KNN para regresión (media local y Nadaraya-Watson).
  * Métricas de distancia (Euclidiana, Manhattan, Minkowski, Mahalanobis y Cosine).
  * Sensibilidad crítica a la escala y estandarización con `StandardScaler` en `Pipeline`.
  * Trade-off sesgo-varianza según $k$ y tasa de error asintótica frente al clasificador Bayesiano ($R^* \le R \le 2R^*$).
  * Maldición de la dimensionalidad: concentración de medidas, hipercubos y degradación de la distancia.
  * Implementación reproducible en Python con `KNeighborsClassifier` y optimización con `GridSearchCV`.
  * **Demostración práctica:** `codigo_demo_knn.py` (Breast Cancer Wisconsin, $k=15$, distancia ponderada).

#### 📚 Referencias Bibliográficas Base:
* **James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013).** *An Introduction to Statistical Learning with Applications in R*. Springer. (Capítulos 2 y 4).
* **Hastie, T., Tibshirani, R., & Friedman, J. (2009).** *The Elements of Statistical Learning* (2.ª ed.). Springer. (Capítulos 2, 6 y 13).
* **Géron, A. (2022).** *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3.ª ed.). O'Reilly Media. (Capítulo 3).
* **Cover, T., & Hart, P. (1967).** *Nearest neighbor pattern classification*. IEEE Transactions on Information Theory, 13(1), 21–27.

---

## 💻 Requisitos y Entorno

### Ejecución de código Python
Para correr los scripts de demostración:
```bash
pip install numpy pandas scikit-learn matplotlib
python "arboles-decision/codigo_demo_arboles_ensambles.py"
python "svm/codigo_demo_svm.py"
python "knn/codigo_demo_knn.py"
```

### Compilación de Diapositivas LaTeX (Beamer)
Se requiere una distribución LaTeX como **TeX Live** o **MiKTeX** con los paquetes:
`beamer`, `tikz`, `tcolorbox`, `booktabs`, `ragged2e`.
Compilar usando:
```bash
cd arboles-decision
pdflatex presentacion-arboles-decision.tex
pdflatex presentacion-arboles-decision.tex
cd ../ciencia-datos-econometria
pdflatex presentacion-ciencia-datos-econometria.tex
pdflatex presentacion-ciencia-datos-econometria.tex
cd ../svm
python codigo_demo_svm.py   # genera fig_svm_*.png (obligatorio antes de compilar)
pdflatex presentacion-svm.tex
pdflatex presentacion-svm.tex
cd ../knn
python codigo_demo_knn.py   # genera fig_knn_*.png y resultados_knn.txt
pdflatex presentacion-knn.tex
pdflatex presentacion-knn.tex
cd ../plantilla-ccde
pdflatex presentacion-plantilla.tex
pdflatex presentacion-plantilla.tex
```

> **Nota:** Todas las presentaciones usan la plantilla canónica `assets/ccde-beamer.sty` (sin fecha, logo centralizado en `assets/`). Para crear una presentación nueva, partir de `plantilla-ccde/` (ver su `README.md`). La CI (`.github/workflows/build-pdfs.yml`) regenera figuras y PDFs automáticamente en cada push a `main`.

---

## 🏛️ Círculo de Ciencia de Datos y Econometría (CCDE)
*Material desarrollado con fines educativos y de divulgación académica.*
