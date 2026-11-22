
"""Regression model pipelines for project effort estimation."""

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_preprocessor(X, scale_numeric=True):
    """Build preprocessing steps using available input columns."""

    categorical_columns = [
        col for col in X.columns
        if (
            X[col].dtype == "object"
            or X[col].dtype.name == "category"
            or col in ["dev_mode", "Language"]
        )
    ]

    numeric_columns = [
        col for col in X.columns
        if col not in categorical_columns
    ]

    numeric_steps = [
        ("imputer", SimpleImputer(strategy="median"))
    ]

    if scale_numeric:
        numeric_steps.append(
            ("scaler", StandardScaler())
        )

    numeric_pipeline = Pipeline(numeric_steps)

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])

    transformers = []

    if numeric_columns:
        transformers.append(
            ("numeric", numeric_pipeline, numeric_columns)
        )

    if categorical_columns:
        transformers.append(
            ("categorical", categorical_pipeline, categorical_columns)
        )

    return ColumnTransformer(transformers=transformers)


def build_models(X):
    """Create the three regression model pipelines."""

    return {
        "Ridge Regression": Pipeline([
            ("preprocessor", build_preprocessor(X, True)),
            ("model", Ridge(alpha=1.0)),
        ]),

        "Random Forest": Pipeline([
            ("preprocessor", build_preprocessor(X, False)),
            ("model", RandomForestRegressor(
                n_estimators=300,
                min_samples_leaf=2,
                random_state=42,
                n_jobs=-1,
            )),
        ]),

        "Gradient Boosting": Pipeline([
            ("preprocessor", build_preprocessor(X, False)),
            ("model", GradientBoostingRegressor(
                n_estimators=100,
                learning_rate=0.05,
                max_depth=2,
                random_state=42,
            )),
        ]),
    }
