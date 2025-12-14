import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


from src.models import _eval_model_core


def test_eval_model_core_runs():
    X_train = np.array([[0], [1], [2], [3]])
    y_train = np.array([0, 1, 0, 1])

    X_valid = np.array([[1], [2]])
    y_valid = np.array([0, 1]) 

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression())
    ])

    class_names = ["class_0", "class_1"]

    acc, cm = _eval_model_core(
        "logistic",
        pipe,
        X_train, y_train,
        X_valid, y_valid,
        class_names,
    )

    assert cm.shape == (2, 2)
    assert 0 <= acc <= 1
