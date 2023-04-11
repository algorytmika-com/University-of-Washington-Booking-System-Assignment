import pandas as pd
from settings.path import csv_path


def get_path() -> str:
    return csv_path


def get_dataframe_from_file(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print("File not found")
    return df


def append_dataframe_to_file(df: pd.DataFrame, path: str) -> None:
    try:
        df.to_csv(path, mode='a', index=False, header=False)
    except FileNotFoundError:
        print("File not found")
    return df
