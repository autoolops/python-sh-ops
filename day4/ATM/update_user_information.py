#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/4 19:20
# FileName: update_user_information.py


'''修改个人资料'''
def Updata_address(current_user):
    while True:
        print("\33[32;0m修改个人资料\33[0m".center(40, "-"))
        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/user_dict', "r+") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            address = users_dict[current_user]["address"]
            print("当前账号：\t%s\n当前收货地址：\t%s\n" % (current_user,address))
            if_updata = input("\33[34;0m是否要修改 % s登录密码 确定【y】/返回【b】\33[0m:" % (current_user))
            if if_updata == "y":
                new_address = input("\33[34;0m输入新的收货地址\33[0m:")
                users_dict[current_user]["address"]=new_address
                dict = json.dumps(users_dict)
                f_users_dict.seek(0)
                f_users_dict.truncate(0)
                f_users_dict.write(dict)
                print("\33[31;1m收货地址修改成功\33[0m\n")
            if if_updata == "b":
                break