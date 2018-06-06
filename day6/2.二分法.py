#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/12 11:30
# FileName: 2.二分法.py



l =  [12,23,43,55,67,70,88,99,101,111,121,131,141,444]

def search(num,l):
    print(l)
    if len(l) == 0:
        print('not exts')
        return
    mid_index = len(l)  // 2
    if  num  > l[mid_index]:
        search(num,l[mid_index+1:])

    elif  num < l[mid_index]:
        search(num,l[:mid_index])

    else:
        print('fint it')

search(444,l)
