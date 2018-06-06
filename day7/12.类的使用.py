#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/19 17:49
# FileName: 12.类的使用.py



#用途一   类本身就是一个容器，所以可以增删改查
# class SchoolOldboy:
#     school = 'Oldboy'
#     def choose_curse(self):
#         print('is chooseing course')
#
#
#
#
# # print(SchoolOldboy.__dict__)
# # print(SchoolOldboy.__dict__['school'])
# # print(SchoolOldboy.__dict__['choose_curse'])
# #
# # SchoolOldboy.__dict__['choose_curse'](123)
#
#
# SchoolOldboy.country='china'
#
# SchoolOldboy.school='Oldgirl'
#
# SchoolOldboy.choose_curse(123)
#
# print(SchoolOldboy.__dict__)
#
# del  SchoolOldboy.school
# print(SchoolOldboy.__dict__)




##用途二  调用类来产生对象，调用类的过程又称为实例化

class SchoolOldboy:
    school = 'Oldboy'
    def choose_curse(self):
        print('is chooseing course')


stu1 = SchoolOldboy()
stu2 = SchoolOldboy()
stu3 = SchoolOldboy()

def init(obj,x,y,z):
    obj.name = x
    obj.sex = y
    obj.age = z


init(stu1,'zhangsan','male','18')
init(stu2,'lisi','female','28')
init(stu3,'wangwu','male','27')

print(stu1.school,id(stu1.school))
print(stu2.school,id(stu2.school))
print(stu3.school,id(stu3.school))


print(stu1.choose_curse,id(stu1.choose_curse))
print(stu2.choose_curse,id(stu2.choose_curse))
print(stu3.choose_curse,id(stu3.choose_curse))












