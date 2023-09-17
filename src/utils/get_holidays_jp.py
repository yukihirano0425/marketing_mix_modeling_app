import datetime

import jpholiday
import pandas as pd


def get_holiday_jp(
    from_year: int,
    from_month: int,
    from_day: int,
    to_year: int,
    to_month: int,
    to_day: int,
):
    """
    日本の休日をデータフレームで取得する
    """
    holiday = jpholiday.between(
        datetime.date(from_year, from_month, from_day),
        datetime.date(to_year, to_month, to_day),
    )
    ds = [date[0] for date in holiday]
    holiday_name = [date[1] for date in holiday]

    holiday_df = pd.DataFrame({"ds": ds, "holiday": holiday_name})
    holiday_df["ds"] = pd.to_datetime(holiday_df["ds"])
    return holiday_df
