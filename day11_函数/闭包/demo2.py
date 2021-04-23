def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print('a+b+c = ', s)

    return inner_func


ifunc = func(6,9)
ifunc()
