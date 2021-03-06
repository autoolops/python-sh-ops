#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : YongFu  Wang
# @Time    : 2018/4/21 11:36
# @FileName: 4.函数参数.py



#1.函数分为两大类：形参和实参
# 形参：指的是在定义函数时括号内定义的参数 ,形参即变量名
# def  foo(x,y):
#     print(x,y)


# 实参：指的是在调用参数时括内传入的参数，实参即变量值
# foo(1,2)


#在函数调用时，实参会传给形参，即变量的赋值



#2.函数参数

#2.1位置参数
#在函数定义式，按照位置顺序从左到右依次定义的参数，称为位置实参
#特点：与形参一一对应


#2.2 关键字实参
#在调用函数时，按照key= values 的形式定义，称为关键字实参




#3.3位置实参可以和关键字实参混合使用
#3.3.1 位置参数一定放到关键字参数前面

#3.3.2 同一个形参只能被赋值一次





#位置形参与默认参数的应用



# *:接受溢出位置实参，存成元组形式，然后赋值给*后面跟的变量名

# *在实参中的应用
# def foo(x,y,*z):
#     print(x,y)
#     print(z)
#
# foo(1,2,3,4,5)


# *在实参中的应用
# def foo(x,y,*z):
#     print(x,y)
#     print(z)
#
# foo(1,2,*(3,4,5,6))

# ** 在形参中的应用
# def foo(x,y,**z):
#     print(x,y)
#     print(z)
# foo(1,a=1,b=2,c=3,y=5)



# **在实参中的应用
# def foo(x,y,**z):
#     print(x,y)
#     print(z)
#
# foo(1,2,**{'a':3,'b':4,'c':5})




#
def foo(*args,**kwargs):
    print(args)
    print(kwargs)
