#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/4 19:17
# FileName: update_passwd.py


'''修改登录密码'''
def Updata_password(current_user):
    while True:
        print("\33[32;0m修改登录密码\33[0m".center(40, "-"))
        print("当前账号：\t%s\n当前密码：\t**\n"%(current_user))
        if_updata = input("\33[34;0m是否要修改 % s登录密码 确定【y】/返回【b】\33[0m:"%(current_user))
        if if_updata == "y":
            with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/user_dict', "r+") as f_users_dict:
                users_dict = json.loads(f_users_dict.read())
                password = users_dict[current_user]["password"]
                old_pwd = input("\33[34;0m输入原来的密码\33[0m:")
                if old_pwd == password:
                    new_pwd = input("\33[34;0m输入新的密码\33[0m:")
                    agin_pwd = input("\33[34;0m再输入新的密码\33[0m:")
                    if new_pwd == agin_pwd:
                        users_dict[current_user]["password"]=new_pwd
                        dict = json.dumps(users_dict)
                        f_users_dict.seek(0)
                        f_users_dict.truncate(0)
                        f_users_dict.write(dict)
                        print("\33[31;1m密码修改成功\33[0m\n")
                    else:
                        print("\33[31;0m两次密码不一致\33[0m\n")
                else:
                    print("\33[31;0m密码不正确\33[0m\n")
        if if_updata == "b":
            break
