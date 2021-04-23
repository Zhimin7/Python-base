# map 函数

list1 = [1, 25, 6, 8, 9, 5, 6, 2, 0, 0]
result = map(lambda x: x + 2, list1)
print(list(result))
list2 = [1, 25, 6, 8, 9, 5, 6, 2, 0, 0]

# for index, i in enumerate(list2):
#     list2[index] = i + 2
#
# print(list2)

even = map(lambda x: x if x % 2 == 0 else x+1, list2)
print(list(even))



