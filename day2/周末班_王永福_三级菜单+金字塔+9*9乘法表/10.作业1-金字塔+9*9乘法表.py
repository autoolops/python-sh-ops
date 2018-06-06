#!/usr/bin/env python
# Author:YongFu Wang
# Date: 2018/4/10
# -*- coding: utf-8 -*-

#9*9 乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" %(i,j,i*j),end=" ")
    print(" ")




#打印金字塔
#方法1
n = int(input('请输入一个数字,打印你想要的金字塔:'))
for i in range(1,n+1):
        for k in range(n-i):
                print(' ',end="")
        for j in range(2*i-1):
                print('*',end="")
        print(" ")


#方法2
n = int(input('请输入一个数字,打印你想要的金字塔:'))
for i in range(1, n):
    print(' ' * (n - (i - 1)) + '*' * (2 * i - 1))










