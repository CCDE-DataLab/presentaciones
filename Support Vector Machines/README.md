# Support Vector Machines (SVM) — CCDE

Material de la sesión del **Círculo de Ciencia de Datos y Econometría (CCDE)** sobre Support Vector Machines.

## Archivos

- `presentacion-svm.tex`: presentación Beamer 16:9 con la identidad visual CCDE.
- `sections/`: secciones modulares de la presentación para facilitar correcciones.
- `codigo_demo_svm.py`: demo reproducible en Python; genera métricas y las figuras usadas por las diapositivas.
- `fig_svm_hard_soft.png`: se genera al ejecutar el script.
- `fig_svm_kernel_moons.png`: se genera al ejecutar el script.
- `fig_svm_gamma.png`: se genera al ejecutar el script.
- `presentacion-svm.pdf`: salida compilada localmente (puede regenerarse desde el `.tex`).

## Contenido

La presentación cubre geometría del hiperplano, margen máximo, hard margin, soft margin, formulación primal y dual, support vectors, cambio de dimensionalidad, kernel trick, kernels lineal/polinómico/RBF/sigmoid, papel de `C` y `gamma`, principales hiperparámetros de `sklearn.svm.SVC`, ventajas/desventajas y una aplicación reproducible en Python.

## Reproducir localmente

Desde esta carpeta:

```bash
pip install numpy matplotlib scikit-learn
python codigo_demo_svm.py
pdflatex presentacion-svm.tex
pdflatex presentacion-svm.tex
```

El script debe ejecutarse antes de compilar si se quieren insertar las tres figuras generadas. El logo se reutiliza desde `../Arboles de Decisión/CCDE-logo-whatsapp-cropped.png`; si no está disponible, la presentación igualmente compila sin el logo.

## Bibliografía base

- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*, 3.ª ed., cap. 5.
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning with Applications in R*, cap. 9.
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*, 2.ª ed., cap. 12.
