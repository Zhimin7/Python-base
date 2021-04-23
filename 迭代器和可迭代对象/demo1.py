'''
可迭代对象：列表、元组、字典、集合、字符串
判断一个对象是否是可迭代对象
可迭代对象不一定是迭代器
生成器也是可迭代的，也是一个迭代器
'''

from collections.abc import Iterable

#
list1 = [1, 2, 3, 6, 6, 5]
list1 = iter(list1) # 将可迭代对象，变成迭代器
print(next(list1))
# f = isinstance(list1, Iterable)
# print(f)

# g = (x+1 for x in range(10))
# f = isinstance(g, Iterable)
# print(f)

# 迭代器

'''
迭代器是访问集合的一种方式，迭代器是一种可以访问位置的对象。
迭代器对象从集合的第一个元素开始访问，知道所有元素被访问结束
迭代器只能往前，不能后退

可以用next获取下一个元素

'''
