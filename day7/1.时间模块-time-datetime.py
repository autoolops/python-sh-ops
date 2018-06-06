#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/19 09:46
# FileName: 1.时间模块-time-datetime.py

import   time
import  datetime


#
print(time.time())  ##unix 时间戳
# print(time.strftime("%Y_%m_%d"))  ##格式化时间
# print(time.localtime())  ##结构化时间
# print(time.localtime().tm_year)  ##结构化时间，中国标准时间
#
# print(time.gmtime())  ##时间标准时间，和结构化时间相差8小时
#
#



##时间转换

# localtime([secs])
# 将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
# time.localtime()
# time.localtime(1473525444.037215)

# gmtime([secs]) 和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。

# mktime(t) : 将一个struct_time转化为时间戳。
# print(time.mktime(time.localtime()))
#

# strftime(format[, t]) : 把一个代表时间的元组或者struct_time（如由time.localtime()和
# time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个
# 元素越界，ValueError的错误将会被抛出

# print(time.strftime("%Y-%m-%d %X", time.localtime()))#2016-09-11 00:49:56
# print(time.strftime("%Y-%m-%d %X"),time.localtime())#2016-09-11 00:49:56

# time.strptime(string[, format])
# 把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
# print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))
#在这个函数中，format默认为："%a %b %d %H:%M:%S %Y"。




##datetime

print(datetime.datetime.now())   #获取当前时间
# print(datetime.datetime.now() + datetime.timedelta(days=3))   #当前时间+3天
# print(datetime.datetime.now() + datetime.timedelta(days=-3))   #当前时间-3天
# print(datetime.datetime.now().replace(year=2011))  #任意替换每个阶段的时间
# print(datetime.datetime.fromtimestamp(11111111))   # 时间戳直接转成日期格式 2016-08-19





