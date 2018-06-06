#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/5 10:30
# FileName: 1.迭代器.py


'''

    什么是迭代：
        迭代是一个重复的过程，每一次迭代都是基于上一次迭代的结果而进行的
    为什么要用迭代器：
        找到一种不依赖索引的迭代取值方式
    可迭代对象：
        在python中，但凡内置__iter__ 方法的对象,都是可迭代对象
    迭代器对象：
            执行可迭代对象__iter__方法得到的返回值就是一个迭代器对象
            迭代器对象内置有__next__方法


'''

#基于迭代器的迭代取之方式
dic = {'k1':1,'k2':2,'k3':3}
iter_obj= dic.__iter__()


while True:
    try:
        next_obj = iter_obj.__next__()
        print(next_obj)
    except StopIteration:
        break
