class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭')

    def run(self):
        print(self.name + '正在跑步')


class Student(Person):
    def __init__(self, name, age, clazz):
        super().__init__(name, age)
        self.clazz = clazz

    def study(self, course):
        print(self.name + '正在学习{}'.format(course))

    def eat(self):
        print(self.name + '正在吃沙拉')


class Doctor(Person):
    def __init__(self, name, age, patients):
        super().__init__(name, age)
        self.patients = patients


class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager


s = Student('jack', 18, 'python2020')
s.run()
s.study('python')
s.eat()
