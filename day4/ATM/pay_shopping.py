#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/4 10:08
# FileName: pay_shopping.py

'''购物结算'''
def Pay_shopping(current_user):
    while True:
        sum = 0
        print("\33[32;0m购物结算\33[0m".center(40, "-"))
        with open(__db_shoping_car, "r+") as f_shopping_car:
            list = json.loads(f_shopping_car.read())
            for item in list:
                sum += int(item[1])
            if_pay = input("\n\n\33[34;0m当前商品总额：%s 是否进行支付 确定【y】/返回【b】\33[0m:"%(sum))
            if if_pay == "y":
                with open(__db_users_dict, "r+") as f_users_dict:
                    users_dict = json.loads(f_users_dict.read())
                    creditcard=users_dict[current_user]["creditcard"]
                    if creditcard == 0:
                        print("\33[31;0m账号 %s未绑定信用卡，请到个人中心里修改信用卡绑定\33[0m\n"%(current_user))
                    else:
                        with open(__db_creditcard_dict, "r+") as f_creditcard_dict:
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