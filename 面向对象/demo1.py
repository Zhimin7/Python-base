'''
面向对象

    类
    对象
    属性  ： 特征
    方法： 动作

'''

# 所有的类名要求首字母大写，多个单词使用驼峰命名法
class Student(object):
    name = '啃书君'
    age = 22


print(Student)
kenshujun = Student()
kenshujun.age = 23
print(kenshujun.age)
