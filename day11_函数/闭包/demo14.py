import time

is_login = False


def login():
    username = input('输入用户名：')
    password = input('请输入密码：')
    if username == 'admin' and password == '123456':
        return True
    else:        
        return False


# 定义一个装饰器函数
def login_required(func):
    def wapper(*args, **kwargs):
        global is_login
        print('-------付款--------')
        if is_login:
            func(*args, **kwargs)
        else:
            print('你还没有登录，无法付款')
            is_login = login()
            if is_login:
                func(*args, **kwargs)

            print('result:', is_login)

    return wapper


# 定义一个付款函数
@login_required
def pay(money):
    print('正在付款，付款金额是{}元'.format(money))
    print('付款中。。。。')
    time.sleep(2)
    print('付款完成')


pay(100)
# pay(200)
