#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/26 16:07
# FileName: 封装.py

#
# class Foo:
#     __n =1
#     def __init__(self,name):
#         self.__name = name
#
#
#     def _f1(self):
#         print('f1')




class Foo:
    def __f1(self):
        print('Foo,f1')

    def f2(self):
        print('Foo,f2')
        self.__f1()


class Bar(Foo):
    def __f1(self):
        print('Bar,f1')


obj=Bar()
obj.f2()