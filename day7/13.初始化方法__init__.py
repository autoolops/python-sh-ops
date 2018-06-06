#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/19 18:29
# FileName: 13.初始化方法__init__.py


class SchoolOldboy:
    school = 'Oldboy'

    def __init__(self, x, y, z):
        self.name = x
        self.sex = y
        self.age = z

    def choose_curse(self):
        print('is chooseing course')


stu1 = SchoolOldboy('zhangsan','male',18)
stu2 = SchoolOldboy('lisi','female',28)
stu3 = SchoolOldboy('wangwu','male',27)

print(stu1.__dict__)
print(stu2.__dict__)
print(stu3.__dict__)



