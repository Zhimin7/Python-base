def decorate(func):
    a = 100
    print('wapper执行开始')

    def wapper():
        func()
        print('安装门窗')
        print('铺地板')
        print('刷漆')
    print('wapper执行结束')

    return wapper

@decorate
def house():
    print('我是毛胚房')


'''
@decorate
1、house为被装饰函数
2、将被装饰函数给装饰器decorate
3、执行decorate函数
4、将装饰函数的返回值赋值给被装饰函数
'''

house()

