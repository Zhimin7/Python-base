# 闭包的同级调用

def func():
    a = 100

    def inner_func1():
        b = 90
        s = a + b
        print('sum=', s)

    def inner_func2():
        inner_func1()
        print('-------->inner func2')

    return inner_func2

f = func()
print(f)
f()
