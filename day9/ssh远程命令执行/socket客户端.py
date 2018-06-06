#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/6/2 14:22
# FileName: socket客户端.py


from socket import  *


phone= socket(AF_INET,SOCK_STREAM)  #流式协议指的式 TCP协议

phone.connect(('127.0.0.1',8080))

while True:
    cmd = input('>>:').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))

    res = phone.recv(1024)
    print(res.decode('gbk'))
    phone.close()




