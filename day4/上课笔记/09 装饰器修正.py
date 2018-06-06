# import time
#
#
# def index():
#     time.sleep(1)
#     print('welcome to index')
#     return 1234
#
# def outter(func):
#
#     def wrapper():
#         start_time=time.time()
#         res=func()
#         stop_time=time.time()
#         print('run time is %s' %(stop_time - start_time))
#         return res
#
#     return wrapper
#
#
# index=outter(index) #index=wrapper
#
#
# res=index() #res=wrapper()
# print('返回值 ',res)







import time


# def index():
#     time.sleep(1)
#     print('welcome to index')
#     return 1234
#
# def home(name):
#     time.sleep(2)
#     print('welcome %s to home page' %name)
#
#
# def outter(func):
#
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print('run time is %s' %(stop_time - start_time))
#         return res
#
#     return wrapper
#
# #
# # home=outter(home) #home=wrapper
# #
# # home('egon')  #wrapper('egon')
#
# index=outter(index)
#
# index()





# 装饰语法糖:
# 在被装饰对象正上方单独一行写@装饰器的名字
def timmer(func):

    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('run time is %s' %(stop_time - start_time))
        return res

    return wrapper

@timmer # index=timmer(index)
def index():
    time.sleep(1)
    print('welcome to index')
    return 1234

@timmer #home=timmer(home)
def home(name):
    time.sleep(2)
    print('welcome %s to home page' %name)




index()

home('egon')