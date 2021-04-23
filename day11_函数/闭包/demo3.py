# 闭包的作用
'''
闭包有什么缺点
1、作用域没有那么直观
2、因为变量不会被垃圾回收，所以有一定的内存占用问题

'''

def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print('a+b+c = ', s)

    return inner_func


ifunc = func(6,9)
ifunc1 = func(2,8)
print(ifunc1)
print(ifunc)
ifunc()
ifunc1()
