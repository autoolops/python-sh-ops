#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : YongFu  Wang
# @Time    : 2018/4/21 15:48
# @FileName: 7.函数对象.py

'''
1.函数对象：函数可以当作变量去处理




'''

#1.1函数可以被赋值
# def foo():
#     print('from foo')
# f=foo
# # print(f)
# f()

#1.2可以当作一个参数传给函数

# def foo():
#     print('from foo')
#
# def bar(func):
#     func()
#
# bar(foo)

#1.3 可以当作函数的返回值
#
# def foo():
#     print('from foo')
#
# def bar(func):
#     return  func
#
# f= bar(foo)
# print(f)

#1.4 可以当作容器类型元素

def put():
    print('from put')

def get():
    print('from get')

def ls():
    print('from ls')

def login():
    print('from login')

def cd():
    print('from cd')


func_dic ={
    "1":[get,'下载'],
    "2":[put,'上传'],
    "3":[ls,'浏览'],
    "4":[login,'登陆'],
    "5":[cd,'切换目录'],

}

def run():
    while True:
        for k in func_dic:
            print(k,func_dic[k][1])
        choice = input('>>>').strip()
        if choice == 'q':break
        if choice in func_dic:
            func_dic[choice][0]()

run()

