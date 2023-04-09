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
