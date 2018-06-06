#!/usr/bin/env python
# Author:YongFu Wang
# Date: 2018/4/14
# -*- coding: utf-8 -*-



#1.   r: 默认打开模式,只读模式
# f = open('/Users/55haitao/Documents/python-sh-ops/day3/a.txt' ,mode='r' ,encoding='utf-8')

# print(f.readable())  #判断是否可读
# print(f.writable())  #判断是否可写
# print(f.read())   #一次性将文件读到应用程序内存中
# print(f.readline())    #一次读一行
# print(f.readlines())     #一次读多好，处理后成字典


#2.  w:只写模式,文件存在则清空，不存在则创建

# f = open('/Users/55haitao/Documents/python-sh-ops/day3/b.txt' ,mode='w' ,encoding='utf-8')
# print(f.writable())
# print(f.readable())
#
# print(f.write('wangyongfu\n'))
# print(f.write('xiaofang'))

####
# info = ['wangyongfu\n','zhangshan\n','lisi\n','xiaofang']
# f.writelines(info)     #



#3.  a:只追加模式,文件存在则指针直接移动到文件末尾，不存在则创建文件
# f = open('access.log' ,mode='w' ,encoding='utf-8')
# print(f.readable())
# print(f.writable())
# print(f.write('wangyongfu\n'))
# print(f.write('xiaofang\n'))


#4. 控制文件读写单位的两种模式
#4.1  t  默认模式，文本为单位





#4.2  b 二进制模式，该模式写读写都是bytes,该模式下不能指定encoding  ,跨平台配合使用

with  open('1.png' ,mode='rb') as f:
    data = f.read()
    print(data)
    print(type(data))


# with  open('c.txt' ,mode='wb') as f:
#   data = f.write('你好hello'.encode('utf-8'))
#   print(data)
#   print(type(data))


# with open('c.txt' ,mode='rb') as  f:
#     data = f.read()
#     print(data)
#     print(type(data))
#     print(data.decode('utf-8'))












































