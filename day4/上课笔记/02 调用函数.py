#调用形式一：语句形式
# def foo():
#     print('from foo')
#
# foo()



# 调用形式二：表达式形式
def max2(x,y): #x=3000  y=2000
    if x > y:
        # print(x)
        return x
    else:
        # print(y)
        return y
#
# salary=max2(3000,2000)
# annual_salary=salary * 12
# print(annual_salary)

# annual_salary=max2(3000,2000) * 12
# print(annual_salary)

# 调用形式三：当做参数传给另外一个函数
def max2(x,y): #x=3000  y=2000
    if x > y:
        # print(x)
        return x
    else:
        # print(y)
        return y

#3 2 1
res=max2(max2(3,2),1)

print(res)





