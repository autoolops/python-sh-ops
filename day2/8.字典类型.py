#作用：存多个值,key-value存取，取值速度快

#定义：key必须是不可变类型，value可以是任意类型
info={'name':'egon','age':18,'sex':'male'} #本质info=dict({....})
或
info=dict(name='egon',age=18,sex='male')
或
info=dict([['name','egon'],('age',18)])
或
{}.fromkeys(('name','age','sex'),None)

#优先掌握的操作：
#1、按key存取值：可存可取
#2、长度len
#3、成员运算in和not in

#4、删除
#5、键keys()，值values()，键值对items()
#6、循环