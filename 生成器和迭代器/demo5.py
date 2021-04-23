# 进程、线程、协程
'''
生成器的定义方式：两种

'''

def tesk1(n):
    for i in range(n):
        print('正在搬第{}砖'.format(i))
        yield None


def tesk2(n):
    for i in range(n):
        print('正在听{}首歌'.format(i))
        yield None



g1 = tesk1(5)
g2 = tesk2(5)

# for i in range(5):
#     print(next(g1))
#     print(next(g2))

while True:
    g1.__next__()
    g2.__next__()


