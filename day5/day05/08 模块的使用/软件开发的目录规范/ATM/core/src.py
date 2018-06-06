from conf import settings
from lib import common

def register():
    print('注册。。。')
    uname=input('请输入用户名: ').strip()
    pwd=input('请输入密码: ').strip()
    with open(settings.DB_PATH,'a',encoding='utf-8') as f:
        f.write('%s:%s\n' %(uname,pwd))

    common.logger(uname)
    print('注册成功')

def pay():
    print('支付功能。。。')

def transfer():
    print('转账。。。。')

def withdraw():
    print('体现。。。')

func_dic={
    '1':register,
    '2':pay,
    '3':transfer,
    '4':withdraw
}

def run():
    while True:
        print("""
        1 注册
        2 支付
        3 转账
        4 提现
        """)

        choice=input('>>>: ').strip()
        if choice in func_dic:
            func_dic[choice]()
        else:
            print('输入错错误指令')
