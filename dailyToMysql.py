import tushare as ts
import pandas as pd
from time import clock, time, strftime
from csv import reader
from constant import PATH_ALL_CODE, ENGINE


def download_dailydata():
    start = clock()
    today = strftime("%Y-%m-%d")
    with open(PATH_ALL_CODE, 'r') as csv_file:
        spam_reader = reader(csv_file, delimiter=' ', quotechar='|')
        for row in spam_reader:
            #df = ts.get_hist_data(row[0][2:8], start='2016-03-31', end='2016-03-31')
            df = ts.get_hist_data(row[0][2:8], today)
            stockcode = pd.DataFrame(row[0], index=df.index, columns= (['stockcode']))
            df.insert(0, 'stockcode', stockcode)
            del df['price_change']
            del df['ma20']
            del df['v_ma20']
            df.to_sql('dailydata', ENGINE, if_exists='append')
    csv_file.close()

    index_list = ['sz399001','sz399006']
    for i in range(0, len(index_list)):
        df = ts.get_hist_data(index_list[i][2:8],today)
        stockcode = pd.DataFrame(index_list[i], index=df.index, columns= (['stockcode']))
        df.insert(0, 'stockcode', stockcode)
        del df['price_change']
        del df['ma20']
        del df['v_ma20']
        df.to_sql('index', ENGINE, if_exists='append')
    end = clock()
    print 'download data costs %d seconds' % (end - start)

