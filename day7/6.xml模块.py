#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/19 14:35
# FileName: 6.xml模块.py
import  xml.etree.ElementTree as ET


tree = ET.parse("/Users/55haitao/Documents/python-sh-ops/day7/a")
root = tree.getroot()

print(root.tag)


#遍历xml文档

for country  in root:
    print('=======>',country.tag,country.attrib)
    for item  in country:
        print(item.tag,item.attrib,item.text)