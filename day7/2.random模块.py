#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/19 10:17
# FileName: 2.random模块.py
import  random

#
# print(random.random())
# print(random.uniform(1,3))
# print(random.randint(1,3))
# print(random.randrange(1,3))
# print(random.choice([1,'a','b']))
# print(random.sample([1,'a','b'],2))


# l = [1,2,3,4,5]
# random.shuffle(l)
# print(l)
#


def make_code(n):
    res = ''
    for i in range(n):
        s1 = str(random.randint(0, 9))
        s2 = chr(random.randint(65, 95))
        res += random.choice([s1,s2])
    return res



print(make_code(5))