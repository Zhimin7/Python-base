'''
在开发中的私有化处理
'''

class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        # self.score = 59   # 私有化

    @property
    def age(self):
        return self.__age

    # 定义共有的set和get方法
    @age.setter
    def age(self, age):

        if 0 < age <= 120:
            self.__age = age
        else:
            print('年龄不在指定范围')
        # self.__name = name
        # self.__score = score

    def get_age(self):
        return self.__age


student1 = Student('peng',20)
student1.name = 'xiaopeng'
print(student1.name)
print(student1.age)