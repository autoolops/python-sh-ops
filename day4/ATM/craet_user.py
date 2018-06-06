#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/4 12:04
# FileName: craet_user.

'''创建用户'''
def User_create(address="None",locked=0,creditcard=0):
    while True:
        print("开始创建用户".center(50,"-"))
        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/user_dict', "r+") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            for key in users_dict:
                print("系统已有用户 【%s】" % (key))
            if_create = input("\n\33[34;0m是否创建新的用户 确定【y】/返回【b】\33[0m:")
            if if_create == "y":
                username = input("\33[34;0m输入要添加账户的用户名：\33[0m")
                password = input("\33[34;0m输入添加账户的密码：\33[0m")
                if username not in users_dict.keys():
                    if len(username.strip()) > 0:
                       if len(password.strip()) > 0:
                           users_dict[username] = {"username":username,"password":password,"creditcard":creditcard,"address":address,
                                                      "locked":locked}
                           dict = json.dumps(users_dict)
                           f_users_dict.seek(0)
                           f_users_dict.truncate(0)
                           f_users_dict.write(dict)
                           print("\33[31;1m创建用户 %s 成功\33[0m\n"%(username))
                       else:
                           print("\33[31;0m输入的密码为空\33[0m\n")
                    else:
                        print("\33[31;0m输入的用户名为空\33[0m\n")
                else:
                    print("\33[31;0m用户名 %s 已经存在\33[0m\n"%(username))
            if if_create == "b":
                break

'''锁定用户'''
def Lock_user():
    while True:
        print("\33[32;0m锁定用户\33[0m".center(50, "-"))
        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/user_dict', "r+") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            for key in users_dict:
                if users_dict[key]["locked"] == 0:
                    print("系统用户 【%s】\t\t锁定状态：【未锁定】"%(key))
                else:
                    print("系统用户 【%s】\t\t锁定状态：\33[7m【已锁定】\33[0m" % (key))
            if_lock = input("\n\33[34;0m是否进行用户锁定 确定【y】/返回【b】\33[0m:")
            if if_lock == "y":
                lock_user = input("\33[34;0m输入要锁定的用户名\33[0m:")
                if lock_user in users_dict.keys():
                    if users_dict[lock_user]["locked"] == 0:
                        users_dict[lock_user]["locked"] = 1
                        dict = json.dumps(users_dict)
                        f_users_dict.seek(0)
                        f_users_dict.truncate(0)
                        f_users_dict.write(dict)
                        print("\33[31;1m用户 %s 锁定成功\33[0m\n" % (lock_user))
                    else:
                        print("\33[31;0m用户 %s 锁定失败 之前已经被锁定\33[0m\n" % (lock_user))
                else:
                    print("\33[31;0m用户 %s 不存在\33[0m\n"%(lock_user))
            if if_lock == "b":
                break

'''解锁用户'''
def Unlock_user():
    while True:
        print("\33[32;0m解锁用户\33[0m".center(50, "-"))
        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/user_dict', "r+") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            for key in users_dict:
                if users_dict[key]["locked"] == 0:
                    print("系统用户 【%s】\t\t锁定状态：【未锁定】" % (key))
                else:
                    print("系统用户 【%s】\t\t锁定状态：\33[7m【已锁定】\33[0m" % (key))
            if_lock = input("\n\33[34;0m是否进行用户解锁 确定【y】/返回【b】\33[0m:")
            if if_lock == "y":
                unlock_user = input("\33[34;0m输入要解锁的用户名\33[0m:")
                if unlock_user in users_dict.keys():
                    if users_dict[unlock_user]["locked"] == 1:
                        users_dict[unlock_user]["locked"] = 0
                        dict = json.dumps(users_dict)
                        f_users_dict.seek(0)
                        f_users_dict.truncate(0)
                        f_users_dict.write(dict)
                        print("\33[31;1m用户 %s 解锁成功\33[0m\n" % (unlock_user))
                    else:
                        print("\33[31;0m用户 %s 解锁失败 用户未被锁定\33[0m\n" % (unlock_user))
                else:
                    print("\33[31;0m用户 %s 不存在\33[0m\n"%(unlock_user))
            if if_lock == "b":
                break