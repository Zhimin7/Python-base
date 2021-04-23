class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print('{}正在吃{}'.format(self.name, food))

    def run(self):
        print('{},今年{}岁了，正在跑步'.format(self.name, self.age))


p1 = Person('张三', 15)
p1.eat('红烧肉')
p1.run()
p2 = Person('李四', 25)
p2.eat('东坡肉')
p2.run()
