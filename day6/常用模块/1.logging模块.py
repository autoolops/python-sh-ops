#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/12 14:19
# FileName: 1.logging模块.py
import logging

#critical:50
#error:40
#warning:30
#info:20
#debug:10

# logging.basicConfig(
#     filename='access.log',
#     format='%(asctime)s - %(name)s - %(levelname)s - %(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level=10,
#     stream=True
# )

# logging.debug('debug级别')
# logging.info('info级别')
# logging.warning('warning级别')
# logging.error('error级别')
# logging.critical('critical级别')


#1.  logger对象：用来产生日志
logger1=logging.getLogger('银行业务相关')  # 日志名是用告诉我们所记录的日志到底是属于哪一类业务相关的信息

#filter对象：过滤日志

#2.  handler对象：控制日志的去向：1 文件 2 终端
fh1=logging.FileHandler('a.log',encoding='utf-8')
fh2=logging.FileHandler('b.log',encoding='utf-8')

ch=logging.StreamHandler() #代表的就是终端

#3.   建立logger对象与handler对象的绑定关系
logger1.addHandler(fh1)
logger1.addHandler(fh2)
logger1.addHandler(ch)

#4.  formmatter对象：定制日志的格式
formatter1 = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p'
)
formatter2 = logging.Formatter(
    fmt='%(asctime)s ===> %(message)s',
)

#5.   为handler对象绑定日志格式
fh1.setFormatter(formatter1)
fh2.setFormatter(formatter2)
ch.setFormatter(formatter2)



#6.   设置日志级别：两层关卡，第一次是logger，第二层是handler，只有两层都放行，最终日志才会打印
# logger1.setLevel(50)
# fh1.setLevel(10)
# fh2.setLevel(10)
# ch.setLevel(10)

logger1.setLevel(10)
fh1.setLevel(10)
fh2.setLevel(10)
ch.setLevel(10)


#7.   调用logger对象产生日志
logger1.debug('这是一条debug日志')



