'''
斐波那契数列
0,1,1,2,3,5,8

yield 相当于return + 暂停

当生成器里面没有内容时会返回return里面的值，当然你要有return
'''

def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield a
        a, b = b, a+b
        n += 1



x = fib(100)
new_list = []
for i in range(100):
    new_list.append(x.__next__())

print(new_list)

