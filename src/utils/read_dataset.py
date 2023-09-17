import os
from pathlib import Path

import pandas as pd

path = ""

PATH = Path(path)
DATA_DIR = PATH / "data"
os.makedirs(DATA_DIR, exist_ok=True)


def read_datasets(
    file_name: str, date_column_name: str, target_columns: list[str]
) -> pd.DataFrame:
    """
    args:
      file_name: ファイル名を記載
      date_column_name: 日付のカラム名を記載
      target_columns: 読み込みたいカラム名を記載
    reutrn:
      df:
        file_name: ファイル名を記載
        行: 1日分の営業チャネル費用 + 売上
        列：日付 + 各広告チャネル + 売上
    """
    df = pd.read_csv(file_name, parse_dates=[date_column_name])
    df.columns = [
        col.lower() if col in [date_column_name] else col for col in df.columns
    ]
    return df[target_columns]


target_columns = [
    "チャネルA",
    "チャネルB",
    "チャネルC",
]
df = read_datasets(DATA_DIR / "data_mmm.csv", "date")[target_columns]
