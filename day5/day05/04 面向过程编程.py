'''
1、面向过程编程
    核心是过程二字，过程指的是解决问题的步骤，即先干什么、再干什么、后干什么。。。。
    基于面向过程的思想编写程序就好比在设计一条流水线,是一种机械式思维方式


    优点：
        将复杂的问题流程化、进而简单化
    缺点：
        修改某一个阶段，其他相关的阶段都有可能受影响，牵一发而动全身，扩展性极差

    应用：
        应用于对扩展性要求不高的场景


'''

def interactive():
    """接收用户输入的用户名、密码"""
    uname=input('username>>>: ').strip()
    group=input('group>>>: ').strip()
    pwd=input('password>>>: ').strip()
    return uname,group,pwd

def auth(uname,group,pwd):
    """认证用户名与密码是否正确"""
    if uname == 'egon' and pwd == '123' and group == 'group1':
        return True,uname,group
    else:
        return False,uname,group


def index(res):
    """如果认证成功，则打印欢迎界面"""
    if res[0]:
        print('部门：%s 员工：%s 登陆成功' %(res[2],res[1]))

    else:
        print('部门：%s 员工：%s 登陆失败' % (res[2], res[1]))


uname,group,pwd=interactive()
res=auth(uname,group,pwd)
index(res)