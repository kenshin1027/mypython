from time import sleep, localtime, clock, time, strptime
import numpy as np


def calculate_sleep_loop(para_time):
    today = str(para_time.tm_year)+str(para_time.tm_mon)+str(para_time.tm_mday)
    t1 = strptime('%s 09:31:00' % today, '%Y%m%d %H:%M:%S')
    t2 = strptime('%s 11:31:00' % today, '%Y%m%d %H:%M:%S')
    t3 = strptime('%s 13:01:00' % today, '%Y%m%d %H:%M:%S')
    t4 = strptime('%s 15:01:00' % today, '%Y%m%d %H:%M:%S')
    if para_time < t1:
        delay_sec = get_seconds(t1, para_time)
        loop_times = 240
    elif t1 <= para_time <t2 or t3 <= para_time < t4:
        if para_time.tm_sec <= 2:
            delay_sec = 0
            t_hour = para_time.tm_hour
            t_min = para_time.tm_min
        else:
            delay_sec = 60-para_time.tm_sec
            if para_time.tm_min == 59:
                t_min = 0
                t_hour = para_time.tm_hour+1
            else:
                t_hour = para_time.tm_hour
                t_min = para_time.tm_min+1
        if para_time.tm_hour < 12:
            loop_times = 240-(t_hour*60+t_min-9*60-31)
        else:
            loop_times = 15*60-t_hour*60-t_min+1
    elif t2 <= para_time < t3:
        delay_sec = get_seconds(t3, para_time)
        loop_times = 120
    else:
        return []
    return [delay_sec, loop_times]


def get_seconds(time1, time2):
    return (time1.tm_hour - time2.tm_hour) * 3600 + (time1.tm_min - time2.tm_min) * 60 + time1.tm_sec - time2.tm_sec


for i in range(0, 10):
    t_hour = np.random.randint(8, 16)
    t_min = np.random.randint(0,60)
    t_sec = np.random.randint(0,60)
    mydt = strptime('20160328 %d:%d:%d' % (t_hour, t_min, t_sec), '%Y%m%d %H:%M:%S')
    print mydt
    result = calculate_sleep_loop(mydt)
    if len(result)>0:
        print result
        if result[0] > 60:
            print 'sleep time is %d minutes, %d seconds' % (result[0]/60, result[0]%60)
    else:
        print 'the trading is over'
    print '-------------'

