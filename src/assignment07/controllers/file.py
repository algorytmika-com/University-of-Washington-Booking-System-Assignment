import pandas as pd

from settings.path import csv_path

def get_path():
    return csv_path

def get_csv_content(path):
    return pd.read_csv(path)

