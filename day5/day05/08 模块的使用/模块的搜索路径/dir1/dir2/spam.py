#spam.py
# print('from the spam.py')
__all__=['money','read1'] # from spam import *，控制的就是*所导入的名字
money=1000

def read1():
    print('spam模块：',money)

def read2():
    print('spam模块')
    read1()

def change():
    global money
    money=0


# 当文件被当做脚本执行时__name__的值为"__main__"
# 当文件被导入时__name__的值为"模块名"
# print(__name__)

if __name__ == '__main__': # 改行代码用于区分python文件的两种不同用途，应该写在文件末尾
    read1()
    read2()
    change()