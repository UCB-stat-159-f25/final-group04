from __future__ import annotations

from typing import Iterable
import pandas as pd


DEFAULT_NONE_COLS = [
    "PoolQC", "MiscFeature", "Alley", "Fence", "FireplaceQu",
    "GarageType", "GarageFinish", "GarageQual", "GarageCond",
    "BsmtQual", "BsmtCond", "BsmtExposure", "BsmtFinType1",
    "BsmtFinType2", "MasVnrType"
]

DEFAULT_ZERO_COLS = [
    "MasVnrArea", "BsmtFinSF1", "BsmtFinSF2",
    "BsmtUnfSF", "TotalBsmtSF", "GarageCars", "GarageArea"
]


def fill_na_with_value(df: pd.DataFrame, cols: Iterable[str], value) -> pd.DataFrame:
    """Fill missing values in selected columns with a constant."""
    out = df.copy()
    for c in cols:
        if c in out.columns:
            out[c] = out[c].fillna(value)
    return out


def fill_lotfrontage_by_neighborhood_median(
    df: pd.DataFrame,
    lot_col: str = "LotFrontage",
    group_col: str = "Neighborhood",
) -> pd.DataFrame:
    """Fill missing lot frontage using neighborhood medians."""
    out = df.copy()
    if lot_col in out.columns and group_col in out.columns:
        out[lot_col] = (
            out.groupby(group_col)[lot_col]
               .transform(lambda x: x.fillna(x.median()))
        )
    return out


def fill_na_with_mode(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Fill missing values in a column using its mode."""
    out = df.copy()
    if col not in out.columns:
        return out
    if not out[col].isna().any():
        return out

    mode = out[col].mode(dropna=True)
    if mode.empty:
        raise ValueError(f"Cannot fill mode for column '{col}'.")
    out[col] = out[col].fillna(mode.iloc[0])
    return out


def clean_ames_missing(
    df: pd.DataFrame,
    *,
    none_cols: list[str] = DEFAULT_NONE_COLS,
    zero_cols: list[str] = DEFAULT_ZERO_COLS,
    lot_col: str = "LotFrontage",
    neighborhood_col: str = "Neighborhood",
    electrical_col: str = "Electrical",
) -> pd.DataFrame:
    """Clean missing values in the Ames Housing dataset."""
    out = df.copy()
    out = fill_na_with_value(out, none_cols, "None")
    out = fill_na_with_value(out, zero_cols, 0)
    out = fill_lotfrontage_by_neighborhood_median(
        out, lot_col=lot_col, group_col=neighborhood_col
    )
    out = fill_na_with_mode(out, electrical_col)
    return out
