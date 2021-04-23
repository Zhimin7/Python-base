'''
继承
'''


class Animal():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('吃饭')

    def sleep(self):
        print('睡觉')


class Person(Animal):
    def __init__(self, name, age, sex, hobby):
        Animal.__init__(self, name, age, sex)
        self.hobby = hobby

    def work(self):
        print('工作')


class Dog():
    pass


class Cat():
    pass


p = Person('小明', 22, '男', '踢足球')
print(p.hobby)
