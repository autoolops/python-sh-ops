#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/4/26 15:34
# FileName: main.py

import  os,sys,json,time,datetime

'''装饰器'''

def  auth(auth_type):
    def  outer_wrapper(func):
        def wrapper(*args,**kwargs):

            if auth_type == "user_auth":
                username = input("\33[34;0m请输入用户名：\33[0m")
                if len(username.strip())>0:
                    with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/user_dict','r+') as  f_user_dict:
                        users_dict = json.loads(f_user_dict.read())
                        if username in users_dict.keys():
                            password = input("\33[34;0m请输入密码：\33[0m")
                            if password == users_dict[username]["password"]:
                                if users_dict[username]["locked"] == 0:
                                    print("\33[31;0m用户 %s 认证成功\33[0m" % (username))
                                    res = func(*args, **kwargs)
                                    return res,username
                                else:
                                    print("\33[31;0m用户 %s 已经被锁定 认证失败\33[0m" % (username))
                            else:
                                print("\33[31;0m输入的密码不匹配，请重新输入\33[0m")
                        else:
                            print("\33[31;0m输入的用户名不存在，请输入正确的用户名\33[0m")
                else:
                    print("\33[31;0m输入的用户名为空,请输入正确的用户名\33[0m")

            if auth_type == "creditcard_auth":
                creditcard = input("\33[34;0m输入信用卡卡号(6位数字)：\33[0m")
                if len(creditcard.strip()) > 0:
                    with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/creditcard_dict',"r+") as f_creditcard_dict:
                        creditcard_dict = json.loads(f_creditcard_dict.read())
                        if creditcard in creditcard_dict.keys():
                            password = input("\33[34;0m输入信用卡的密码：\33[0m")
                            if password == creditcard_dict[creditcard]["password"]:
                                if creditcard_dict[creditcard]["locked"] == 0:
                                    print("\33[31;0m信用卡 %s 认证成功\33[0m" % (creditcard))
                                    res = func(*args,**kwargs)
                                    return res, creditcard
                                else:
                                    print("\33[31;0m信用卡 %s 已经被冻结 认证失败\33[0m" % (creditcard))
                            else:
                                print("\33[31;0m输入的密码不匹配 认证失败\33[0m")
                        else:
                            print("\33[31;0m输入的信用卡卡号不存在 认证失败\33[0m")
                else:
                    print("\33[31;0m输入的信用卡卡号为空 认证失败\33[0m")

            if auth_type == "admincenter_auth":
                admincenter_dict = {"admin": "admin"}
                username = input("\33[34;0m请输入管理用户名：\33[0m")
                if len(username.strip()) > 0:
                    if username in admincenter_dict.keys():
                        password = input("\33[34;0m请输入管理密码：\33[0m")
                        if password == admincenter_dict[username]:
                            print("\33[31;0m管理用户 %s 认证成功\33[0m" % (username))
                            res = func(*args,**kwargs)
                            return  res,username
                        else:
                            print("\33[31;0m输入的密码不匹配 认证失败\33[0m")
                    else:
                        print("\33[31;0m输入的用户名不存在 认证失败\33[0m")
                else:
                    print("\33[31;0m输入的用户名为空 认证失败\33[0m")


        return wrapper
    return outer_wrapper


'''用户登录认证'''
@auth(auth_type="user_auth")
def user_auth():
    print("\33[32;0m用户登录认证\33[0m".center(40,"-"))
    return "True"

'''信用卡认证'''
@auth(auth_type="creditcard_auth")
def creditcard_auth():
    print("\33[32;0m信用卡登录认证\33[0m".center(40,"-"))
    return "True"


'''后台管理认证'''
@auth(auth_type="admincenter_auth")
def admincenter_auth():
    print("\33[32;0m后台管理登录认证\33[0m".center(40,"-"))
    return "True"


