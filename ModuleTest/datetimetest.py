#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
from datetime import datetime, timedelta, timezone

# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
print(utc_dt.timestamp())

# 拿到utc时间，并强制设置时区为UTC+9:00:
print('---')
tz_utc_9 = timezone(timedelta(hours=9))
print(tz_utc_9)
utc_dt_dd = datetime.utcnow().replace(tzinfo=tz_utc_9)
print(utc_dt_dd)
print(utc_dt_dd.timestamp())
print('----')

# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=-8)))
print(bj_dt)
print(bj_dt.timestamp())


# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)


# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


def to_timestamp(dt_str, tz_str):
    utc = re.match(r'^UTC([\+\-][01]*?[0-9]):00', tz_str)
    #print(float(utc.group(1)))
    dt_zone = timezone(timedelta(hours=float(utc.group(1))))
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=dt_zone)
    return dt.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')