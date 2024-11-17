import tushare as ts
from ts_conf import TOKEN
import talib as ta

ts.set_token(TOKEN)


def get_stock_basic_data():
    pro = ts.pro_api()
    df = pro.stk_premarket(trade_date='20241112')
    print(df)


def _test_ta():
    import numpy as np
    close = np.random.random(100)
    output = ta.SMA(close)
    upper, middle, lower = ta.BBANDS(close, matype=ta.MA_Type.T3)
    print(len(output))
    print(len(upper))
    print(len(middle))
    print(len(lower))


if __name__ == '__main__':
    get_stock_basic_data()
    _test_ta()
