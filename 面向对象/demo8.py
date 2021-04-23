class Cat(object):
    type = '猫'

    def __init__(self, nickname, color, age):
        self.nickname = nickname
        self.color = color
        self.age = age

    def eat(self, food):
        print('{}喜欢吃{}'.format(self.nickname, food))

    def catch(self, color):
        print('{}抓了一只{}颜色的大老鼠'.format(self.nickname, color))

    def sleep(self, hour):
        if hour < 5:
            print('继续睡觉吧')
        else:
            print('赶快起床，去抓老鼠')

    def show(self):
        print(self.nickname, self.color, self.age)


cat1 = Cat(nickname='花花', color='black', age=24)
cat1.show()