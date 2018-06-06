
#1、return
#特点:return 是函数结束的标志，函数内可以有多个return
#但只要执行一个，函数就立即结束，并且把return后的值当做本次调用的结果返回

# def foo():
#     print('first')
#     return 1
#     print('second')
#     return 2
#     print('third')
#     return 3
#
# res=foo()
# print(res)

#2、返回值注意：
#2.1 返回值没有类型限制
# def bar():
#     return {'x':1}
#
# print(bar())

#2.2 返回值没有个数限制，可以用逗号分开多个值 一次返回
# def bar():
#     return (1,'wxx',{'x':1})
#
# x,y,z=bar()
# print(x,y,z)

#2.3 可以没有return,默认返回None
def bar():
    pass

res=bar()
print(res)