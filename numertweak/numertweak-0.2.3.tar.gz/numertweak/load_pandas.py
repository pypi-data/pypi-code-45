from zipfile import ZipFile
import pandas as pd
import numpy as np
from .get_cols import get_cols


def get_dtypes():
    """dtype for pandas.read_csv"""
    col_ids, col_typ, _, col_target, col_feat, _ = get_cols()
    dtypes = {}
    dtypes = {**dtypes, **{s: np.float16 for s in col_feat}}
    dtypes = {**dtypes, **{s: np.float16 for s in col_target}}
    dtypes = {**dtypes, **{s: str for s in col_typ}}
    dtypes = {**dtypes, **{s: str for s in col_ids}}
    return dtypes


def get_converters():
    """converters for pandas.read_csv"""
    convert_era = lambda s: np.uint16(s[3:]) if s != 'eraX' else np.uint16(999)
    converters = {}
    converters = {**converters, **{"era": convert_era}}
    return converters


def load_dataset(filepath: str = "numerai_datasets.zip",
                 csvname: str = "numerai_training_data.csv"):
    """Load training set or test set

    Examples:
    ---------
    df_train = load_dataset("numerai_datasets.zip", "numerai_training_data.csv")
    df_submit = load_dataset("numerai_datasets.zip", "numerai_tournament_data.csv")
    """
    dtypes = get_dtypes()
    converters = get_converters()
    with ZipFile(filepath) as zipptr:
        # print(zipptr.namelist())
        with zipptr.open(csvname) as csvfile:
            df = pd.read_csv(csvfile, dtype=dtypes, converters=converters)
    return df
