#!/usr/bin/env python
# Author:YongFu Wang
# Date: 2018/4/5
# -*- coding: utf-8 -*-


user = "wangyongfu"
passwd = "55HaiTao"
count = 0

# dict = {
#            'zhangsan':{password:'123456','count':0},
#            'lisi':{password:'123456','count':0},
#            'wyf':{password:'123456','count':0},
#         }

while count<3:
    username = input("username:")
    password = input("password:")

    if user == username  and passwd == password :
        print(">>欢迎 %s 登录认证成功" %user)
        break

    else:
        print(">>用户名不存在或密码输入错误，请重新输入相关信息！")
    count +=1

    if count == 3:
        print(">>用户或密码输入错误三次，账号已经被锁定")
        with open('lock.txt','a') as f:
            f.write('%s\n' %user)


    with open('lock.txt','r') as f:
        lock_users = f.read().split('\n')
        if user in lock_users:
            print('用户%s已经被锁定' %user)
            break









