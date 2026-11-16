
import numpy as np


def _validate(values, name):
    """Convert values to a valid one-dimensional numeric array."""
    values = np.asarray(values, dtype=float)

    if values.ndim != 1 or len(values) == 0:
        raise ValueError(f"{name} must be a non-empty one-dimensional array.")

    if not np.all(np.isfinite(values)):
        raise ValueError(f"{name} must contain finite values.")

    if np.any(values < 0):
        raise ValueError(f"{name} cannot contain negative values.")

    return values


def mean_baseline(y_train, n_predictions):
    """Predict the training-set mean for every test project."""
    y_train = _validate(y_train, "Training effort")

    if n_predictions < 1:
        raise ValueError("n_predictions must be at least 1.")

    return np.full(n_predictions, np.mean(y_train))


def median_baseline(y_train, n_predictions):
    """Predict the training-set median for every test project."""
    y_train = _validate(y_train, "Training effort")

    if n_predictions < 1:
        raise ValueError("n_predictions must be at least 1.")

    return np.full(n_predictions, np.median(y_train))


# Basic COCOMO coefficients by development mode:
# effort = a * (KLOC ** b)
COCOMO_COEFFICIENTS = {
    "organic": (2.4, 1.05),
    "semidetached": (3.0, 1.12),
    "embedded": (3.6, 1.20),
}


def basic_cocomo_baseline(kloc, dev_mode):
    """Predict effort in person-months using Basic COCOMO."""
    kloc = _validate(kloc, "KLOC")
    dev_mode = np.asarray(dev_mode, dtype=str)

    if dev_mode.ndim != 1 or len(dev_mode) != len(kloc):
        raise ValueError("KLOC and development modes must have equal lengths.")

    predictions = []

    for size, mode in zip(kloc, dev_mode):
        mode = mode.strip().lower()

        if size <= 0:
            raise ValueError("KLOC values must be greater than zero.")

        if mode not in COCOMO_COEFFICIENTS:
            raise ValueError(f"Unknown COCOMO development mode: {mode}")

        a, b = COCOMO_COEFFICIENTS[mode]
        predictions.append(a * (size ** b))

    return np.asarray(predictions)


def fit_size_ratio(size_train, effort_train):
    """Learn a size-to-effort ratio using training data only."""
    size_train = _validate(size_train, "Training size")
    effort_train = _validate(effort_train, "Training effort")

    if len(size_train) != len(effort_train):
        raise ValueError("Training size and effort lengths must match.")

    if np.any(size_train <= 0):
        raise ValueError("Training sizes must be greater than zero.")

    coefficient = np.dot(size_train, effort_train) / np.dot(
        size_train, size_train
    )

    return float(coefficient)


def size_ratio_baseline(size, coefficient):
    """Predict effort from size using a fitted training-set ratio."""
    size = _validate(size, "Project size")

    if np.any(size <= 0):
        raise ValueError("Project sizes must be greater than zero.")

    if not np.isfinite(coefficient) or coefficient < 0:
        raise ValueError("Coefficient must be a finite non-negative number.")

    return coefficient * size
