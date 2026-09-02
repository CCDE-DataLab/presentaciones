# CCDE — Materiales y Presentaciones Académicas
### Círculo de Ciencia de Datos y Econometría

Repositorio oficial con las presentaciones, artículos, código fuente en LaTeX (Beamer) y scripts interactivos en Python desarrollados para las sesiones del **Círculo de Ciencia de Datos y Econometría (CCDE)**.

---

## 📑 Contenido del Repositorio

```
CCDE/
├── Arboles de Decisión/
│   ├── presentacion-arboles-decision.pdf      # Presentación final (Diapositivas Beamer)
│   ├── presentacion-arboles-decision.tex      # Código fuente LaTeX
│   ├── codigo_demo_arboles_ensambles.py       # Script interactivo con Scikit-Learn
│   └── CCDE-logo-whatsapp-cropped.png         # Logo institucional
│
├── Ciencia de Datos vs Econometría/
│   ├── presentacion-ciencia-datos-econometria.pdf # Diapositivas de la ponencia
│   ├── presentacion-ciencia-datos-econometria.tex # Código fuente Beamer
│   ├── Ciencia de datos y econometría.pdf         # Artículo / Paper base
│   ├── main (2).tex                               # Código fuente del artículo
│   ├── deep-research-report.md                    # Reporte de investigación y marco teórico
│   └── CCDE logotipo.*                            # Recursos gráficos (SVG / PNG)
│
├── .gitignore
└── README.md
```

---

## 🎯 Módulos y Sesiones

### 1. Árboles de Decisión y Métodos de Ensamble
* **Ubicación:** `Arboles de Decisión/`
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
* **Ubicación:** `Ciencia de Datos vs Econometría/`
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

## 💻 Requisitos y Entorno

### Ejecución de código Python
Para correr los scripts de demostración:
```bash
pip install numpy pandas scikit-learn matplotlib
python "Arboles de Decisión/codigo_demo_arboles_ensambles.py"
```

### Compilación de Diapositivas LaTeX (Beamer)
Se requiere una distribución LaTeX como **TeX Live** o **MiKTeX** con los paquetes:
`beamer`, `tikz`, `tcolorbox`, `booktabs`, `ragged2e`.
Compilar usando:
```bash
pdflatex presentacion-arboles-decision.tex
pdflatex presentacion-ciencia-datos-econometria.tex
```

---

## 🏛️ Círculo de Ciencia de Datos y Econometría (CCDE)
*Material desarrollado con fines educativos y de divulgación académica.*
