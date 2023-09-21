from typing import Optional

import pandas as pd
from prophet import Prophet


def convert_df_for_prophet(
    data: pd.DataFrame,
    sales_column_name: str,
    date_column_name: str,
    *event_column_name: Optional[str]
) -> pd.DataFrame:
    """prophetの時系列分析ができるようデータ整形を行う
    args:
      data: mmm用データ(eventカラムがある場合の設計)
      sales_column_name: 売上カラム名
      date_column_name: 日付カラム名
      event_column_name: イベントカラム名（任意指定）
    return:
      prophet_df: prophetに適したデータ（カラム名変換、eventカラムをダミーデータ変換）
    """
    event_values = None
    if event_column_name:
        event_values = pd.get_dummies(
            data[event_column_name], drop_first=True, prefix="events"
        )

    # Prophetに合わせて、売上カラムをyに、日付カラムをdsに変換する必要がある
    data = data.rename(columns={sales_column_name: "y", date_column_name: "ds"})
    prophet_df = pd.concat([data, event_values], axis=1)

    return prophet_df


def create_prophet_model(holiday_df: pd.DataFrame) -> Prophet:
    """prophetモデルを作成
    args:
      holiday_df:
        祝日データ
    return:
      prophet_model:
        prophetモデル（詳細はパラメーターを参照）
        https://facebook.github.io/prophet/docs/quick_start.html
    """
    prophet_model = Prophet(
        yearly_seasonality=True, weekly_seasonality=True, holidays=holiday_df
    )

    # prophet_model.add_regressor(name="weekend")

    return prophet_model


def fit_predict_prophet_model(holiday_df: pd.DataFrame, prophet_df: pd.DataFrame):
    """
    モデルfitとpredictを実行する
    prophet_model.add_regressorをした場合は、そのカラムをfitとpredictに追加する
    """
    prophet_model = create_prophet_model(holiday_df)
    prophet_model.fit(
        prophet_df[["ds", "y"]]  # "weekend"
    )  # , "events_event2", "events_na"
    pred = prophet_model.predict(
        prophet_df[["ds", "y"]]  # "weekend"
    )  # , "events_event2", "events_na"
    return pred, prophet_model
