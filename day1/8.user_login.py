#!/usr/bin/env python
# Author:YongFu Wang
# Date: 2018/4/5
# -*- coding: utf-8 -*-



dict = {
           'zhangsan':{'passwd':'123456','count':0},
           'lisi':{'passwd':'123456','count':0},
           'wyf':{'passwd':'123456','count':0},
        }

count = 0
while True:
    username = input("username:")
    if username not in dict:
        print("输入的用户%s不存在，请重新输入！" %username)
        continue

    with open('lock.txt','r') as f:
        lock_users = f.read().split('\n')
        if username in lock_users:
            print('用户%s密码输入次数过，账号已经锁定' % username)
            break
    if dict[username]['count'] > 2:
        print('密码输入次数过多，账号已经被锁定，请15分钟后在尝试登录')
        with open('lock.txt', 'a') as f:
            f.write('%s\n' % username)
            break

    password = input('password:')
    if password == dict[username]['passwd']:
        print('登录成功')
        break
    else:
        print('用户名或密码输入错误')
        dict[username]['count'] += 1












