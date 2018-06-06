#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/26 14:32
# FileName: 4.组合.py


import  pickle

class OldboyPepole:
    school = 'oldboy'

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def save(self):
        with open('%s' % self.name,'wb') as  f:
            pickle.dump(self,f)


class OldboyStudent(OldboyPepole):
    def __init__(self,name,age,sex):
        OldboyPepole.__init__(self,name,age,sex)
        self.course = []

    def choose_course(self,course):
        print('%s is choosing course:%s' %(self.name,course))



class OldboyTearch(OldboyPepole):
    def __init__(self,name,age,sex,level):
        OldboyPepole.__init__(self,name,age,sex)
        self.level=level

    def score(self,course):
        print('%s is score %s ' %(self,name,stu,name))



class Course:
    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period

    def tell_info(self):
        print('''
            课程名：%s
            价钱：%s
            周期：%s
        ''' %(self.name,self.price,self.period))



python = Course('python',8000,'5month')
linux = Course('linux',1000,'4month')

#
# python.tell_info()
# linux.tell_info()
#

stu1 = OldboyStudent('张三',18,'male')
stu1.course.append(linux)
stu1.course.append(python)
# print(stu1.course)
print('张三选择的课程如下：')
for course in stu1.course:
    course.tell_info()


stu2 = OldboyStudent('李四',28,'female')
stu2.course.append(python)
# print(stu2.course)
print('李四选择的课程如下：')
for course in stu2.course:
    course.tell_info()



