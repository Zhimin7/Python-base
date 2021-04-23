'''
类方法
动作
种类：普通方法、类方法、静态方法、魔术方法
'''


class Phone(object):
    brand = 'xiaomi'
    price = 4000
    type = 'mate 40'

    # self 的作用:self就是对象本身
    def call(self):
        print('self-----', self)
        print('正在打电话', self.note)


phone1 = Phone()
phone2 = Phone()
phone1.note = 'phone1的note'
# phone2.note = 'phone2的note'
# print(phone1.call())
# phone1.call()
# print(phone1)
phone1.call()
phone2.call()

