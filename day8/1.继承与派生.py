#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/26 11:18
# FileName: 1.继承与派生.py



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
    def choose_course(self,course):
        print('%s is choosing course:%s' %(self.name,course))



class OldboyTearch(OldboyPepole):
    def __init__(self,name,age,sex,level):
        OldboyPepole.__init__(self,name,age,sex)
        self.level=level

    def score(self,course):
        print('%s is score %s ' %(self,name,stu,name))



stu1 =  OldboyTearch('wyf1',18,'man',10)
stu1.save()

