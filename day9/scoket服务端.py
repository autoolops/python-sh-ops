#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/6/2 14:23
# FileName: scoket服务端.py

import  socket
#
# phone= socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #流式协议指的式 TCP协议
#
# phone.bind(('127.0.0.1',9080))
#
# phone.listen(5)   #
#
# conn,client_addr=phone.accept()
#
# data = conn.recv(1024)
#
# print('客户端数据:%s' %data)
#
# conn.send(data.upper())
#
# conn.close()
# phone.close()



##################加上通信循环###
# phone= socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #流式协议指的式 TCP协议
# phone.bind(('127.0.0.1',8080))
# phone.listen(5)   #
# conn, client_addr = phone.accept()
# print(client_addr)
# while True:
#     try:
#         data = conn.recv(1024)
#         if not data:break
#         print('客户端数据:%s' %data)
#         conn.send(data.upper())
#     except ConnectionResetError:
#         break
# conn.close()
#
# phone.close()


###################加上链接循环#####
phone= socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #流式协议指的式 TCP协议
phone.bind(('127.0.0.1',8080))
phone.listen(5)   #
print('服务端启动.....')
while True:
    conn, client_addr = phone.accept()
    print(client_addr)
    while True:
        try:
            data = conn.recv(1024)
            if not data:break
            print('客户端数据:%s' %data)
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()

phone.close()