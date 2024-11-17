import efinance as ef


def get_stock_data_min():
    stock_code = '688107'
    frequency = 1  # 5min
    start_time = '20241113'
    df = ef.stock.get_quote_history(stock_code, klt=frequency, beg=start_time)
    print(df.head(10))
    print(df.tail(10))


def get_stock_data_lt():
    start_date = '2024-11-11'
    end_date = '2024-11-13'
    df = ef.stock.get_daily_billboard(start_date=start_date, end_date=end_date)
    print(df.head(10))
    print(df.tail(10))


if __name__ == '__main__':
    # get_stock_data_min()
    get_stock_data_lt()
