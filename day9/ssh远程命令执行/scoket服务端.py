#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : YongFu  Wang
# Time    : 2018/6/2 14:23
# FileName: scoket服务端.py
import subprocess
from  socket import  *


phone= socket(AF_INET,SOCK_STREAM)
phone.bind(('127.0.0.1',8080))
phone.listen(5)
conn, client_addr = phone.accept()
print(client_addr)

while True:
    while True:
        try:
            cmd = conn.recv(1024)
            if not cmd:break
            obj=subprocess.Popen(cmd.decode('utf-8'),shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                             )
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
            break
    conn.close()
    phone.close()



