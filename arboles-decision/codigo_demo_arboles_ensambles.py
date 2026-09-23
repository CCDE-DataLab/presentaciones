"""Demo reproducible para la presentación de árboles y ensambles.

Usa un conjunto incluido en scikit-learn, por lo que no requiere descargas.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import (
    BaggingClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text


RANDOM_STATE = 42


def main() -> None:
    data = load_breast_cancer(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        data.data,
        data.target,
        test_size=0.25,
        stratify=data.target,
        random_state=RANDOM_STATE,
    )

    base_tree = DecisionTreeClassifier(
        max_depth=3,
        min_samples_leaf=8,
        random_state=RANDOM_STATE,
    )

    models = {
        "Árbol": base_tree,
        "Bagging": BaggingClassifier(
            estimator=DecisionTreeClassifier(random_state=RANDOM_STATE),
            n_estimators=300,
            max_samples=0.8,
            bootstrap=True,
            oob_score=True,
            n_jobs=-1,
            random_state=RANDOM_STATE,
        ),
        "Random forest": RandomForestClassifier(
            n_estimators=500,
            max_features="sqrt",
            min_samples_leaf=2,
            oob_score=True,
            n_jobs=-1,
            random_state=RANDOM_STATE,
        ),
        "Gradient boosting": GradientBoostingClassifier(
            n_estimators=150,
            learning_rate=0.05,
            max_depth=2,
            random_state=RANDOM_STATE,
        ),
    }

    print("Modelo               Accuracy   ROC-AUC   OOB")
    print("-" * 52)
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        prob = model.predict_proba(X_test)[:, 1]
        oob = getattr(model, "oob_score_", None)
        oob_text = f"{oob:.3f}" if oob is not None else "—"
        print(
            f"{name:<20} {accuracy_score(y_test, pred):>8.3f}"
            f"   {roc_auc_score(y_test, prob):>7.3f}   {oob_text:>5}"
        )

    base_tree.fit(X_train, y_train)
    print("\nReglas del árbol regularizado:\n")
    print(export_text(base_tree, feature_names=list(data.feature_names)))


if __name__ == "__main__":
    main()
