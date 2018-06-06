#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/6/2 14:22
# FileName: socket客户端.py

import  socket


# phone= socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #流式协议指的式 TCP协议
#
# phone.connect(('127.0.0.1',9080))
#
# phone.send('hello word'.encode('utf-8'))
#
# data = phone.recv(1024)
# print(data)
#
# phone.close()

##############循环版######

phone= socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #流式协议指的式 TCP协议

phone.connect(('127.0.0.1',8080))
while True:
    msg = input('>>').strip()
    phone.send(msg.encode('utf-8'))

    data = phone.recv(1024)
    print(data.decode('utf-8'))

phone.close()