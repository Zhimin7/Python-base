'''
抛出异常
'''

'''
注册，用户名必须是6位

'''

def register():
    username = input('输入用户名：')
    if len(username) < 6:
        raise Exception('用户名必须超过6位')
    else:
        print('输入的用户名：',username)

try:
    register()
except Exception as err:
    print(err)
    print('注册失败')
else:
    print('注册成功')