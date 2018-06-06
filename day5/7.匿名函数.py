#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/5 16:38
# FileName: 7.匿名函数.py


salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}


#max()函数使用
# def  func(k):
#     return salaries[k]
#
# print(max(salaries,key=lambda x:salaries[x]))
# print(min(salaries,key=lambda x:salaries[x]))




#sorted应用
# print(sorted(salaries,key=lambda  x:salaries[x]))
# print(sorted(salaries,key=lambda  x:salaries[x],reverse=True))



#map应用
# names = ['alex','wupeiqi','yuanhao','liuqingzheng']
# l = [name+ '_sb' for  name  in names]
# print(l)
#
# obj = map(lambda  x:x+'_sb',names)
# print(list(obj))


#filter 的应用

# names = ['alex_sb', 'wupeiqi_sb', 'yuanhao_sb', 'liuqingzheng_sb','wangyongfu']

# l = (name for name in names if name.endswith('sb'))
# print(l)


#filter 会得到names 的迭代器对象obj  然后next(obj) 将得到的值传给filter第一个参数指定的函数
#将函数返回值为True 的那个值留下

# res = filter(lambda  x:x.endswith('sb'),names)
# print(list(res))



