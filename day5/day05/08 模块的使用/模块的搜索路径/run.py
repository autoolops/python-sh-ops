#查找模块的顺序
#内存---->内置---->sys.path
# import time
#
# import spam #找到spam
# time.sleep(30)
# import spam
# print(spam.money)



# import time
# time.sleep(3)

# import sys
# print(sys.path)
# sys.path.append(r'D:\code\SH_weekend_s1\day05\08 模块的使用\模块的搜索路径\dir1')
# import spam
# print(spam.money)

# from dir1.dir2 import spam
# print(spam.money)

# sys.path.append(r'D:\code\SH_weekend_s1\day05\08 模块的使用\模块的搜索路径\dir1\dir2')
# import spam
# print(spam.money)


# ！！！！！！！！！！！！！sys.path的值是以当前执行文件为准！！！！！！！！！！！！！
# import sys
# print(sys.path) #D:\\code\\SH_weekend_s1\\day05\\08 模块的使用\\模块的搜索路径
from dir1 import m1
m1.f1()