'''购物商城'''
def Shopping_mall():
    shopping_list,pro_list  = [],[]
    with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/product_list', "r", encoding="utf-8") as  f_product:
        for item in f_product:
            pro_list.append(item.strip("\n").split())
    def pro_inf():
        print("编号\t商品\t\t价格")
        for index, item in enumerate(pro_list):
            print("%s\t\t%s\t\t%s" % (index, item[0], item[1]))
    while True:
            print(("\33[32;0m目前商城在售的商品信息\33[0m").center(40, "-"))
            pro_inf()
            choice_id = input("\n\33[34;0m选择要购买的商品编号 【购买 ID】/【返回 b】\33[0m：")
            if choice_id.isdigit():
                choice_id = int(choice_id)
                if choice_id < len(pro_list) and choice_id >=0:
                    pro_item = pro_list[choice_id]
                    print("\33[31;0m商品%s加入购物车 价格%s\33[0m"%(pro_item[0],pro_item[1]))
                    shopping_list.append(pro_item)

                else:
                    print("\33[31;0m错误：没有相应的编号 请重新输入:\33[0m\n")
            elif  choice_id == "b":
                with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/shopping_car', "r+") as f_shopping_car:
                    list = json.loads(f_shopping_car.read())
                    list.extend(shopping_list)
                    f_shopping_car.seek(0)
                    f_shopping_car.truncate(0)
                    list = json.dumps(list)
                    f_shopping_car.write(list)
                break
            else:
                 print("\33[31;0m错误：没有相应的编号 请重新输入:\33[0m\n")

'''购物车'''
def Shopping_car():
    while True:
        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/shopping_car', "r+") as f_shopping_car:
            list = json.loads(f_shopping_car.read())
            sum = 0
            print("\33[32;0m购物车信息清单\33[0m".center(40,"-"))
            for index,item in enumerate(list):
                print(index,item[0],item[1])
                sum +=int(item[1])
            print("\33[31;1m商品总额共计： %s\33[0m"%(sum))
        if_buy = input("\n\33[34;0m选择要进行的操作 返回【b】/清空【f】\33[0m:")
        if if_buy == "b" :
            break
        if if_buy == "f":
            Empty_shopping_car()


'''清空购物车'''
def Empty_shopping_car():
    with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/shopping_car', "w") as f_shopping_car:
        list = json.dumps([])
        f_shopping_car.write(list)

'''购物结算'''
def Pay_shopping(current_user):
    while True:
        sum = 0
        print("\33[32;0m购物结算\33[0m".center(40, "-"))
        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/shopping_car', "r+") as f_shopping_car:
            list = json.loads(f_shopping_car.read())
            for item in list:
                sum += int(item[1])
            if_pay = input("\n\n\33[34;0m当前商品总额：%s 是否进行支付 确定【y】/返回【b】\33[0m:"%(sum))
            if if_pay == "y":
                with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/user_dict', "r+") as f_users_dict:
                    users_dict = json.loads(f_users_dict.read())
                    creditcard=users_dict[current_user]["creditcard"]
                    if creditcard == 0:
                        print("\33[31;0m账号 %s未绑定信用卡，请到个人中心里修改信用卡绑定\33[0m\n"%(current_user))
                    else:
                        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/creditcard_dict', "r+") as f_creditcard_dict:
                            creditcard_dict = json.loads(f_creditcard_dict.read())
                            limit = creditcard_dict[creditcard]["limit"]
                            limit_new = limit - sum
                            if limit_new >=0:
                                res = Auth_creditcard(creditcard)
                                if res == True:
                                    creditcard_dict[creditcard]["limit"]=limit_new
                                    dict=json.dumps(creditcard_dict)
                                    f_creditcard_dict.seek(0)
                                    f_creditcard_dict.truncate(0)
                                    f_creditcard_dict.write(dict)
                                    value = "购物支付 %s"%(sum)
                                    print("\33[31;1m支付成功，当前余额 %s元\33[0m\n"%(limit_new))
                                    Shoppingcar_record(current_user,list)
                                    Creditcard_record(creditcard, value)
                                    Empty_shopping_car()
                            else:
                                print("\33[31;0m当前信用卡额度 %s元 不足矣支付购物款 可绑定其他信用卡支付\33[0m\n"%(limit))
            if if_pay == "b":
                break


