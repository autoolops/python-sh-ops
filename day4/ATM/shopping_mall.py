#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/3 15:32
# FileName: shopping_mall.py



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
                with open('/Users/55haitao/Documents/python-sh-ops/day4/ATM/db/product_list', "r+") as f_shopping_car:
                    list = json.loads(f_shopping_car.read())
                    list.extend(shopping_list)
                    f_shopping_car.seek(0)
                    f_shopping_car.truncate(0)
                    list = json.dumps(list)
                    f_shopping_car.write(list)
                break
            else:
                 print("\33[31;0m错误：没有相应的编号 请重新输入:\33[0m\n")
