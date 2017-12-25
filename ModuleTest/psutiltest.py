#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import psutil

# 查看系统相关信息

# cpu逻辑数量
print(psutil.cpu_count())
# cpu物理核心
print(psutil.cpu_count(logical=False))
# cpu用户/系统/空闲时间
print(psutil.cpu_times())

# for i in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))

# 物理内存
print(psutil.virtual_memory())
# 交换内存
print(psutil.swap_memory())


# 磁盘分区信息
print(psutil.disk_partitions())
# 磁盘使用情况
print(psutil.disk_usage(r'c:'))
# 磁盘IO
print(psutil.disk_io_counters())

# 获取网络读写字节／包的个数
print(psutil.net_io_counters())
# 获取网络接口信息
print(psutil.net_if_addrs())
# 获取网络接口状态
print(psutil.net_if_stats())

# 获取当前网络连接信息
print(psutil.net_connections())


# 获取进程
print(psutil.pids())
print(psutil.test())