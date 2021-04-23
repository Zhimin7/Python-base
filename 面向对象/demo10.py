'''
私有化

'''

class Student(object):

    def __init__(self,name, age):
        self.__name = name
        self.__age = age
        self.__score = 59   # 私有化

    # 定义共有的set和get方法
    def set_age(self, age):

        if 0 < age <= 120:
            self.__age = age
        else:
            print('年龄不在指定范围')
        # self.__name = name
        # self.__score = score

    def get_age(self):
        return self.__age



    def __str__(self):
        return 'name:{},age{},score:{}'.format(self.__name,self.__age,self.__score)


xiaogu = Student('小古',25)
print(xiaogu)
xiaogu.set_age(20)
print(xiaogu)
print(xiaogu.get_age())
print(dir((Student)))
print(xiaogu._Student__age)
print(xiaogu.__dir__())