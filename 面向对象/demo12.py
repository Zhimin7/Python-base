'''
继承
'''
import random


class Road(object):
    def __init__(self, name, len):
        self.len = len
        self.name = name


class Car(object):
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}公路上以{}的时速行驶了{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的，速度{}'.format(self.brand, self.speed)


# 创建实例化对象
r = Road('京藏高速', 12000)

aodi = Car('奥迪', 120)
# print(aodi)
aodi.get_time(r)