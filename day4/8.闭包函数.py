#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : YongFu  Wang
# @Time    : 2018/4/21 17:47
# @FileName: 8.闭包函数.py


'''
闭包函数 = 嵌套函数+ 名称空间与作用域 +函数对象

1.什么是闭包函数
    1、定义在函数内部的函数
    2、该函数提代码包含对该函数外层作用域中的名字引用
        强调： 函数外层指的不是全局作用域
    满足上述两个条件，那么内部函数就称为闭包函数

'''
#
# def  outter():
#     x = 1
#     def inner():
#         print(x)
#     return  inner  # 利用函数对象的感念，将一个内部函数返回并在全局拿来使用，从而打破函数的层级限制
#
# f = outter()
# print(f)
# f()
#
#
# def foo():
#     print('from foo')
#     f()
#
# foo()





#为函数体传值的方式

#方式一
import  requests


def get(url)