'''修用户改登录密码'''
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



'''发行信用卡'''
def Creditcard_create(limit=15000,locked=0):
    while True:
        print("发行信用卡".center(50, "-"))
        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/creditcard_dict', "r+") as f_creditcard_dict:
            creditcard_dict = json.loads(f_creditcard_dict.read())
            for key in creditcard_dict:
                print("系统已有信用卡 【%s】 \t持卡人 【%s】" % (key,creditcard_dict[key]["personinfo"]))
            if_create = input("\n\33[34;0m是否发行新的信用卡 确定【y】/返回【b】\33[0m:")
            if if_create == "y":
                creditcard = input("\33[34;0m输入要发行信用卡卡号(6位数字)：\33[0m")
                if creditcard not in creditcard_dict.keys():
                    if creditcard.isdigit() and len(creditcard) == 6:
                        password = input("\33[34;0m输入要发行信用卡的密码：\33[0m")
                        if len(password.strip()) > 0:
                            personinfo = input("\33[34;0m输入要发行信用卡申请人：\33[0m")
                            if len(personinfo.strip()) > 0:
                                creditcard_dict[creditcard] = {"creditcard":creditcard, "password":password, "personinfo":personinfo,
                                                        "limit":limit,"limitcash":limit//2,"locked":locked,"deflimit":limit}
                                dict = json.dumps(creditcard_dict)
                                f_creditcard_dict.seek(0)
                                f_creditcard_dict.truncate(0)
                                f_creditcard_dict.write(dict)
                                print("\33[31;0m发行信用卡 %s 成功 额度 %s\33[0m\n"%(creditcard,limit))
                            else:
                                print("\33[31;0m信用卡申请人不能为空\33[0m\n")
                        else:
                            print("\33[31;0m输入的密码为空\33[0m\n")
                    else:
                        print("\33[31;0m信用卡 %s 卡号不符合规范\33[0m\n" % (creditcard))
                else:
                    print("\33[31;0m信用卡 %s 已经存在\33[0m\n" % (creditcard))
            if if_create == "b":
                break

'''冻结信用卡'''
def Lock_creditcard():
    while True:
        print("\33[32;0m冻结信用卡\33[0m".center(50, "-"))
        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/creditcard_dict', "r+") as f_creditcard_dict:
            creditcard_dict = json.loads(f_creditcard_dict.read())
            for key in creditcard_dict:
                if creditcard_dict[key]["locked"] == 0:
                    print("信用卡 【%s】\t\t冻结状态：【未冻结】" % (key))
                else:
                    print("信用卡 【%s】\t\t冻结状态：\33[7m【已冻结】\33[0m" % (key))
            if_Unlock = input("\n\33[34;0m是否进行信用卡冻结 确定【y】/返回【b】\33[0m:")
            if if_Unlock == "y":
                creditcard = input("\33[34;0m输入要冻结的信用卡卡号\33[0m:")
                if creditcard in creditcard_dict.keys():
                    if creditcard_dict[creditcard]["locked"] == 0:
                        creditcard_dict[creditcard]["locked"] = 1
                        dict = json.dumps(creditcard_dict)
                        f_creditcard_dict.seek(0)
                        f_creditcard_dict.truncate(0)
                        f_creditcard_dict.write(dict)
                        print("\33[31;1m信用卡 %s 冻结成功\33[0m\n" % (creditcard))
                    else:
                        print("\33[31;0m信用卡 %s 冻结失败 之前已经被冻结\33[0m\n" % (creditcard))
                else:
                    print("\33[31;0m信用卡 %s 不存在\33[0m\n" %(creditcard))
            if if_Unlock == "b":
                break

'''解冻信用卡'''
def Unlock_creditcard():
    while True:
        print("\33[32;0m解冻信用卡\33[0m".center(50, "-"))
        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/creditcard_dict', "r+") as f_creditcard_dict:
            creditcard_dict = json.loads(f_creditcard_dict.read())
            for key in creditcard_dict:
                if creditcard_dict[key]["locked"] == 0:
                    print("信用卡 【%s】\t\t冻结状态：【未冻结】" % (key))
                else:
                    print("信用卡 【%s】\t\t冻结状态：\33[7m【已冻结】\33[0m" % (key))
            if_Unlock = input("\n\33[34;0m是否进行信用卡解冻 确定【y】/返回【b】\33[0m:")
            if if_Unlock == "y":
                creditcard = input("\33[34;0m输入要解冻的信用卡卡号\33[0m:")
                if creditcard in creditcard_dict.keys():
                    if creditcard_dict[creditcard]["locked"] == 1:
                        creditcard_dict[creditcard]["locked"] = 0
                        dict = json.dumps(creditcard_dict)
                        f_creditcard_dict.seek(0)
                        f_creditcard_dict.truncate(0)
                        f_creditcard_dict.write(dict)
                        print("\33[31;1m信用卡 %s 解冻成功\33[0m\n" % (creditcard))
                    else:
                        print("\33[31;0m信用卡 %s 解冻失败 之前未被冻结\33[0m\n" % (creditcard))
                else:
                    print("\33[31;0m信用卡 %s 不存在\33[0m\n" % (creditcard))
            if if_Unlock == "b":
                break

'''修改信用卡额度'''
def Updata_limit():
    while True:
        print("\33[32;0m修改信用卡额度\33[0m".center(70, "-"))
        with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/creditcard_dict', "r+") as f_creditcard_dict:
            creditcard_dict = json.loads(f_creditcard_dict.read())
            for key in creditcard_dict:
                    limitcash = creditcard_dict[key]["limitcash"]
                    print("信用卡 【%s】\t目前可用额度：【￥%s】\t取现额度：【￥%s】" %
                          (key,creditcard_dict[key]["limit"],limitcash))
            if_Updata = input("\n\33[34;0m是否进行信用卡额度调整 确定【y】/返回【b】\33[0m:")
            if if_Updata == "y":
                creditcard = input("\33[34;0m输入要修改额度的信用卡卡号\33[0m:")
                if creditcard in creditcard_dict.keys():
                    limit = input("\33[34;0m输入额度修改后的金额(至少￥5000)\33[0m:")
                    if limit.isdigit():
                        limit_default = creditcard_dict[creditcard]["deflimit"]
                        limit = int(limit)
                        if limit >=5000:
                            updata = limit - limit_default
                            creditcard_dict[creditcard]["limit"] +=updata
                            creditcard_dict[creditcard]["limitcash"] += updata//2
                            creditcard_dict[creditcard]["deflimit"]=limit
                            dict = json.dumps(creditcard_dict)
                            f_creditcard_dict.seek(0)
                            f_creditcard_dict.truncate(0)
                            f_creditcard_dict.write(dict)
                            print("\33[31;1m信用卡 %s 额度修改成功 额度 %s \33[0m\n" % (creditcard,limit))
                        else:
                            print("\33[31;0m输入金额 ￥%s 小于￥5000\33[0m\n" % (limit))
                    else:
                        print("\33[31;0m输入金额 ￥%s 格式错误\33[0m\n" % (limit))
                else:
                    print("\33[31;0m信用卡 【%s】 不存在\33[0m\n" % (creditcard))
            if if_Updata == "b":
                break

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


while True:
    print(
        '''
        #######################################################
        #           WELCOME  TO   ATM+SHOPPPING               #
        #                                                     #
        #           1.购物中心                                 #                                  
        #           2.信用卡中心                               #  
        #           3.后台管理                                 #
        #           b.exit                                    #
        #                                                     #
        #######################################################
        '''
    )
    choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:").strip()
    if choice_id == "1":
        res = user_auth()
        if res !=  None:
            current_user = res[1]
            Empty_shopping_car()
            while True:
                print(
                    '''
                    #######################################################
                    #                WELCOME  TO   购物中心                #
                    #                                                     #
                    #           1.购物商场                                 #
                    #           2.查看购物车                               #
                    #           3.购物结算                                 #
                    #           4.个人中心                                 #
                    #           5.返回('b')                                #
                    #                                                     #
                    #######################################################
                    '''
                )
                choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:").strip()
                if choice_id == '1':
                    Shopping_mall()
                elif choice_id == '2':
                    Shopping_car()
                elif choice_id == '3':
                    Pay_shopping(current_user)
                elif choice_id == '4':
                    while True:
                        print(
                            '''
                            #######################################################
                            #                WELCOME  TO   个人中心                #
                            #                                                     #
                            #           1.购物历史记录                              #
                            #           2.修改登录密码                              #
                            #           3.修改个人信息                              #
                            #           4.修改行用卡绑定                            #
                            #           5.返回('b')                                #
                            #                                                     #
                            #######################################################
                            '''
                        )
                        choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:").strip()
                        if choice_id == '1':
                            pass
                        elif choice_id == '2':
                            Updata_password(current_user)
                        elif choice_id == '3':
                            Updata_address(current_user)
                        elif choice_id == '4':
                            Link_creditcard(current_user)
                        elif choice_id == 'b':
                            break
                        else:
                            print("\33[31;0m输入的ID无效，请重新选择\33[0m")

                elif choice_id == 'b':
                    break
                else:
                    print("\33[34;0m输入的ID有误，请重新选择\33[0m:")


    elif choice_id == "2":
        res = creditcard_auth()
        if  res != None:
            if res[0] == "True":
                current_creditcard = res[1]
                while True:
                    print(
                        '''
                        #######################################################
                        #                WELCOME  TO  信用卡中心                #
                        #                                                     #
                        #           1.我的信用卡                                #
                        #           2.提现                                     #
                        #           3.转账                                     #
                        #           4.还款                                     #
                        #           5.流水记录                                  #
                        #           b.返回                                     #
                        #                                                     #
                        #######################################################
                        '''
                    )
                    choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:").strip()
                    if choice_id == '1':
                        pass
                    elif choice_id == '2':
                        pass
                    elif choice_id == '3':
                        pass
                    elif choice_id == '4':
                        pass
                    elif choice_id == '5':
                        pass
                    elif choice_id == 'b':
                        break
                    else:
                        print("\33[34;0m输入的ID有误，请重新选择\33[0m:")

    elif choice_id == "3":
        res = admincenter_auth()
        if  res != None:
            while True:
                print(
                    '''
                    #######################################################
                    #                WELCOME  TO  后台管理                 #
                    #                                                     #
                    #           1.创建账号                                 #
                    #           2.锁定账号                                 #
                    #           3.解锁账号                                 #
                    #           4.发行信用卡                               #
                    #           5.冻节信用卡                               #
                    #           6.解冻信用卡                               #
                    #           7.提升信用卡额度                            #
                    #           b.返回                                     #
                    #                                                     #
                    #######################################################
                    '''
                )
                choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:").strip()
                if choice_id == '1':
                    User_create()
                elif choice_id == '2':
                    Lock_user()
                elif choice_id == '3':
                    Unlock_user()
                elif choice_id == '4':
                    Creditcard_create()
                elif choice_id == '5':
                    Lock_creditcard()
                elif choice_id == '6':
                    Unlock_creditcard()
                elif choice_id == '7':
                    Updata_limit()
                elif choice_id == 'b':
                    break
                else:
                    print("\33[34;0m输入的ID有误，请重新选择\33[0m:")

    elif choice_id == "b":
        break

    else:
        print("\33[34;0m输入的ID有误，请重新选择\33[0m:")



