'''
1、什么是迭代器
    迭代的工具

    什么是迭代？
        迭代是一个重复的过程，每一次重复都是基于上一次结果而进行的

        # 单纯的重复并不是迭代
        while True:
            print('=====>')

2、为什么要用迭代器
    找到一种可以不依赖索引的迭代取值方式


3、怎么用迭代器
    可迭代对象？
        在python中，但凡内置有__iter__方法对象，都是可迭代的对象

    迭代器对象？
        执行可迭代对象下__iter__方法得到的返回值就是一个迭代器对象

        迭代器对象内置
            __next__方法
            __iter__方法,执行该方法得到仍然是迭代器本身，干什么用？？



    迭代器对象一定是可迭代的对象
    可迭代的对象不一定是迭代器对象
'''

# l=['a','b','c']
# l='hello'
# l=('a','b','c','d','e')
# l={'a':1,'b':2,'c':3}
# i=0
# while i < len(l):
#     print(l[i])
#     i+=1


a=1
b=1.1
# 以下都是可迭代的对象
c='hello'
d=[1,2,3]
e=(1,2,3)
d={'a':1}
g={1,2,3}
f=open('aa.py','rb') # 本身就是迭代器对象





# 执行可迭代对象的__iter__方法得到迭代器对象
# dic={'k1':1,'k2':2,'k3':3}
# iter_obj=dic.__iter__()
#
# # print(iter_obj)
#
# print(iter_obj.__next__())
#
# print(iter_obj.__next__())
#
# print(iter_obj.__next__())
# print(iter_obj.__next__())




# f=open('aa.py','rt',encoding='utf-8')
# iter_obj=f.__iter__()
#
# print(iter_obj.__next__(),end='')
# print(iter_obj.__next__(),end='')
# print(iter_obj.__next__(),end='')


# 基于迭代器的迭代取值方式
dic={'k1':1,'k2':2,'k3':3}


# iter_obj=dic.__iter__()
# # print(iter_obj.__iter__().__iter__().__iter__().__iter__() is iter_obj)
#
# while True:
#     try:
#         print(iter_obj.__next__())
#     except StopIteration:
#         break

#for循环的底层运行机制：for循环可以称之为迭代器循环
#1、先调用in后那个对象的__iter__方法，得到该对象的迭代器对象
#2、执行迭代器对象的__next__方法，将得到的返回值赋值in前面的变量名，然后执行一次循环体代码
#3、循环往复，直到取干净迭代器内所有的值，自动捕捉异常结束循环

# for k in dic: #iter_obj=dic.__iter__()
#     print(k)

#
# for x in 10:
#     pass


# f=open('aa.py','rt',encoding='utf-8')
# for line in f:
#     print(line)


# 示范一
# dic={'k1':1,'k2':2,'k3':3}
# iter_obj=dic.__iter__()
#
# print('第一次迭代iter_obj')
# for k in iter_obj: #iter_obj.__iter__()
#     print(k)
#
# print('第二次迭代iter_obj')
# for k in iter_obj:
#     print(k)


# # 示范二
# dic={'k1':1,'k2':2,'k3':3}
# iter_obj=dic.__iter__()
# print('第一次迭代iter_obj')
# for k in iter_obj:
#     print(k)
#
# iter_obj=dic.__iter__()
# print('第二次迭代iter_obj')
# for k in iter_obj:
#     print(k)



# 示范三
# dic={'k1':1,'k2':2,'k3':3}
#
# print('第一次迭代')
# for k in dic: #dic.__iter__()
#     print(k)
#
#
# print('第二次迭代')
# for k in dic:
#     print(k)


#总结迭代器的优缺点：
#优点：
#1、提供一种不依赖与索引的迭代取值方式====》应用于for循环
#2、节省内存
l=[1,2,3,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]

# obj=l.__iter__()

# f=open('aa.py')
# print(f.__next__())

# f.readline()
# for line in f:
#     print(line)


for i in range(1,10000):
    print(i)
# 缺点：
#1、只能往后取，不能往前取，是一次性的，值取值干净后无法再次取值，除非重新得到新的迭代器对象,
    # 不如按照索引取值的方式灵活

#2、值取不干净，永远无法预测迭代器的长度



