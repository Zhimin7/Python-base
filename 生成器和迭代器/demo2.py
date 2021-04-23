# 定义生成器的方式：用函数完成
'''
在函数中出现yield,说明该函数不再是函数，是生成器

'''

def func():
    n = 0
    while True:
        n += 1
        yield n


x = func().__next__()
print(x)