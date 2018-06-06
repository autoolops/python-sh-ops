#!/usr/bin/env python
# Author:YongFu Wang
# Date: 2018/4/6
# -*- coding: utf-8 -*-

'''
1.什么是循环
    循环即重复的过程
2.为什么要有循环

3.while 循环的语法

'''

#4. while  + break  结束本次循环

# username = 'wyf'
# password = '123456'
# while True:
#     name = input('username:')
#     pwd = input('password:')
#     if name == username and pwd == password:
#         print('登录成功')
#         break
#     else:
#         print('用户名或密码错误')

#打印1-10

# n=1
# while True:
#     if n <= 10:
#         print(n)
#         n+=1
#     else:
#         break

#打印1-10  改进1
# n=1
# while True:
#     if n > 10:break
#     print(n)
#     n+=1

#打印1-10  改进2
# n =1
# while n<=10:
#     print(n)
#     n+=1

#5. while + continue  结束本次循环,进入下一次循环

# n=1
# while n<=7:
#     if n == 3:
#         n+= 1
#         continue
#     print(n)
#     n+=1


######例题
# username = 'wyf'
# password = '123456'
# count = 1
#
# while True:
#     if count == 3:
#         print('密码输入次数过多')
#         break
#     name = input('username:')
#     pwd = input('password:')
#
#     if name == username and pwd == password:
#         print('登录成功')
#         while True:
#             cmd = input('请输入你的命令:')
#             if cmd == 'q':
#                 break
#             print('%s is running' %cmd)
#         break
#     else:
#         print('用户名或密码错误')
#         count +=1

#6. while +tag


username = 'wyf'
password = '123456'
count = 1

tag = True
while tag:
    if count == 3:
        print('密码输入次数过多')
        break
    name = input('username:')
    pwd = input('password:')

    if name == username and pwd == password:
        print('登录成功')
        while tag:
            cmd = input('请输入你的命令:')
            if len(cmd) == 0:continue    ## <===>  if not cmd:continue
            if cmd == 'q':
                tag = False
                break
            print('%s is running' %cmd)
        # break
    else:
        print('用户名或密码错误')
        count +=1

























