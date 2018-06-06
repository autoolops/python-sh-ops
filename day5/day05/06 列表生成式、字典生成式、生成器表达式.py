#列表生成式
# l=[]
# for i in range(10):
#     l.append('egg%s' %i)

# print(l)


# l=['egg%s' %i for i in range(10)]
# print(l)
#
# nums=[i**2 for i in range(10)]
# print(nums)


# nums=[i for i in range(10) if i > 3]
# print(nums)

# 1、将names=['egon','alex_sb','wupeiqi','yuanhao']中的名字全部变大写
# names=['egon','alex_sb','wupeiqi','yuanhao']
# names=[name.upper() for name in names]
# print(names)


# 2、将names=['egon','alex_sb','wupeiqi','yuanhao']中以sb结尾的名字过滤掉，然后保存剩下的名字长度
# names=['egon','alex_sb','wupeiqi','yuanhao']
# l=[len(name) for name in names if not name.endswith('sb')]
# print(l)




#字典生成式
# d={i:i for i in range(10) if i > 0}
# print(d)
# userinfo=[('egon','123'),('alex','456'),('wxx','679')]
# dic={k:v for k,v in userinfo}
# print(dic)



#生成器表达式
# g=(i for i in range(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
# # print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# chicken=('egg%s' %i for i in range(3))
# # print(chicken)
# print(next(chicken))
# print(next(chicken))
# print(next(chicken))
# print(next(chicken))


#求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
# res=max((1,2,3,4,5,6,7))
# print(res)

with open('a.txt','r',encoding='utf-8') as f:
    nums=(len(line) for line in f)
    # print(nums)
# print(nums)
# print(next(nums))

print(max(nums))




