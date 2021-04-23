import time


def decorate(func):
    def wapper(*args, **kwargs):
        print('正在校验中...')
        time.sleep(2)
        print('校验完毕')
        func(*args, **kwargs)

    return wapper


@decorate
def f1(n):
    print('---------f1---------', n)


@decorate
def f2(name, age, sex):
    print('-----------f2---------', name, age, sex)

@decorate
def f3(student, clazz='1904'):
    print('是{}班的学生'.format(clazz))
    for stu in student:
        print(stu)


f2('lily', 25, '男')
f1(5)
students = ['lyli', 'jack', 'jone']
f3(students)
