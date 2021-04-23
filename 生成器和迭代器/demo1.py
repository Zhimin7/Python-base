'''
通过列表生成式（列表推导式）：我们可以直接创建一个列表
但是，受到内存限制，列表容量肯定是有限的
而且创建一个包含100万个元素的列表，不仅占用很大的存储空间
如果我们仅仅是访问前面几个元素，那后面大多数元素占用的空间就白白浪费了
这样就不必创建完整的list，从而节省大量的空间，在Python中这样一边循环一边计算的机制，称为生成器：generator
'''
try:
    newlist = [x*3 for x in range(5)]
    print(newlist)
    # 生成器对象
    x = (x*3 for x in range(5))
    print(x)
    # 通过__next__()
    print(x.__next__())
    # 每调用一次next就下一个
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
except StopIteration:
    print('生成器无元素')