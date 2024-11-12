import tushare as ts
from ts_conf import TOKEN

ts.set_token(TOKEN)


def get_stock_basic_data():
    pro = ts.pro_api()
    df = pro.stk_premarket(trade_date='20240603')
    print(df)


if __name__ == '__main__':
    get_stock_basic_data()
