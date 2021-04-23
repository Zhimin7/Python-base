'''
类方法的补充
静态方法:类似于类方法
    1、需要装饰器方法
    2、静态方法无需去调用传递参数：cls、self
    3、只能访问类属性和方法，对象无法访问
    4、加载时机与类方法相同
    5、装饰器不同、无参数
    6、通过类名访问
    7、在对象创建之前调用
与普通方法的区别
1、没有装饰器
2、依赖对象，与self参数
3、对象创建之后调用
'''


class Person(object):
    __age = 10  # 私有

    def __init__(self, name):
        self.name = name

    def show(self):
        print('--------->', self.__age)

    @ classmethod
    def update_age(cls):
        print('----------->类方法')
        cls.__age = 20

    @ classmethod
    def show_age(cls):
        print('修改后的年龄是：', cls.__age)

    @ staticmethod
    def test():
        print('----------->静态方法')
        print(Person.__age)



p1 = Person('张三')
Person.update_age()
Person.show_age()
Person.test()
# p1.age = p1.age + 1
# p1.show()

