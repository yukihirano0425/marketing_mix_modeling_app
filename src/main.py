import pandas as pd
from prophet import Prophet

from model.prophet_model import convert_df_for_prophet, fit_predict_prophet_model
from utils.get_holidays_jp import get_holiday_jp
from utils.plot_cost_transition import plot_cost_transition
from utils.read_dataset import read_datasets

target = "revenue"
# sales_channel = ["営業チャネルA", "営業チャネルB", "営業チャネルC", "営業チャネルD", "営業チャネルE"]
sales_channel = [
    "tv_S",
    "ooh_S",
    "print_S",
    "facebook_I",
    "search_clicks_P",
    "search_S",
]
# non_sales_channel = ["非営業チャネルA", "非営業チャネルB", "非営業チャネルC", "非営業チャネルD", "非営業チャネルE"]
non_sales_channel = ["competitor_sales_B", "facebook_S", "newsletter"]
whole_cost = sales_channel + non_sales_channel
features = sales_channel + non_sales_channel
columns = ["DATE"] + [target] + features


df = read_datasets("data_raw_Robyn.csv", "DATE", columns)
holiday_df = get_holiday_jp(2015, 11, 23, 2019, 11, 11)

# plot_cost_transition(df, "DATE", whole_cost)

prophet_df = convert_df_for_prophet(df, target, "DATE")
pred, prophet_model = fit_predict_prophet_model(holiday_df, prophet_df)
