#一：函数的参数分为两大类：形参与实参
#形参：指的是在定义函数时括号定义的参数，形参即变量名
# def foo(x,y): #x=1,y=2
#     print(x,y)
#实参：指的是在调用函数时括号传入的值，实参即变量值
# foo(1,2)

# 在调用函数时，实参的值会传给形参，这就是一个赋值操作

#二：函数参数
#1、位置参数：
#1.1 在定义函数时，按照从左到右的顺序依次定义的参数，称为位置形参
#特性：位置形参必须被传值，多一个不行少一个也不行
def foo(x,y,z):
    print(x,y,z)


# foo(1,2,3)
# foo(1,2)
# foo(1,2,3,4)
#1.2 在调用函数时，按照从左到右的顺序依次传入的值，称为位置实参
#特点：与形参一一对应
# foo(1,2,3)
# foo(3,2,1)


#2、关键字实参：
#在调用函数时，按照key=value的形式定义的实参，称为关键字参
#特点:
#可以完全打乱顺序,但仍然能指名道姓地为指定的参数传值
def foo(x,y,z):
    print(x,y,z)

# foo(1,2,3)
# foo(z=3,x=1,y=2,)

# 位置实参与关键字实参可以混合使用
# 1、位置参数一定放到关键字参数的前面
# 2、同一个形参只能被赋值一次

# foo(1,2,z=3)
# foo(1,y=2,z=3)
# foo(1,z=3,y=2)

# foo(z=3,y=2,1) # 报错
# foo(1,z=3,y=2)
# foo(1,z=3,y=2,z=30)
# foo(1,z=3,y=2,)
# foo(1,x=3,y=2)


#3 默认参数:在定义函数时，就已经被赋值的参数，称为默认形参
#注意
#3.1 在定义阶段就已经被赋值,意味着在调用阶段就可以不用传值
# def foo(x,y=10):
#     print(x,y)

# foo(1)
# foo(1,3)
# foo(y=4,x=1)

#3.2 默认参数必须跟在位置形参的后面
# def foo(y=1,x):
#     pass

#3.3 默认参数的值只在定义阶段被赋值一次就固定死了,定义之后改变没有影响
# m=10
# def func(x,y=m):
#     print(x)
#     print(y)
# m=1111111
# func(1)


#3.4 默认参数的值应该设置成不可变类型
# def func(name,hobby,l=[]): #['read','play']
#     l.append(hobby)
#     print(name,l)
#
# func('egon','read')
# func('alex','play')
# func('wxx','eat')


def func(name,hobby,l=None):
    if l is None:
        l=[]
    l.append(hobby)
    print(name,l)

# func('egon','read')
# func('alex','play')
# func('wxx','eat')

# func('egon','read',['music','movie'])
# func('wxx','play',['xxx',])


# 位置形参与默认参数的应用:
#1 大多数场景值都固定不变则需要定义成默认参数
#2 大多数场景值都需要改变则需要定义成位置形参
# def register(name,password,gender='male'):
#     print(name)
#     print(password)
#     print(gender)
#
#
# register('alex','123',)
# register('wxx','wxx123',)
# register('lxx','lxx123',)
# register('evia','evia123','female')




#4 可变长参数:
#指的是在调用函数时,传入的实参个数可以不固定
# 而实参无非两种形式:1 位置实参  2 关键字实参
# 所以对应的,形参也必须对应两种解决方案,专门用于接收溢出位置实参和溢出的关键字实参

# *:接收溢出位置实参, 存成元组形式,然后赋值给*后面跟的那个变量名
# 用法1:在形参中用*
# def foo(x,y,*z):  #z=(3,4,5)
#     print(x,y)
#     print(z)

# foo(1,2,3,4,5)
# foo(1,2,3,4,5,6,7,8,9)

# 用法2:在实参中用*
# def foo(x,y,*z):  #z=(3,4,5,)
#     print(x,y)
#     print(z)

# foo(1,2,*(3,4,5,6,7,8,9)) #foo(1,2,3,4,5,6,7,8,9)
# foo(1,2,*[3,4,5]) #foo(1,2,3,4,5)
# foo(1,2,*'abc') #foo(1,2,'a','b','c')


# def foo(x,y,):
#     print(x,y)

# foo(1,*(2,3,4,5)) #foo(1,2,3,4,5)
# foo(1,(2,3,4,5)) #
# foo(*(1,2,3,4,5)) #foo(1,2,3,4,5)


# def my_sum(*args):
#     res=0
#     for n in args:
#         res+=n
#     return res
#
# res1=my_sum(1,2,3)
# res2=my_sum(1,2,3,4)
# res3=my_sum(1,2,3,4,5)
# print(res1)
# print(res2)
# print(res3)


# **:接收溢出关键字实参, 存成字典形式,然后赋值给**后面跟的那个变量名
# 用法1:在形参中用**
# def foo(x,y,**z): # z={'c':4,'b':4,'a':2}
#     print(x)
#     print(y)
#     print(z)
#
#
# foo(1,a=2,b=3,c=4,y=5)

# 用法2:在实参中用**
# def foo(x,y,**z): # z={'c':4,'b':4,'a':2}
#     print(x)
#     print(y)
#     print(z)


# foo(1,{'a':2,'c':3,'b':10,'y':111})
# foo(1,**{'a':2,'c':3,'b':10,'y':111}) #foo(1,y=111,c=3,a=2,b=10)
# foo(1,**{'a':2,'c':3}) #foo(1,c=3,a=2)


# def foo(x,y,z):
#     print(x)
#     print(y)
#     print(z)
#
# # d={'x':1,'y':2,'z':3}
#
# # foo(d['x'],d['y'],d['z'])
# # foo(**d) #foo(z=3,y=2,x=1)
#
# d={'x':1,'y':2,}
# foo(**d) #foo(x=1,y=2)





# def foo(*args,**kwargs): # x=(1,2,3,4,5)
#     print(args)
#     print(kwargs)
#
# foo(1,2,3,4,5,a=1,b=2,c=3,d=4)



def index(name,gender):
    print('welecom %s gender is %s' %(name,gender))




def wrapper(*args,**kwargs): # args=('alex','male')  kwargs={}
    index(*args,**kwargs) #index(*('alex','male'),**{}) #index('alex','male')

# wrapper('alex','male')
# wrapper(gender='male',name='alex')
wrapper('alex',gender='male',)




