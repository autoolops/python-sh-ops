#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/5 15:43
# FileName: 6. 列表生成式、字典生成式、生成器表达式.py



#列表生成式

# l = ['wyf%s' %i for  i   in range(10)]
# l1 = [ i for  i   in range(10)]
# l2 = [ i**2 for  i   in range(10)]
# print(l)
# print(l1)
# print(l2)

#练习
# 1、将names=['egon','alex_sb','wupeiqi','yuanhao']中的名字全部变大写
# names=['egon','alex_sb','wupeiqi','yuanhao']
# names=[name.upper() for name  in  names]
# print(names)

# 2、将names=['egon','alex_sb','wupeiqi','yuanhao']中以sb结尾的名字过滤掉，然后保存剩下的名字长度
# names=['egon','alex_sb','wupeiqi','yuanhao']
# names = [len(name) for name in names if not name.endswith('sb') ]
# print(names)



#字典生成式
# userinfo=[('egon','123'),('alex','456'),('wxx','679')]
# dic={ k:v for k,v in userinfo }
# print(dic)


#生成器表达式

with open('a.txt','r',encoding="utf-8") as  f:
    nums = (len(line) for line  in f)
    print(max(nums))


