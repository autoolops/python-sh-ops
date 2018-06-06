'''
1、什么是生成器
    在函数内但凡有yield关键字，再调用函数就不会执行函数体代码，得到返回值就是一个生成器对象，
    强调：生成器本质就是迭代器


    next(g)过程：
        会触发生成器g所对应的函数的执行，直到遇到yield才停下来，然后把yiled后的返回值当做
        本次next操作的结果


2、为何要用生成器：
    学习生成器是为了掌握一种自定义迭代器的方式



3、总结yield：
    1、yield提供一种自定义迭代器的方式
    2、与return对比，都能返回值，都能返回多个值，都没有类型限制，而return只能返回一次值，而yield可以返回多次值（yield可以
    帮我们保存函数的执行状态）

'''
def func():
    print('first')
    yield 1 # 暂停
    print('second')

    yield 2 # 暂停
    print('third')


# g=func()
# print(g)

# res1=next(g) #g.__next__()
# print(res1)
#
# res2=next(g) #g.__next__()
# print(res2)
#
# res3=next(g) #g.__next__()


# g=func()
# for item in g: #item=next(g)
#     print(item)

'''
first
1
second
2
third
'''


# range(1,100,2)
# # python2的做法
# def my_range(start,stop,step=1):
#     res=[]
#     while start < stop:
#         res.append(start)
#         start+=step
#     return res
#
#
# res=my_range(1,1000,2)
#
# print(res)

# python3的做法
def my_range(start,stop,step=1):
    # print('开始运行')
    while start < stop:
        yield start
        start+=step

    # print('结束运行')

# obj=my_range(1,1000,2)

# res1=next(obj)
# print(res1)
#
# res2=next(obj)
# print(res2)

for item in my_range(1,10,2):
    print(item)