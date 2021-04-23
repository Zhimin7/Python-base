list1 = [3, 5, 9, 2, 65, 25]
result = max(list1)
print(result)

list2 = [{'a': 20, 'b': 3}, {'a': 13, 'b': 30}, {'a': 19, 'b': 39}]
result = min(list2, key=lambda x: x['b'])
print(result)
