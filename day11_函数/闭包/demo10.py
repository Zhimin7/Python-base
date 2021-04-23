'''

如果装饰器是多层的，则优先使用离你较近的装饰器

'''


def zhang1(func):
    print('------->start')
    func()
    def wapper(*args, **kwargs):
        print('刷漆')

    print('------->end')
    return wapper


def zhang2(func):
    print('--------->start')
    func()

    def wapper(*args, **kwargs):
        print('铺地')

    print('------->end')
    return wapper

@zhang2
@zhang1
def house():
    print('我是毛胚房')


house()
