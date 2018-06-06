#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/4 19:25
# FileName: Link_creditcard.py

'''修改信用卡绑定'''
def Link_creditcard(current_user):
    while True:
        print("\33[32;0m修改信用卡绑定\33[0m".center(40, "-"))
        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/user_dict', "r+") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            creditcard = users_dict[current_user]["creditcard"]
            if creditcard == 0 :
                print("当前账号： \t%s"%(current_user))
                print("信用卡绑定：\33[31;0m未绑定\33[0m\n")
            else:
                print("当前账号： \t%s" %(current_user))
                print("绑定的信用卡： %s\n"%(creditcard))
            if_updata = input("\33[34;0m是否要修改信用卡绑定 确定【y】/返回【b】\33[0m:")
            if if_updata == "y":
                creditcard_new = input("\33[34;0m输入新的信用卡卡号(6位数字)\33[0m:")
                if creditcard_new.isdigit() and len(creditcard_new) ==6:
                    with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/creditcard_dict', "r+") as f_creditcard_dict:
                        creditcard_dict = json.loads(f_creditcard_dict.read())
                        if creditcard_new in creditcard_dict.keys():
                            users_dict[current_user]["creditcard"]=creditcard_new
                            dict = json.dumps(users_dict)
                            f_users_dict.seek(0)
                            f_users_dict.truncate(0)
                            f_users_dict.write(dict)
                            print("\33[31;1m信用卡绑定成功\33[0m\n")
                        else:
                            print("\33[31;0m输入信用卡卡号不存在(未发行)\33[0m\n")
                else:
                    print("\33[31;0m输入信用卡格式错误\33[0m\n")
            if if_updata == "b":
                break