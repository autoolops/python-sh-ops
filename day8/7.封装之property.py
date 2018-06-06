#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/26 17:01
# FileName: 7.封装之property.py




# class People:
#     def __init__(self,name,height,weight):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
#
# egon = People('ehon',1.80,75)
# print(egon.bmi)




class People:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self,val):
        if type(val) is not str:
            raise TypeError('名字的值必须为str类型')
        self.__name=val

    @name.deleter
    def name(self):
        print('不能删除')

p = People('egon')
# p.name = "EGON"
# print(p.name)


del p.name
print(p.name)