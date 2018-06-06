
def dog(name):
    print('狗哥%s准备开吃' %name)
    food_list=[]
    while True:
        food=yield food_list#暂停 food=yield='骨头'
        print('狗哥%s 吃了%s' %(name,food))
        food_list.append(food)



g=dog('alex')
# print(g)
# res1=next(g) # 让狗准备好，即让生成器对象先暂停到一个位置，准备接收
# print(res1)

g.send(None) #完全等同于next(g),强调：对于表达式形式yield的生成器，在使用前必须先用next(g)或g.send(None)初始化一次


# res2=g.send('骨头')
# print(res2)
# #
# res3=g.send('骨头1')
# print(res3)
#
# res4=g.send('骨头2')
# print(res4)
#
# res4=next(g)
# print(res4)



#
# def dog(food):
#     print('狗哥%s 吃了%s' %(food))
#
#
# dog('alex1')
# dog('alex2')
# dog('alex3')