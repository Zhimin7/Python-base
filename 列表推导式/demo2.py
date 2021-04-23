dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'lucy', 'salary': 8000}
dict3 = {'name': 'jack', 'salary': 4000}
dict4 = {'name': 'mike', 'salary': 6000}

list1 = [dict1, dict2, dict3, dict4]

# salary = [s['salary']+500 for s in list1 if s['salary'] >= 5000]
salary = [employee['salary'] + 500 if employee['salary'] > 5000 else employee['salary'] + 200 for employee in list1]
print(salary)
# print(salary)
