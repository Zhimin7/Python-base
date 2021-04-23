# 装饰器的定义是函数作为参数

def func(number):
    a = 0

    def inner_func():
        nonlocal a
        for i in range(number + 1):
            a += i
        print('修改后的a=', a)

    return inner_func


f = func(100)
f()


