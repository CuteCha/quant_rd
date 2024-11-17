import qstock as qs


def get_hs_all_stock():
    df = qs.realtime_data()
    print(df.head())


if __name__ == '__main__':
    get_hs_all_stock()
