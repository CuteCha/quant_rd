# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts
from ts_conf import TOKEN
from pyecharts.charts import Line, Scatter
from pyecharts import options as opts
import re

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False

ts.set_token(TOKEN)
pro = ts.pro_api()


def get_stock_data_real():
    df = ts.pro_bar(
        ts_code='688107.SH',
        freq='1min',
        start_date='2024-11-13 09:00:00',
        end_date='2024-11-13 17:00:00'
    )
    print(df)


if __name__ == '__main__':
    get_stock_data_real()
