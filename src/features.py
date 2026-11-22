
"""Feature engineering for the COCOMO81 and Desharnais datasets."""

import numpy as np
import pandas as pd


def prepare_cocomo_features(df):
    """Prepare COCOMO81 input features and actual effort target."""
    required = {"dev_mode", "loc", "actual"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"Missing COCOMO81 columns: {sorted(missing)}")

    data = df.copy()

    if (data["loc"].dropna() < 0).any():
        raise ValueError("LOC cannot contain negative values.")

    # Log transformation helps handle differences in project size.
    data["log_loc"] = np.log1p(data["loc"])

    # Remove project ID and target from the input features.
    X = data.drop(columns=["num", "actual"], errors="ignore")
    y = data["actual"].copy()

    return X, y


def prepare_desharnais_features(df):
    """Prepare Desharnais input features and actual effort target."""
    required = {"PointsAjust", "Effort", "Language"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"Missing Desharnais columns: {sorted(missing)}")

    data = df.copy()

    if (data["PointsAjust"].dropna() < 0).any():
        raise ValueError("Adjusted points cannot contain negative values.")

    # Log transformation of project size.
    data["log_points"] = np.log1p(data["PointsAjust"])

    # Remove identifiers and target from the input features.
    X = data.drop(
        columns=["id", "Project", "Effort"],
        errors="ignore"
    )
    y = data["Effort"].copy()

    return X, y
