import pandas as pd
import pytest

from src.ames_cleaning import (
    fill_na_with_value,
    fill_lotfrontage_by_neighborhood_median,
    fill_na_with_mode,
    clean_ames_missing,
)


def test_fill_na_with_value_fills_only_specified_cols():
    df = pd.DataFrame({"A": [None, 1], "B": [None, 2]})
    out = fill_na_with_value(df, cols=["A"], value="X")
    assert out["A"].iloc[0] == "X"
    assert pd.isna(out["B"].iloc[0])  # B untouched
    # original not modified
    assert pd.isna(df["A"].iloc[0])


def test_fill_lotfrontage_by_neighborhood_median_groupwise():
    df = pd.DataFrame(
        {"Neighborhood": ["N1", "N1", "N2", "N2"],
         "LotFrontage": [10.0, None, 20.0, None]}
    )
    out = fill_lotfrontage_by_neighborhood_median(df)
    assert out.loc[1, "LotFrontage"] == 10.0  # median of N1
    assert out.loc[3, "LotFrontage"] == 20.0  # median of N2


def test_fill_na_with_mode_fills_missing():
    df = pd.DataFrame({"Electrical": ["SBrkr", None, "SBrkr", "FuseA"]})
    out = fill_na_with_mode(df, "Electrical")
    assert out["Electrical"].isna().sum() == 0
    assert out.loc[1, "Electrical"] == "SBrkr"  # mode


def test_fill_na_with_mode_raises_if_all_na():
    df = pd.DataFrame({"Electrical": [None, None]})
    with pytest.raises(ValueError):
        fill_na_with_mode(df, "Electrical")


def test_clean_ames_missing_end_to_end():
    df = pd.DataFrame({
        "PoolQC": [None, "Ex"],
        "GarageArea": [None, 200],
        "Neighborhood": ["N1", "N1"],
        "LotFrontage": [10.0, None],
        "Electrical": ["SBrkr", None],
    })
    out = clean_ames_missing(
        df,
        none_cols=["PoolQC"],
        zero_cols=["GarageArea"],
        lot_col="LotFrontage",
        neighborhood_col="Neighborhood",
        electrical_col="Electrical",
    )

    assert out.loc[0, "PoolQC"] == "None"
    assert out.loc[0, "GarageArea"] == 0
    assert out.loc[1, "LotFrontage"] == 10.0
    assert out.loc[1, "Electrical"] == "SBrkr"
