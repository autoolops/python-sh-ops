#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/19 15:22
# FileName: 7.configparser模块.py

import configparser



config=configparser.ConfigParser()
config.read('b.cfg')

#查看所有的标题
res = config.sections()
print(res)

#查看标题section1下所有key=value的key
options=config.options('section1')
print(options)


#查看标题section1下user的值=>字符串格式

val=config.get('section1','user')
print(val) #egon


#查看标题section1下age的值=>整数格式

val1 = config.getint('section1','age')
print(val1)


#查看标题section1下is_admin的值=>布尔值格式
val2=config.getboolean('section1','is_admin')
print(val2) #True


#查看标题section1下salary的值=>浮点型格式
val3=config.getfloat('section1','salary')
print(val3) #31.0



