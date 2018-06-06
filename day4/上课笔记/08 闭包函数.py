'''
闭包函数就是：函数嵌套+名称空间与作用域+函数对象

1、什么是闭包函数
    1、定义在函数的内函数
    2、该函数体代码包含对该函数外层作用域中名字的引用，
        强调：函数外层指的不是全局作用域

    满足上述两个条件，那么该内部函数就称之为闭包函数
'''
# def outter():
#     x = 1
#
#     def inner():
#         print(x)
#
#     return inner #利用函数对象的概念，将一个内部函数返回并在全局中拿到并使用，从而打破了函数的层级限制
#
# f=outter() #f=inner
# # print(f)
#
# # f()
#
# def foo():
#     x=111111111111111111111111111111111111111111111111
#     print('from foo')
#     f()
#
# foo()




#为函数体传值的方式
#方式一：以参数的形式为函数体传值
import requests #pip3 install requests


# def get(url):
#     response=requests.get(url)
#     if response.status_code == 200:
#         print(response.text)
#
# get('https://www.python.org')
# get('https://www.python.org')
# get('https://www.python.org')
# get('https://www.python.org')



#方式二：包给函数

def outter(url):
    # url='https://www.baidu.com'
    def get():
        response=requests.get(url)
        if response.status_code == 200:
            print(response.text)
    return get


baidu=outter('https://www.baidu.com')
python=outter('https://www.python.org')

python()
python()

baidu()
baidu()













