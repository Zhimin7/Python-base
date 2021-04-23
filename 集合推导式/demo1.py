# 集合推导式
'''
在列表推导式添加去除重复项的功能
'''

list1 = [1, 2, 1, 3, 5, 2, 1, 8, 9, 7]
set1 = {x for x in list1 if x > 5}
print(set1)
set2 = set(list1)
print(set2)

# 字典推导式
dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
newdict = {value: key for key, value in dict1.items()}
print(newdict)
