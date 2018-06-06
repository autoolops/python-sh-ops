#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/5 14:53
# FileName: 3.yield 表达式的应用.py


def  dog(name):
    food_list = []
    while True:
        food = yield food_list
        print('狗哥 %s 吃了 %s' %(name,food))
        food_list.append(food)


g= dog('alex')
print(g)
res = next(g)
print(res)


res1=g.send('骨头')
print(res1)

res2=g.send('骨头2')
print(res2)

res3=g.send('骨头3')
print(res3)