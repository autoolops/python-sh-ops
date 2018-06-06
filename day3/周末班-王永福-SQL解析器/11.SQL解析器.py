#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : YongFu  Wang
# @Time    : 2018/4/16 21:41
# @FileName: 11.作业.py
import  os

'''
Hi egon  作业有点写不出来，可能需要讲解一下

'''


#第一部分，sql解析
def sql_parse(sql):    #insert  update select  delete
    '''
    把sql字符串切分，提取命令信息，分发给具体的解析函数去解析
    :param sql:
    :return:
    '''
    func_parse = {
        'insert':insert_parse,
        'delete':delete_parse,
        'update':update_parse,
        'select':select_parse,

    }
    print('sql str is %s' %sql)
    sql_l = sql.strip(' ')
    func = sql_l[0]
    res = []
    if func in func_parse:
        res=func_parse[func][sql_l]
    return res



def insert_parse(sql_l):
    '''
    定义insert语句的语法结构，执行sql解析，返回sql_dic
    :param sql:
    :return:
    '''
    sql_dic= {
        'func':insert,
        'insert':[],
        'into':[],
        'values':[],
    }
    return handle_parse(sql_l,sql_dic)



def select_parse(sql):
    pass



def update_parse(sql):
    pass




def delete_parse(sql):
    pass


def handle_parse(sql_l,sql_dic):
    '''
    执行sql解析操作，返回sql_dic
    :param sql_l:
    :param sql_dic:
    :return:
    '''
    tag = False
    for item in sql_l:
        if tag and item in sql_dic:
            tag = False
        if not tag and item in sql_dic:
            tag =True
            key = item
            continue
        if tag:
            sql_dic[key].append(item)
        if sql_dic.get('where'):
            sql_dic['where'] = where_parse(sql_dic.get('where'))
        return sql_dic


def where_parse(where_l):
    '''
    分析用户sql where的各种条件，再拼成合理的条件字符串
    :param where_l:用户输入where后对应的过滤条件列表
    :return:
    '''
    res = []
    key = ['and','or','not']
    char=''
    for i in where_l:
        if len(i) == 0:continue
        if i in key:
            if len(char) != 0:
                char = three_parse(char)
                res.append(char)
                res.append(i)
                char=''
        else:
            char += i
    else:
        char = three_parse(char)
        res.append(char)
    return  res

def three_parse(exp_str):
    '''
    将每一个小的过滤条件如,name>=1转换成['name','>=','1'
    :param exp_str:条件表达式的字符串形式,例如'name>=1'
    :return:
    '''
    key = ['>','<','=']
    res = []
    char = ''
    opt = ''
    tag = False
    for i in exp_str:
        if i in key:
            tag =True
            if len(char)  != 0:
                res.append(char)
                char = ''
            opt += i
        if not tag:
            char += i

        if tag and i not in key:
            tag=False
            res.append(opt)
            opt = ''
            char +=i
    else:
        res.append(char)
    if len(res) == 1:
        res=res[0].split('like')
        res.insert(1,'like')
    return  res


#第二部分，sql执行
def sql_action(sql_dic):
    '''
    从字典sql_dic提取命令，分发给具体的命令函数去执行
    :param sql_dic:
    :return:
    '''
    return sql_dic.get('func')(sql_dic)



def insert(sql_dic):
    print('insert %s' %sql_dic)
    db,table=sql_dic.get('into')[0].split('.')
    with open('%s/%s' %(db,table),'ab+') as fh:
        offs = -100
        while True:
            fh.seek(offs,2)
            lines = fh.readlines()
            if len(lines)>1:
                last = lines[-1]
                break
            offs *=2
        last =last.decode(encoding='utf-8')
        last_id = int(last.split(',')[0])
        new_id=last_id+1
        record=sql_dic.get('values')[0].split(',')
        record.insert(0,str(new_id))
        record_str=','.join(record)+'\n'
        fh.write(bytes(record_str,encoding='utf-8'))
        fh.flush()
    return [['insert successful']]



def select(sql_dic):
    pass




def update(sql_dic):
    pass

def delete(sql_dic):
    pass






if __name__ == '__main__':
    while True:
        sql = input('sql>').strip()
        if sql == 'exit':break
        if len(sql) ==0:continue

        sql_dic =sql_parse(sql)
        if len(sql_dic) == 0:continue

        res = sql_action(sql_dic)
        print('\033[43;1m%s\033[0m' %res[0])
        for i in res[-1]:
            print(i)




