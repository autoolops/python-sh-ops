





#1.用途 ： 关系运算
#1.1关系运算
#1.2  去重

#2.定义： {}内用逗号分割开多个元素
#2.1 每一个元素必须是不可变类型
#2.2 集合内的元素不可重复
#2.3 集合无序

#可变类型 ===   不可hash   可变类型  ===可hash
#定义空集合 s = set()

#优先掌握的操作：
#1、长度len
#2、成员运算in和not in

#3、|合集
#4、&交集
#5、-差集
#6、^对称差集
#7、==
#8、父集：>,>=
#9、子集：<,<=


# 　有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
# pythons = {'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
# linuxs = {'wupeiqi','oldboy','gangdan'}
# # 　　1. 求出即报名python又报名linux课程的学员名字集合
# print(pythons & linuxs)
# print(pythons.intersection(linuxs))
# # 　　2. 求出所有报名的学生名字集合
# print(pythons|linuxs)
# print(pythons.union(linuxs))
# # 　　3. 求出只报名python课程的学员名字
# print(pythons - linuxs)
# print(pythons.difference(linuxs))
# # 　　4. 求出没有同时这两门课程的学员名字集合
# print(pythons ^ linuxs)
# print(pythons.symmetric_difference(linuxs))







#需要掌握的操作

# s1 = {'a','b','c'}
#增加
# s1.add('d')
# print(s1)

#删除
# s1 = {'a','b','c'}
# res = s1.remove('b')  #只是单纯删除，没有返回值
# print(s1)
# print(res)
# s1.remove('ddd')   #元素不存则报错

# s1 = {'a','b','c'}
# res = s1.discard('b')   #只是单纯删除，没有返回值
# print(res)
# print(s1)
# s1.discard('ddd')   # 元素不存在也不报错

# s1 = {'a','b','c'}
# res = s1.pop()  #随机删除，有返回值
# print(res)
# print(s1)


#更新

# s1 = {1,2,3}
# s1.update({4,5,6})
# print(s1)




#集合去重

# s1 = {1,2,3,4,5,2,3,4}
# print(set(s1))
# print(list(set(s1)))


#用集合去重，局限性很强
#1.不能保证原数据类型的顺序
#2. 原数据类型中包含的元素必须全部为不可变类型

l=[
    {'name':'egon','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'egon','age':20,'sex':'female'},
    {'name':'egon','age':18,'sex':'male'},
    {'name':'egon','age':18,'sex':'male'},
]
s = set() #定义一个空字典
s1 = []

for d in l:
    valuse = (d['name'],d['age'],d['sex'])
    # print(valuse)
    if valuse not in s:
        s.add(valuse)
        s1.append(d)
print(s1)

# s=set()
# l1=[]
# for item in l:
#     val=(item['name'],item['age'],item['sex'])
#     if val not in s:
#         s.add(val)
#         l1.append(item)
#
# print(l1)

##方法二

# s=[]  #定义一个字典
#
# for d in l:
#     if d not in s:
#         s.append(d)
# print(s)