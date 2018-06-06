#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : YongFu  Wang
# @Time    : 2018/4/23 23:09
# @FileName: shopping_cart.py


def loggin():
    user_list = {
        'u01':{'password':'123'},
        'u02':{'password':'123'},
        'u03':{'password':'123'},
        'u04':{'password':'123'},
        'u05':{'password':'123'},
    }
    count = 0
    while True:
        if count == 3:
            print("用户名输入次数达到三次限制")
            break
        user_name = input("请输入你的用户名>>:").strip()
        if user_name not in user_list:
            print("你输入的用户不存在，请输入正确的用户名!")
            count +=1
        with open('/Users/55haitao/Documents/python-sh-ops/day4/周末班-王永福-ATM+购物车/blacklist.txt','r') as f:
            lock_file = f.readlines()
        if user_list in lock_file:

            print("用户名已锁定，请联系管理员!")
            exit()
        if user_name in user_list:
            user_password = input("请输入你的密码>>:").strip()
            if user_password == user_list[user_name]['password']:
                print("%s 欢迎登陆ATM + 购物车管理系统" %user_name)
                # break
            else:
                print("密码错误")
                count += 1
            if count ==3:
                print("你输入的密码错误次数已达到3次，将锁定你的用户!")
                with open('/Users/55haitao/Documents/python-sh-ops/day4/周末班-王永福-ATM+购物车/blacklist.txt','a') as f:
                    f.write('%s' %user_name)
                    break


loggin()
