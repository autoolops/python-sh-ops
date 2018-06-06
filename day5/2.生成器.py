#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/5 11:52
# FileName: 2.生成器.py


'''

    1.什么是生成器
        在函数内但凡有yield关键字，在调用函数就不会执行函数体内代码，得到返回值就是一个迭代器对象


'''




def  func():
    # try:
    print('fisrt')
    yield  1
    print('second')
    yield 2
    print('third')
    # except StopIteration:
    #     break

g = func()
res1 = next(g)
print(res1)
res2 = next(g)
print(res2)
res3 = next(g)
print(res3)