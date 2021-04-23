'''
在装饰器如果存在参数，则需要三层函数
'''

def outer(a):
    def decorate(func):
        def wapper():
            func()
            print('------>铺{}块地砖'.format(a))
        return wapper
    return decorate


@outer(100)
def house():
    print('我是毛胚房')


house()