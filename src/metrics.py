
import numpy as np


def _validate_inputs(y_true, y_pred):
    """Validate actual and predicted effort values."""
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    if y_true.ndim != 1 or y_pred.ndim != 1:
        raise ValueError("Inputs must be one-dimensional.")

    if len(y_true) == 0:
        raise ValueError("Inputs cannot be empty.")

    if len(y_true) != len(y_pred):
        raise ValueError("Actual and predicted values must have equal lengths.")

    if not np.all(np.isfinite(y_true)) or not np.all(np.isfinite(y_pred)):
        raise ValueError("Inputs must contain only finite numbers.")

    return y_true, y_pred


def mae(y_true, y_pred):
    """Calculate Mean Absolute Error."""
    y_true, y_pred = _validate_inputs(y_true, y_pred)
    return float(np.mean(np.abs(y_true - y_pred)))


def mmre(y_true, y_pred):
    """Calculate Mean Magnitude of Relative Error."""
    y_true, y_pred = _validate_inputs(y_true, y_pred)

    if np.any(y_true == 0):
        raise ValueError("MMRE is undefined when actual effort is zero.")

    relative_errors = np.abs(y_true - y_pred) / np.abs(y_true)
    return float(np.mean(relative_errors))


def pred_25(y_true, y_pred):
    """Return the proportion of predictions with relative error <= 25%."""
    y_true, y_pred = _validate_inputs(y_true, y_pred)

    if np.any(y_true == 0):
        raise ValueError("Pred(25) is undefined when actual effort is zero.")

    relative_errors = np.abs(y_true - y_pred) / np.abs(y_true)
    return float(np.mean(relative_errors <= 0.25))
