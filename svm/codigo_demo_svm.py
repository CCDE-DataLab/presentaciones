"""Demo reproducible de Support Vector Machines para la sesión CCDE.

Genera:
- métricas de un SVM lineal y un SVM RBF sobre make_moons;
- búsqueda de hiperparámetros con GridSearchCV;
- tres figuras PNG usadas opcionalmente por la presentación Beamer.

Requisitos:
    pip install numpy matplotlib scikit-learn
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs, make_moons
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

RANDOM_STATE = 42


def plot_boundary(ax, model, X, y, title: str) -> None:
    """Dibuja frontera, margen aproximado y observaciones."""
    x_min, x_max = X[:, 0].min() - 0.7, X[:, 0].max() + 0.7
    y_min, y_max = X[:, 1].min() - 0.7, X[:, 1].max() + 0.7
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 400),
        np.linspace(y_min, y_max, 400),
    )
    grid = np.c_[xx.ravel(), yy.ravel()]
    zz = model.decision_function(grid).reshape(xx.shape)

    ax.contourf(xx, yy, zz > 0, alpha=0.12)
    ax.contour(xx, yy, zz, levels=[-1, 0, 1], linestyles=["--", "-", "--"], linewidths=[1, 2, 1])
    ax.scatter(X[:, 0], X[:, 1], c=y, s=24, edgecolors="k", linewidths=0.25)
    ax.set_title(title)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")


def figure_hard_soft() -> None:
    X, y = make_blobs(
        n_samples=90,
        centers=[(-1.4, -0.2), (1.4, 0.2)],
        cluster_std=0.55,
        random_state=RANDOM_STATE,
    )
    # Outlier deliberado: vuelve poco razonable una frontera casi hard-margin.
    X = np.vstack([X, [[0.15, 1.35]]])
    y = np.r_[y, 0]

    models = [
        make_pipeline(StandardScaler(), SVC(kernel="linear", C=0.15)),
        make_pipeline(StandardScaler(), SVC(kernel="linear", C=1000)),
    ]
    titles = ["Soft margin: C = 0.15", "Penalización fuerte: C = 1000"]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
    for ax, model, title in zip(axes, models, titles):
        model.fit(X, y)
        plot_boundary(ax, model, X, y, title)
    fig.savefig("fig_svm_hard_soft.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def figure_kernel_moons() -> None:
    X, y = make_moons(n_samples=360, noise=0.22, random_state=RANDOM_STATE)
    models = [
        make_pipeline(StandardScaler(), SVC(kernel="linear", C=1.0)),
        make_pipeline(StandardScaler(), SVC(kernel="rbf", C=10.0, gamma=1.0)),
    ]
    titles = ["Kernel lineal", "Kernel RBF"]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
    for ax, model, title in zip(axes, models, titles):
        model.fit(X, y)
        plot_boundary(ax, model, X, y, title)
    fig.savefig("fig_svm_kernel_moons.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def figure_gamma() -> None:
    X, y = make_moons(n_samples=320, noise=0.22, random_state=RANDOM_STATE)
    gammas = [0.1, 1.0, 10.0]
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.0), constrained_layout=True)
    for ax, gamma in zip(axes, gammas):
        model = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=10.0, gamma=gamma))
        model.fit(X, y)
        plot_boundary(ax, model, X, y, f"RBF: gamma = {gamma:g}")
    fig.savefig("fig_svm_gamma.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    X, y = make_moons(n_samples=600, noise=0.25, random_state=RANDOM_STATE)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        stratify=y,
        random_state=RANDOM_STATE,
    )

    pipe = make_pipeline(StandardScaler(), SVC())
    param_grid = [
        {
            "svc__kernel": ["linear"],
            "svc__C": [0.1, 1, 10, 100],
        },
        {
            "svc__kernel": ["rbf"],
            "svc__C": [0.1, 1, 10, 100],
            "svc__gamma": ["scale", 0.1, 1, 10],
        },
    ]

    search = GridSearchCV(
        pipe,
        param_grid=param_grid,
        scoring="roc_auc",
        cv=5,
        n_jobs=-1,
        refit=True,
    )
    search.fit(X_train, y_train)

    best = search.best_estimator_
    pred = best.predict(X_test)
    score = best.decision_function(X_test)

    print("Mejores hiperparámetros:", search.best_params_)
    print(f"ROC-AUC CV: {search.best_score_:.4f}")
    print(f"Accuracy test: {accuracy_score(y_test, pred):.4f}")
    print(f"ROC-AUC test: {roc_auc_score(y_test, score):.4f}")
    print("Matriz de confusión:\n", confusion_matrix(y_test, pred))
    print("Support vectors por clase:", best.named_steps["svc"].n_support_)

    # Comparación lineal vs RBF con parámetros razonables.
    candidates = {
        "SVM lineal": make_pipeline(StandardScaler(), SVC(kernel="linear", C=1.0)),
        "SVM RBF": make_pipeline(StandardScaler(), SVC(kernel="rbf", C=10.0, gamma=1.0)),
    }
    for name, model in candidates.items():
        model.fit(X_train, y_train)
        p = model.predict(X_test)
        s = model.decision_function(X_test)
        print(
            f"{name}: accuracy={accuracy_score(y_test, p):.4f}, "
            f"roc_auc={roc_auc_score(y_test, s):.4f}, "
            f"SV={model.named_steps['svc'].support_.size}"
        )

    figure_hard_soft()
    figure_kernel_moons()
    figure_gamma()
    print("Figuras generadas: fig_svm_hard_soft.png, fig_svm_kernel_moons.png, fig_svm_gamma.png")


if __name__ == "__main__":
    main()
