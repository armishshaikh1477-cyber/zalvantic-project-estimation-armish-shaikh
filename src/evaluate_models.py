
"""Evaluate regression models and baselines using LOOCV."""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.model_selection import LeaveOneOut

from src.features import (
    prepare_cocomo_features,
    prepare_desharnais_features,
)
from src.models import build_models
from src.baselines import (
    mean_baseline,
    median_baseline,
    basic_cocomo_baseline,
    fit_size_ratio,
    size_ratio_baseline,
)
from src.metrics import mae, mmre, pred_25


ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
RESULTS_DIR = ROOT / "results"


def evaluate_dataset(dataset_name, X, y):
    """Evaluate all estimators using identical LOOCV folds."""

    if (y <= 0).any():
        raise ValueError(
            f"{dataset_name}: actual effort must be positive."
        )

    loo = LeaveOneOut()
    models = build_models(X)

    estimator_names = [
        "Mean Baseline",
        "Median Baseline",
        "Size-Based Baseline",
        "Ridge Regression",
        "Random Forest",
        "Gradient Boosting",
    ]

    predictions = {
        name: [] for name in estimator_names
    }

    for train_index, test_index in loo.split(X):

        X_train = X.iloc[train_index]
        X_test = X.iloc[test_index]

        y_train = y.iloc[train_index]
        y_test = y.iloc[test_index]

        # Week 2 mean and median baselines.
        predictions["Mean Baseline"].append(
            mean_baseline(y_train, len(test_index))[0]
        )

        predictions["Median Baseline"].append(
            median_baseline(y_train, len(test_index))[0]
        )

        # Dataset-specific size-based baseline.
        if dataset_name == "COCOMO81":
            size_predictions = basic_cocomo_baseline(
                X_test["loc"].to_numpy(),
                X_test["dev_mode"].to_numpy(),
            )
        else:
            coefficient = fit_size_ratio(
                X_train["PointsAjust"].to_numpy(),
                y_train.to_numpy(),
            )

            size_predictions = size_ratio_baseline(
                X_test["PointsAjust"].to_numpy(),
                coefficient,
            )

        predictions["Size-Based Baseline"].append(
            np.asarray(size_predictions).reshape(-1)[0]
        )

        # Train and predict with the three regression models.
        for model_name, model in models.items():
            fitted_model = clone(model)
            fitted_model.fit(X_train, y_train)

            prediction = fitted_model.predict(X_test)[0]
            predictions[model_name].append(prediction)

    # Calculate metrics from all out-of-fold predictions.
    results = []

    for estimator_name, predicted_values in predictions.items():
        predicted_values = np.asarray(
            predicted_values, dtype=float
        )

        results.append({
            "Dataset": dataset_name,
            "Estimator": estimator_name,
            "Projects": len(y),
            "MAE": mae(y, predicted_values),
            "MMRE (%)": mmre(y, predicted_values) * 100,
            "Pred(25) (%)": pred_25(y, predicted_values) * 100,
        })

    return results


def main():
    """Run the complete Week 3 evaluation."""

    cocomo = pd.read_csv(RAW_DIR / "cocomo81.csv")
    desharnais = pd.read_csv(RAW_DIR / "desharnais.csv")

    X_cocomo, y_cocomo = prepare_cocomo_features(cocomo)
    X_desharnais, y_desharnais = prepare_desharnais_features(
        desharnais
    )

    results = []

    results.extend(
        evaluate_dataset("COCOMO81", X_cocomo, y_cocomo)
    )

    results.extend(
        evaluate_dataset("Desharnais", X_desharnais, y_desharnais)
    )

    results_df = pd.DataFrame(results)

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    csv_path = RESULTS_DIR / "week3_cv_results.csv"
    md_path = RESULTS_DIR / "week3_cv_results.md"

    results_df.to_csv(csv_path, index=False)

    with open(md_path, "w", encoding="utf-8") as file:
        file.write("# Week 3: Cross-Validation Results\n\n")
        file.write(
            "Evaluation uses Leave-One-Out Cross-Validation "
            "(LOOCV). All estimators use identical held-out folds.\n\n"
        )
        file.write(results_df.to_markdown(index=False))
        file.write("\n")

    print("\nWEEK 3 CROSS-VALIDATION RESULTS\n")
    print(results_df.to_string(index=False))

    print(f"\nCSV saved to: {csv_path}")
    print(f"Markdown saved to: {md_path}")


if __name__ == "__main__":
    main()
