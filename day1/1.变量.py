#!/usr/bin/env python
# Author:YongFu Wang
# Date: 2018/3/31
# -*- coding: utf-8 -*-

'''
1.什么是变量
    变量就是变化的量
    量: 表达某种状态
    变： 状态一直在发生变化
'''
# 2. 如何定义变量，分成三部分
#变量名 ：
#赋值符号赋 ：
#值 ：数据，用来表示某种状态

#3. 垃圾回收机制： python 解释器会定期清理引用计数为0的值

#4. 定义一份变量都有三个特征：
#id
#type
#值
# age = 18
# print(id(age))
# print(type(age))
# print(age)
#
# age1 = age
# print(id(age))
# print(type(age))
# print(age)

# is  与 ==
#==：判断值是否相等
#is：判断id是否相等
# 定义两个变量，值相等，如果数据量小，并且在短时间内会被调用，python优化机制，会调用同一个值，避免内存浪费
# info = 'hello'
# info1 = 'hello'
# print(id(info),id(info1))
# print(info is info1)

#5.变量的命名规范
#强调： 变量名一定要能反映变量值表示的状态
#5.1 变量名只能是字母、数字或下划线的任意组合；
#5.2 变量名的第一个字母不能数数字
#5.3 关键字不能声明为变量

#6. 两种定义方式
#驼峰体
# AgeOfWang = 11
#下划线
# age_of _wang = 12


# 7.  常量  ： 不变的量

