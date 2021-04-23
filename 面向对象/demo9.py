'''
魔术方法
1、初始化魔术方法
    触发时机：初始化对象的时候（不是实例化的时候触发，但是可以在一个操作中）
    参数：至少有一个self
    返回值：无

2、__new__
    实例化的时候触发
'''

class Person(object):
    def __init__(self, name):
        print('------->init', name)

    def __new__(cls, *args, **kwargs):
        print('--------->new')
        super(Person, cls).__new__(cls, *args, **kwargs)

# Person('aa')
person1 = Person()