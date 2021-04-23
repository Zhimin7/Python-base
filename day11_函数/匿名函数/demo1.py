# 匿名函数：简化函数定义
# a = 5
# b = 10
# var = lambda a, b: a + b
# print(var(1, 2))


def func(x, y, func):
    print(func)
    print(x, y)
    s = func(x, y)
    print(s)


func(1, 2, lambda a, b: 1 + 2)
