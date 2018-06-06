# import time
#
# current_user={'login':False}
#
# def outter(func):
#     def wrapper(*args,**kwargs):
#         if current_user['login']:
#             return func(*args,**kwargs)
#
#         user=input('username>>>: ').strip()
#         pwd=input('password>>>: ').strip()
#         if user == 'egon' and pwd == '123':
#             current_user['login']=True
#             return func(*args,**kwargs)
#     return wrapper
#
# @outter
# def index():
#     time.sleep(1)
#     print('welcome to index')
#     return 1234
#
# @outter
# def home(name):
#     time.sleep(2)
#     print('welcome %s to home page' %name)
#
#
# index()
# home('egon')
#
#



# 有参装饰器：
import time

current_user={'login':False}

def auth(engine):
    def outter(func):
        def wrapper(*args,**kwargs):
            if current_user['login']:
                return func(*args,**kwargs)

            user=input('username>>>: ').strip()
            pwd=input('password>>>: ').strip()

            if engine == 'file':
                if user == 'egon' and pwd == '123':
                    current_user['login']=True
                    return func(*args,**kwargs)

            elif engine == 'mysql':
                print('基于mysql数据的认证')
            elif engine == 'ldap':
                print('基于ldap的认证方式')
        return wrapper
    return outter

@auth(engine='mysql') # @outter # index=outter(index) #index=wrapper
def index():
    time.sleep(1)
    print('welcome to index')
    return 1234

@auth(engine='ldap') # @outter # home=outter(home) #home=wrapper
def home(name):
    time.sleep(2)
    print('welcome %s to home page' %name)


index()
home('egon')


