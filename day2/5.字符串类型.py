#作用：名字，性别，国籍，地址等描述信息

#定义：在单引号\双引号\三引号内，由一串字符组成
#name='egon'

#优先掌握的操作：
#1、按索引取值(正向取+反向取) ：只能取

# msg= "wangyongfu"
# print(msg[0])
# print(msg[5])
# print(msg[-1])  #反向取值

#2、切片(顾头不顾尾，步长)
# msg = "wang yong fu"
# print(msg[0:5])
# print(msg[0:5:2])


#3、长度len
# msg = 'wangyongfu'
# print(len(msg))

#4、成员运算in和not in
# msg = "wang yong fu"
# name = input('username:').strip()
# # if name in msg:
# # if name not in msg:
# if not name in msg:
#     print('haha')
# else:
#     print('test')



#5、移除空白strip

# msg = "*****wyf****/*"
# msg1= msg.strip('* /')  ###默认去掉左右两边的字符
# print(msg1)


#6、切分split
# info = "root:*:0:0:System Administrator:/var/root:/bin/sh"
# info1=info.split(':')
# print(info1)
# print(info1[0])

#7、循环

#循环取值
#
# msg = 'wangyongfu'
# for i in msg:
#     print(i)
#



##需要掌握
#1、strip,lstrip,rstrip  #去除左右两边的特殊字符

#2、lower,upper  大小写转换

#3、startswith,endswith  ##以什么开头  以什么结尾

#4、format的三种玩法  #格式化字符串

#5、split,rsplit   #从左往右 切割
#6、join             #jion 只能连接所包含的元素都为字符串类型的列表


#7、replace  ＃ 替换字符串




#8、isdigit  #判断是否是数字













