#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/5/19 15:31
# FileName: 8.suprocess模块.py

import subprocess

obj=subprocess.Popen('ifconfig',
                 shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE
                 )

stdout=obj.stdout.read()
print(stdout.decode('gbk'))

stderr=obj.stderr.read()
print(stderr.decode('gbk'))