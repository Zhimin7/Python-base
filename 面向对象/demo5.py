'''
类方法
    定义方式：依赖装饰器classmethod
    类方法里面的参数：是当前类
    类方法中只能对使用类属性
    类方法能否使用普通方法


类方法：
    只能访问类属性和类方法，在创建对象之前，完成功能

'''


class Dog(object):
    nickname = 'aa'

    def __init__(self, nickname):
        self.nickname = nickname    # 动态添加Nickname

    def run(self):  # self依赖对象
        print('{}在院子里跑来跑去'.format(self.nickname))

    def eat(self):
        print('正在吃饭')
        self.run()  # 类中方法的调用:self.方法名()

    @classmethod
    def test(cls):  # cls 依赖类   指的是Dog类
        print(cls)
        print(cls.nickname)
        # print()
        # cls.run()



# dog1 = Dog('大黄')
# dog1.run()
# dog1.test()
Dog.test()
