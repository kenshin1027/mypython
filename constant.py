from sqlalchemy import create_engine

PATH_ALL_CODE = r'C:\Users\zzw\Desktop\allcode.csv'
# the following constant be used in fenshijunxian model
URL = 'http://hq.sinajs.cn/list='
PAGE_NUMBERS = 100
REDUNDANT_NUMBERS_CHARS_IN_LINE = 4
INTERVAL_SECONDS = 60
ENGINE = create_engine('mysql://root:@localhost/stockdata?charset=utf8')
MIN_RATIO_BETWEEN_CLOSE_AND_AVP = 0.996   # This constant is used in fenshijunxian mode and mead the gap between close and avarage price