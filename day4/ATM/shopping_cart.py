#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/4/26 15:34
# FileName: shopping_cart.py
import  os,sys

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