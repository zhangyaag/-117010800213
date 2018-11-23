
import numpy as np
from datetime import datetime
from datetime import timedelta
 
# 1) 获取当前日期和时间
now = datetime.now()  # 返回当前日期和时间
print('1)')
print('当前时间 :', now)
 
# 2) 获取指定日期和时间
dt = datetime(2017, 5, 28, 23, 10, 54)
print('2)')
print('指定时间 :', dt)
 
# 3) datetime转换为timestamp
dt_stamp = dt.timestamp()
print('3)')
print('指定时间对应时间戳 :', dt_stamp)
 
# 4) timestamp转换为datetime
t = 163423625
print('4)')
print('时间戳 :', t)
print('对应本地时间 :', datetime.fromtimestamp(t))
print('UTC标准时间 :', datetime.utcfromtimestamp(t))
print('weekOfDay :', datetime.fromtimestamp(t).weekday())
 
# 5) str转换为datetime
day = datetime.strptime('2016-12-2 15:45:35', '%Y-%m-%d %H:%M:%S')
print('5)')
print(day)
 
# 6) datetime转换为str
now = datetime.now()
print('6)')
print('当前时间 :', now)
print(now.strftime('%A, %B %d %H:%M, %Y'))
 
# 7) datetime加减
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
now = datetime.now()
print('7)')
print('当前时间 :', now)
now_stamp = now.timestamp()
print('时间戳 :', now_stamp)
np.savetxt('now_stamp.txt', np.array([now_stamp]))
t = now + timedelta(days=1, hours=8, minutes=5, seconds=20)
print('1天8小时5分20秒之后的时间 :', t)
