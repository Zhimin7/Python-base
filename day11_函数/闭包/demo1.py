'''
闭包的特点：
1、存在内部函数
2、外部函数有返回值
3、返回值是内部函数名（函数名不加括号）
4、内部函数还引用外部函数的变量值
'''


def func():
    a = 100

    def inner_func():
        b = 99
        print(a, b)

    print(locals())
    return inner_func


x = func()
x()
