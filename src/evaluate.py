
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from src.baselines import (
    mean_baseline,
    median_baseline,
    basic_cocomo_baseline,
    fit_size_ratio,
    size_ratio_baseline,
)
from src.metrics import mae, mmre, pred_25


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"


def evaluate_predictions(dataset, estimator, actual, predicted, unit, n_train):
    """Calculate evaluation metrics for one estimator."""
    return {
        "Dataset": dataset,
        "Estimator": estimator,
        "Train Projects": n_train,
        "Test Projects": len(actual),
        "MAE": mae(actual, predicted),
        "MMRE (%)": mmre(actual, predicted) * 100,
        "Pred(25) (%)": pred_25(actual, predicted) * 100,
        "Effort Unit": unit,
    }


def evaluate_cocomo():
    """Evaluate baselines on the COCOMO81 dataset."""
    path = ROOT / "data" / "raw" / "cocomo81.csv"
    df = pd.read_csv(path)

    df = df.dropna(subset=["loc", "actual", "dev_mode"])
    df = df[(df["loc"] > 0) & (df["actual"] > 0)]

    train, test = train_test_split(
        df, test_size=0.20, random_state=42
    )

    y_train = train["actual"].to_numpy()
    y_test = test["actual"].to_numpy()

    results = []

    predictions = {
        "Mean": mean_baseline(y_train, len(test)),
        "Median": median_baseline(y_train, len(test)),
        "Basic COCOMO": basic_cocomo_baseline(
            test["loc"].to_numpy(),
            test["dev_mode"].to_numpy(),
        ),
    }

    for name, predicted in predictions.items():
        results.append(
            evaluate_predictions(
                "COCOMO81", name, y_test, predicted,
                "person-months", len(train)
            )
        )

    return results


def evaluate_desharnais():
    """Evaluate baselines on the Desharnais dataset."""
    path = ROOT / "data" / "raw" / "desharnais.csv"
    df = pd.read_csv(path)

    df = df.dropna(subset=["PointsAjust", "Effort"])
    df = df[
        (df["PointsAjust"] > 0) &
        (df["Effort"] > 0)
    ]

    train, test = train_test_split(
        df, test_size=0.20, random_state=42
    )

    y_train = train["Effort"].to_numpy()
    y_test = test["Effort"].to_numpy()

    coefficient = fit_size_ratio(
        train["PointsAjust"].to_numpy(),
        y_train,
    )

    predictions = {
        "Mean": mean_baseline(y_train, len(test)),
        "Median": median_baseline(y_train, len(test)),
        "Size Ratio": size_ratio_baseline(
            test["PointsAjust"].to_numpy(),
            coefficient,
        ),
    }

    results = []

    for name, predicted in predictions.items():
        results.append(
            evaluate_predictions(
                "Desharnais", name, y_test, predicted,
                "person-hours", len(train)
            )
        )

    return results


def main():
    RESULTS_DIR.mkdir(exist_ok=True)

    all_results = (
        evaluate_cocomo() +
        evaluate_desharnais()
    )

    results_df = pd.DataFrame(all_results)

    csv_path = RESULTS_DIR / "baseline_results.csv"
    markdown_path = RESULTS_DIR / "baseline_results.md"

    results_df.to_csv(csv_path, index=False)

    with open(markdown_path, "w", encoding="utf-8") as file:
        file.write("# Week 2 Baseline Evaluation Results\n\n")
        file.write("Train/test split: 80/20, random_state=42\n\n")
        file.write(results_df.round(3).to_markdown(index=False))
        file.write("\n")

    print("\nWEEK 2 BASELINE RESULTS\n")
    print(results_df.round(3).to_string(index=False))

    print(f"\nCSV saved to: {csv_path}")
    print(f"Markdown saved to: {markdown_path}")


if __name__ == "__main__":
    main()
