# 函数对象：函数可以当中变量去处理

# 函数可以
# 1、可以被赋值
# def foo():
#     print('from foo')

# f=foo
# # print(f)
# f()

# 2、可以当做参数传给一个函数
# def foo():
#     print('from foo')
#
# def bar(func): #func=foo
#     # print(func)
#     func()
#
# bar(foo)

# 3、可以当做函数的返回值
# def foo():
#     print('from foo')
#
# def bar(func): #func=foo
#     return func #return foo
#
# f=bar(foo)
#
# print(f)


# 4、可以当做容器类型元素
# def foo():
#     print('from foo')
#
# l=[foo,]
# print(l)
# l[0]()
# d={'foo':foo}
#
# d['foo']()

def get():
    print('from get')

def put():
    print('from put')

def ls():
    print('from ls')

def login():
    print('from login')

def cd():
    print('from cd')

func_dic={
    "1":[get,'下载'],
    "2":[put,'上传'],
    "3":[ls,'浏览'],
    "4":[login,'登录'],
    "5":[cd,'切换目录']

}


def run():
    while True:
        for k in func_dic:
            print(k,func_dic[k][1])

        choice=input('>>>: ').strip()
        if choice == 'q':break
        if choice in func_dic:
            func_dic[choice][0]()

run()







