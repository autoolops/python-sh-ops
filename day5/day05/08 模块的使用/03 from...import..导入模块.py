
#==============================第一部分
# x=1
# y=2
# from spam import money,read1,read2,change
# #1、from。。。import。。。首次导入模块也做三件事：
# #1.1 先产生一个模块的名称空间
# #1.2 会执行模块文件的代码，将产生的名字放到模块的名称空间中
# #1.3 会在当前名称空间中直接拿到一个模块名称空间中的名字
# money=1
#
# #2、使用:可以不用加前缀直接使用
# # print(money)
# # print(read1)
# # print(read2)
# #优点：简洁
# #缺点: 容易与当前名称空间中的名字冲突
#
#
# # 强调强调强调：来自于模块名称空间中的函数一定是模块的名称空间为准的
# # read1()
# change()
# read1()
# # print(money)


#==============================第二部分
# from spam import *
#
# # print(money)
# # print(read1)
# # print(read2)
# # print(change)
# # 不推荐使用*，除非在我们需要引入模块中很多名字时，可以用*起到一个节省代码的作用


#==============================第三部分(了解)
from spam import *

print(money,read1)
print(read2)

#==============================第四部分
# from spam import money as m
# print(m)

