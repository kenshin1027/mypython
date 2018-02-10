import pandas as pd
from time import time, strftime, localtime
from functions import calculate_sleep_loop
from myengine import engine
import matplotlib.pyplot as plt
# today = strftime("%Y%m%d")
# t = localtime(time())
# delay_loop = calculate_sleep_loop(t)
# print 'there are still %d loops' % delay_loop[1]
# table_name = '1_min' + '_' + today
table_name = '1_min_20160401'
yesterday = "'2016-03-31'"
series_index = 120
fig = plt.figure()

ax1 = fig.add_subplot(1,2,1)
sql_str = 'select p_change from %s where series_index =%d' % (table_name, series_index)
df = pd.read_sql(sql_str, engine)
df[df['p_change']>10]=10
df[df['p_change']<-10]=-10
df.plot(ax = ax1,kind ='hist', bins = 20,color = 'green', alpha =0.5,range=(-10,10))

ax2 = fig.add_subplot(1,2,2)
sql_str1 = 'select stockcode,p_change as tp_change from dailydata where p_change>7 and `date` = %s' % yesterday
df1 = pd.read_sql(sql_str1, engine)
# print df1
sql_str2 = 'select stockcode, p_change from %s where series_index = %d' % (table_name, series_index)
df2 = pd.read_sql(sql_str2, engine)
df2[df2['p_change']>10]=10
df2[df2['p_change']<-10]=-10
# print df2
df1 = pd.merge(df1, df2,on = 'stockcode', how='left')
# print df1
df1['p_change'].plot(ax=ax2,kind ='hist', bins = 20,color = 'green', alpha =0.5,range=(-10,10))
plt.show()

