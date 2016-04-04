from time import strptime, strftime
def calculate_sleep_loop(para_time):
    today = str(para_time.tm_year)+str(para_time.tm_mon)+str(para_time.tm_mday)
    t1 = strptime('%s 09:31:00' % today, '%Y%m%d %H:%M:%S')
    t2 = strptime('%s 11:31:00' % today, '%Y%m%d %H:%M:%S')
    t3 = strptime('%s 13:01:00' % today, '%Y%m%d %H:%M:%S')
    t4 = strptime('%s 15:01:00' % today, '%Y%m%d %H:%M:%S')
    if para_time < t1:
        delay_sec = get_seconds(t1, para_time)
        loop_times = 240
    elif t1 <= para_time < t2 or t3 <= para_time < t4:
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

def get_today_1min_table_name():
    today = strftime("%Y%m%d")
    table_name = '1_min'+'_'+today
    return table_name
