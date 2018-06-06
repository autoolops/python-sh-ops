#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : YongFu  Wang
# @Time    : 2018/4/14 18:01
# @FileName: 7.copy.py


import sys,os

src_file_path =sys.argv[1]
if not os.path.isfile(src_file_path):
    print('文件不存在')
    sys.exit()
dst_file_path =sys.argv[2]


with open(r'%s' %src_file_path,mode='rb') as read_f,\
        open(r'%s' %dst_file_path ,mode='wb') as  write_f:


