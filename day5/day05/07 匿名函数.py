# def f1():
#     print('from f1')
#
# f1()
# f1()


def func(x,y):
    return x+y

# print(func)
# func(1,2)

# 匿名
#注意：
#1、不会单独使用，会与其他函数配合使用
#2、匿名函数的精髓在于没有名字，如果没有名字意味用一次就立即回收，所以
# 匿名函数的应用场景仅应用于只使用一次的场景
# lambda x,y:x+y


#配合使用的内置函数：max，min，sorted，filter，map，

salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}
# 求出最大工资的那个人名

# def func(k):
#     return salaries[k]

# print(max(salaries,key=lambda x:salaries[x])) # 比的是value，但得的结果是key
# print(min(salaries,key=lambda x:salaries[x])) # 比的是value，但得的结果是key

# sorted，按照薪资排序，从小到大排
# print(sorted(salaries,key=lambda x:salaries[x]))
# print(sorted(salaries,key=lambda x:salaries[x],reverse=True))


# map的应用
# names=['alex','wupeiqi','yuanhao','liuqingzheng']
# l=[name+"_SB" for name in names]
# print(l)
#
# obj=map(lambda x:x+"_SB",names) #迭代器
# print(list(obj))

#filter的应用
names=['alex_sb','wupeiqi_sb','egon','yuanhao_sb','liuqingzheng_sb']

# l=(name for name in names if name.endswith('sb'))
# print(l)

#filter会得到names的迭代器对象obj，然后next（obj）将得到的值传给filter第一个参数指定的函数
# 将函数返回值为True的那个值留下
res=filter(lambda x:x.endswith('sb'),names)
print(list(res))
