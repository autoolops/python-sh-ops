'''
01 语法：
    def 函数名(参数1,参数2，...):
        """
        文档注释
        """
        代码1
        代码2
        代码3
        ....

        return 返回值

02 定义函数时：只检测语法，不执行代码

03 定义函数的三种形式
'''

# 定义函数的形式一：无参函数
# def foo():
#     print('from fooo')
#
# foo()

def print_msg():
    print('************************************')
    print('==========welcome to ATM============')
    print('************************************')

def pay():
    print('from pay')

def check():
    print('from check')

def transfer():
    print('from transfer')


def run():
    print("""
    1 支付
    2 查询
    3 转账
    """)
    choice=input('>>: ').strip()
    if choice == '1':
        pay()
    elif choice == '2':
        check()
    elif choice == '3':
        transfer()

# run()



#定义函数的形式二：有参函数
# def bar(x,y):
#     print(x,y)
#
# bar(1,2)

# def max2(x,y):
#     # x=30
#     # y=20
#
#     if x > y:
#         print(x)
#     else:
#         print(y)
#
# max2(20,30)
# max2(2,3)
#
#


#定义函数的形式三：空函数
# def foo(x,y):
#     pass


def get():
    pass

def put():
    pass

def auth():
    pass

def ls():
    pass

def cd():
    pass
