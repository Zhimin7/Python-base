def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp:',temp)
        i += 1
    return '没有更多的数据'


g = gen()
# 还未进入yield不能传值
g.send(None)
n1 = g.send('haha') # 相当于触发生成器
print(n1)
print(g.__next__())