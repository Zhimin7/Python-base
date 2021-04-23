'''
类方法的补充

'''


class Person(object):
    __age = 10  # 私有

    def show(self):
        print('--------->', self.__age)

    @ classmethod
    def update_age(cls):
        print('----------->类方法')
        cls.__age = 20

    @ classmethod
    def show_age(cls):
        print('修改后的年龄是：', cls.__age)


p1 = Person()
Person.update_age()
Person.show_age()
# p1.age = p1.age + 1
# p1.show()

