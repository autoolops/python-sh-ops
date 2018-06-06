'''
1 开放封闭原则
    软件一旦上之后就应该开放封闭原则
    具体是指对修改是封闭的，但对扩展是开放的

2、什么是装饰器
    装饰就是修饰，器指的就是工具
    装饰器本身可以是任意可调用的对象
    被装饰的对象也可以是任意可调用的对象

    装饰器——》函数
    被装饰的对象=》函数

    装饰器是用来为被装饰对象添加新功能的一种工具
    必须遵循：
        1、不能修改被装饰对象的源代码
        2、不能修改被装饰对象的调用方式


'''
import time


def index():
    time.sleep(1)
    print('welcome to index')

def outter(func):

    def wrapper():
        start_time=time.time()
        func()
        stop_time=time.time()
        print('run time is %s' %(stop_time - start_time))

    return wrapper


index=outter(index) #index=wrapper

index()





