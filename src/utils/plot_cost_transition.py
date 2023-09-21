import matplotlib.pyplot as plt
import pandas as pd


def plot_cost_transition(
    df: pd.DataFrame, date_column_name: str, features: list[str]
) -> None:
    """
    指定した営業チャネルのコスト推移をグラフ表示する
    args:
      df: 日別のコストデータの入ったデータフレーム
      date_column_name: 日付カラム
      features: 表示したい営業チャネル
        ex: 複数チャネルを表示する場合) ["sales_channel_A", "sales_channel_B", "sales_channel_C"]
        ex: 単一チャネルを表示する場合) ["sales_channel_A"]
    """

    plt.figure(figsize=(17, 7))
    plt.plot(df[date_column_name], df[features], label=features)

    plt.title(f"{features[0]}")
    plt.xticks(rotation=90)
    plt.ylabel("コスト(円)")
    plt.legend(fontsize=14, loc="upper left")
    plt.ticklabel_format(style="plain", axis="y")

    plt.show()
    plt.tight_layout()
