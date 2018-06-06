'''
1 名称空间Namespaces
    存放名字与值绑定关系的地方

2 名称空间的分类
    内置名称空间：
        存放python解释器自带名字,比如内置的函数名:len，max，sum
        创建：随着python解释器启动而创建
        销毁：随着python解释器关闭而销毁

    全局名称空间
        存放文件级别的名字，比如x，f1，z
        x=1

        def f1():
            y=2

        if x == 1:
            z=3

        创建：文件开始执行时则立即创建
        销毁：文件开始执行完毕时则销毁

    局部名称空间
        存放函数内的名字，强调函数的参数也属于局部的
        创建：函数执行时才临时创建
        销毁：函数执行完毕则立即销毁

        def f1():
            x=1
            y=2
            z=3

        f1()


3 名称空间的加载顺序
    内置名称空间---》全局名称空间-----》局部名称空间

    加载的目的是为了吧名字存起来，然而存起的目的就是为取
    那么但凡查找一个名字一定会从三种名称空间之一找到

4、名称空间的查找名字顺序

    局部名称空间====》全局名称空间===》内置名称空间


'''
# len=10
# def f1():
#     # len=3
#     print(len)
#
# f1()


# len=10
# def f1():
#     len=100
#     def f2():
#         # len=1000
#         def f3():
#             # len=10000
#             print(len)
#         f3()
#     len=200
#     f2()
# # len=111111111111111111111111111111
#
# f1()


# 名字的查找关系是在函数定义阶段就已经固定死的，与调用位置无关

# x=100
# def f1():
#     # x=10
#     print(x)
#
#
# def f2():
#     x=11111
#     f1()
#
# f2()
#
# x=1000



# 作用域：域=范围
# 全局范围：内置名称空间中的名字，全局名称空间中的名字
# 特点：全局有效，全局存活


# 局部范围：局部名称空间中的名字
# 特点：局部有效，临时存活

# 定义在全局作用域的名字称为全局变量
# 定义在局部作用域的名字称为局部变量


# x=1
# def f1():
#     print(len)
#     print(x)
# def f2():
#     print(len)
#     print(x)
# def f3():
#     def f4():
#         print(len)
#         print(x)
#     f4()
#

# x=111111111111111111111111111111111111111111111111111111
# print(globals()) #查看全局作用域中的名字

# print(locals() is globals())

# def f1():
#     y=2
#     z=3
#     print(locals())
#
# f1()



# global与nonlocal

# l=[]
# def foo():
#    l.append(2)
#
# foo()
# print(l)


# x=10
# def foo():
#     x=100
#     print(x)
#
# foo()
# print(x)




# x=10
# def foo():
#     global x
#     x=100
#
# foo()
# print(x)


def f1():
    # x=10
    def f2():
        def f3():
            nonlocal x # nonlocal会从当前外一层开始查找一直找到最外层的函数，如果还没有则报错
            x=11
        f3()
    f2()
    # print(x)

f1()
