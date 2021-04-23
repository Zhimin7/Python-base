# def func(names):
#     for name in names:
#         print(name)
#
#
# name_list = ['aa', 'bb', 'cc']
# func(name_list)


class Phone(object):
    # 魔术方法之一:创建对象就是执行
    def __init__(self):
        print('----------->init')
        # 动态给self添加两个属性：brand和price
        self.price = 500
        self.brand = '小米'

    def call(self): # self 是不断改变的
        print('call', self.price)   # 不能保证每一个self都有price


p1 = Phone()
# print(p1)
