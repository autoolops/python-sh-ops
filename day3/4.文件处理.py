#!/usr/bin/env python
# Author:YongFu Wang
# Date: 2018/4/14
# -*- coding: utf-8 -*-


#  open('文件的路径',mode=文件的打开模式,encoding=字符编码)

#以下操作涉及两方面的资源
#1. 操作系统需要打开文件
#2. f 就是python 的一个变量

# f = open('/Users/55haitao/Documents/python-sh-ops/day3/a.txt',mode='r',encoding='utf-8')
# data =f.read()
# print(data)
# f.close() #回收操作系统资源


#打开文件后取完数据自动关闭文件
#with  open(文件1) as f,open(文件2) as f1: 可以同时打开多个文件
# with open('/Users/55haitao/Documents/python-sh-ops/day3/a.txt',mode='r',encoding='utf-8') as f:
#     data = f.read()
#     print(data)







