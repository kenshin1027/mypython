import tushare as ts
import pandas as pd
from time import clock, time, strftime
from sqlalchemy import create_engine
from csv import reader
PATH_ALL_CODE = r'C:\Users\zzw\Desktop\allcode.csv'
start = clock()
today = strftime("%Y-%m-%d")
engine = create_engine('mysql://root:@localhost/stockdata?charset=utf8')
with open(PATH_ALL_CODE, 'r') as csv_file:
    spam_reader = reader(csv_file, delimiter=' ', quotechar='|')
    for row in spam_reader:
        #df = ts.get_hist_data(row[0][2:8], start='2013-04-01', end='2016-03-28')
        df = ts.get_hist_data(row[0][2:8], today)
        stockcode = pd.DataFrame(row[0], index=df.index, columns= (['stockcode']))
        df.insert(0, 'stockcode', stockcode)
        del df['price_change']
        del df['ma20']
        del df['v_ma20']
        df.to_sql('dailydata', engine, if_exists='append')
csv_file.close()
end = clock()
print 'download data costs %d seconds' % (end - start)

