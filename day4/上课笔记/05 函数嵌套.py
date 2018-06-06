#1 函数的嵌套调用
# def max2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
# def max4(x,y,m,n):
#     res1=max2(x,y)
#     res2=max2(res1,m)
#     res3=max2(res2,n)
#     return res3
#
# print(max4(1,2,3,4))

#2 函数的嵌套定义
def f1():
    print('from f1')
    def f2():
        print('from f2')
        def f3():
            print('from f3')
        f3()
    f2()
# f1()


'''
from f1
from f2
from f3
'''

