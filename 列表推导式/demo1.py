'''
列表推导式


格式：
    [表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if 条件]
'''
'''
string.capitalize()与string.title()的区别：
    capitalize：使整个字符串的首字母大写
    title:使整个字符串内的单词首字母大写

'''

names = ['tom', 'lily', 'abc', 'jack', 'steven', 'bob']
# name = [name.capitalize() for name in names if len(name)>3]
name = [name.title() for name in names if len(name) > 3]
print(name)

# name = filter(lambda x: len(x) > 3, names)
# print(list(name))

# 将1-100的数能被3整除的数取出
# list1 = [i for i in range(1, 101) if i % 3 == 0]
# print(list1)
newlist = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(newlist)
# for i in range(5):
#     if i % 2 == 0:
#         for j in range(10):
#             if j % 2 != 0:
#                 newlist.append((i,j))
#
#
# print(newlist)
