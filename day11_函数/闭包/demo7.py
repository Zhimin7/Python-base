# 函数作为参数出现
# 要有闭包的特点出现

def test():
    print('-------test')


def func(f):
    print(f)
    f()
    print('---------func')


func(test)
