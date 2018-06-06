#1、导入模块：import 模块名
#2、首次导入模块都发生了哪些事？
#2.1 先产生一个模块的名称空间
#2.2 会执行模块文件的代码，将产生的名字放到模块的名称空间中
#2.3 会在当前名称空间中拿到一个模块名，该模块名指向模块的名称空间
# x=1
# y=2
#
# import spam
# import spam
# import spam


#2、如何使用模块
import spam

# 模块名.名字，是在向模块的名称空间中拿名字
# money=0
# print(spam.money)
# print(spam.read1)
# print(spam.read2)
# print(spam.change)


# 但凡来自于spam名称空间中的功能，执行时都是模块自己的名称空间为准的
# money=111111111111111111111111
# spam.read1()

# spam.change()
# print(money)
# spam.read1()


# def read1():
#     print('02 import 导入模块.py read1')
#
# spam.read2()


# import导入模块的方式，在引用模块名称空间中改名字时，必须加上前缀：模块名.
# 优点：指名道姓地访问模块名称空间中的名字，肯定不会与当前名称空间中名字冲突
# import spam
# money=11111111111111
# print(spam.money)

# 缺点：每次引用模块名称空间中的名字都需要加上前缀，在模块名过长时，前缀会显得非常臃肿
# import spam as sm
# print(sm.money)




# 模块用逗号分隔一次性导入多个模块
# import spam,os,time
# 推荐多行导入
import spam
import os
import time