"""Demo reproducible de K-Nearest Neighbors (KNN) para la sesión CCDE.

Genera:
- fig_knn_regions.png: Fronteras de decisión para k=1, 5, 15 en make_moons.
- fig_distancias_knn.png: Geometría de bolas unitarias para distancias L1, L2 y L-infinito.
- resultados_knn.txt: Métricas reproducibles de un Pipeline (StandardScaler + KNN) con GridSearchCV
  sobre el dataset Breast Cancer Wisconsin.

Requisitos:
    pip install numpy matplotlib scikit-learn
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_moons, load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, confusion_matrix

RANDOM_STATE = 42

# Paleta institucional CCDE
CCDE_NAVY = "#0a1e40"
CCDE_BLUE = "#22355e"
CCDE_ACCENT = "#0077b6"
CCDE_SKY = "#3d96d2"
CCDE_LIGHT = "#73c4df"
CCDE_ICE = "#ebf7fc"
CCDE_WARN = "#ca5d36"
CCDE_GREEN = "#16805f"


def save_knn_regions_figure() -> None:
    """Genera y guarda la figura con regiones de decisión para k = 1, 5, 15."""
    X, y = make_moons(n_samples=300, noise=0.22, random_state=RANDOM_STATE)
    ks = [1, 5, 15]

    fig, axes = plt.subplots(1, 3, figsize=(13, 4.2), constrained_layout=True)

    x_min, x_max = X[:, 0].min() - 0.6, X[:, 0].max() + 0.6
    y_min, y_max = X[:, 1].min() - 0.6, X[:, 1].max() + 0.6
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 400), np.linspace(y_min, y_max, 400))

    # Fondos suaves y colores de puntos institucionales
    bg_cmap = ListedColormap(["#e0f2fe", "#fee2e2"])
    pt_colors = np.array([CCDE_ACCENT, CCDE_WARN])

    for ax, k in zip(axes, ks):
        model = Pipeline([
            ("scaler", StandardScaler()),
            ("knn", KNeighborsClassifier(n_neighbors=k, weights="uniform", metric="minkowski", p=2)),
        ])
        model.fit(X, y)
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

        ax.contourf(xx, yy, Z, alpha=0.75, cmap=bg_cmap)
        ax.contour(xx, yy, Z, levels=[0.5], colors=[CCDE_NAVY], linewidths=1.2)
        ax.scatter(X[:, 0], X[:, 1], c=pt_colors[y], edgecolor="#1e293b", s=28, linewidth=0.5)

        subtitle = "Frontera quebrada (sobreajuste)" if k == 1 else ("Equilibrio sesgo-varianza" if k == 5 else "Frontera suave (regularizada)")
        ax.set_title(f"$k = {k}$\n({subtitle})", fontsize=11, fontweight="bold", color=CCDE_NAVY)
        ax.set_xlabel("$x_1$", fontsize=10, color=CCDE_NAVY)
        ax.set_ylabel("$x_2$", fontsize=10, color=CCDE_NAVY)
        ax.tick_params(colors=CCDE_NAVY)
        for spine in ax.spines.values():
            spine.set_color("#cbd5e1")

    fig.suptitle("Regiones de Decisión KNN en Función de $k$ (make_moons)", fontsize=13, fontweight="bold", color=CCDE_NAVY)
    fig.savefig("fig_knn_regions.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def save_minkowski_balls_figure() -> None:
    """Genera la comparación geométrica de bolas unitarias de distancias L1, L2 y L-inf."""
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.8), constrained_layout=True)
    t = np.linspace(0, 2 * np.pi, 600)

    # p = 1 Rombo (Manhattan)
    x1 = np.array([0, 1, 0, -1, 0])
    y1 = np.array([1, 0, -1, 0, 1])
    axes[0].plot(x1, y1, color=CCDE_ACCENT, linewidth=2)
    axes[0].fill(x1, y1, color=CCDE_LIGHT, alpha=0.35)
    axes[0].set_title("Manhattan ($L_1$, $p=1$)\n$d = |x_1| + |x_2| \\leq 1$", fontsize=10.5, color=CCDE_NAVY, fontweight="bold")

    # p = 2 Círculo (Euclidiana)
    x2 = np.cos(t)
    y2 = np.sin(t)
    axes[1].plot(x2, y2, color=CCDE_BLUE, linewidth=2)
    axes[1].fill(x2, y2, color=CCDE_SKY, alpha=0.35)
    axes[1].set_title("Euclidiana ($L_2$, $p=2$)\n$d = \\sqrt{x_1^2 + x_2^2} \\leq 1$", fontsize=10.5, color=CCDE_NAVY, fontweight="bold")

    # p = inf Cuadrado (Chebyshev)
    x3 = np.array([-1, 1, 1, -1, -1])
    y3 = np.array([-1, -1, 1, 1, -1])
    axes[2].plot(x3, y3, color=CCDE_WARN, linewidth=2)
    axes[2].fill(x3, y3, color="#fed7aa", alpha=0.35)
    axes[2].set_title("Chebyshev ($L_\\infty$, $p=\\infty$)\n$d = \\max(|x_1|, |x_2|) \\leq 1$", fontsize=10.5, color=CCDE_NAVY, fontweight="bold")

    for ax in axes:
        ax.axhline(0, color="#94a3b8", linewidth=0.8, linestyle="--")
        ax.axvline(0, color="#94a3b8", linewidth=0.8, linestyle="--")
        ax.set_xlim(-1.45, 1.45)
        ax.set_ylim(-1.45, 1.45)
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlabel("$x_1$", fontsize=10, color=CCDE_NAVY)
        ax.set_ylabel("$x_2$", fontsize=10, color=CCDE_NAVY)
        ax.grid(True, alpha=0.3, linestyle=":")
        ax.tick_params(colors=CCDE_NAVY)
        for spine in ax.spines.values():
            spine.set_color("#cbd5e1")

    fig.suptitle("Geometría de Bolas Unitarias $\\{x \\in \\mathbb{R}^2 : d(0, x) \\leq 1\\}$", fontsize=12.5, fontweight="bold", color=CCDE_NAVY)
    fig.savefig("fig_distancias_knn.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def run_real_dataset_example() -> dict:
    """Ejecuta Pipeline con StandardScaler + KNN en Breast Cancer y guarda resultados."""
    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.25, stratify=data.target, random_state=RANDOM_STATE
    )

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier()),
    ])

    param_grid = {
        "knn__n_neighbors": [3, 5, 7, 9, 11, 15],
        "knn__weights": ["uniform", "distance"],
        "knn__metric": ["minkowski"],
        "knn__p": [1, 2],
    }

    grid = GridSearchCV(pipe, param_grid=param_grid, cv=5, scoring="roc_auc", n_jobs=-1)
    grid.fit(X_train, y_train)
    best_model = grid.best_estimator_
    pred = best_model.predict(X_test)
    prob = best_model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, pred)
    auc = roc_auc_score(y_test, prob)
    cm = confusion_matrix(y_test, pred)

    with open("resultados_knn.txt", "w", encoding="utf-8") as f:
        f.write("MEJOR CONFIGURACION KNN\n")
        f.write(str(grid.best_params_) + "\n\n")
        f.write(f"Best CV ROC-AUC: {grid.best_score_:.4f}\n")
        f.write(f"Test Accuracy: {acc:.4f}\n")
        f.write(f"Test ROC-AUC: {auc:.4f}\n\n")
        f.write("Confusion matrix:\n")
        f.write(np.array2string(cm) + "\n\n")
        f.write("Classification report:\n")
        f.write(classification_report(y_test, pred))

    return {
        "best_params": grid.best_params_,
        "best_cv_auc": grid.best_score_,
        "test_accuracy": acc,
        "test_auc": auc,
        "confusion_matrix": cm,
    }


if __name__ == "__main__":
    save_knn_regions_figure()
    save_minkowski_balls_figure()
    res = run_real_dataset_example()
    print("KNN demo completado exitosamente:")
    for k, v in res.items():
        print(f"  {k}: {v}")
