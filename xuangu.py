import pandas as pd
from myengine import engine

loop_time = 125
table_name = '1_min_20160331'
yesterday = "'2016-03-30'"
# fenshijunxian
sql_str1 = 'select stockcode, sum(indicator) as a from %s where series_index <= %d group by stockcode order by a desc limit 150' % (table_name, loop_time)
df1 = pd.read_sql(sql_str1, engine)
df1['a'] = df1['a']/loop_time
df1 = df1[df1['a']>0.9]

# price(-3~+5) and volume
sql_str2 = 'select stockcode,`close`,`high`, p_change, volume from %s where series_index = %d  and p_change between -2 and 4' % (table_name, loop_time)
df2 = pd.read_sql(sql_str2, engine)

# merge df1 and df2 on stockcode, then filter the list according to p_change
df1 = pd.merge(df1, df2, on='stockcode', how='left')
df1 = df1[pd.notnull(df1['p_change'])]
df1['volume'] = df1['volume'] / loop_time/100  # the volume here is actually stock number, not shou

# select p_change volume from dailydata
# sql_str3 = 'select stockcode,volume as t_volume from dailydata where `date` = %s' % yesterday
# df3 = pd.read_sql(sql_str3, engine)
# df3['t_volume'] = df3['t_volume'] / 240   # one trading day have 240 minutes
#
# df1 = pd.merge(df1, df3, on='stockcode',how='left')
# df1 = df1[df1['volume']>df1['t_volume']]
#
# df1 = df1[df1['close']>df1['high']*0.98]
print df1



