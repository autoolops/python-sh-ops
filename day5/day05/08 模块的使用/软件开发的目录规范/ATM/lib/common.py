from conf import settings

def logger(msg):
    with open(settings.LOG_PATH,'a',encoding='utf-8') as f:
        f.write('2018-5-5 11:11:11 %s 注册成功\n' %msg)