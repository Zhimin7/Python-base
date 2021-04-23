# 前言

在上一篇文章中教会了大家如何创建了列表，还学习了如何操作列表元素。

接下来我就将上次分享给大家的内容先总结整理给各位小伙伴，具体如下图所示：

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/%E5%88%97%E8%A1%A8%E7%9A%84%E4%BD%BF%E7%94%A8.png)

本次文章主要为大家分享如何遍历整个列表，这只需要几行代码就可以，无论列表有多长，循环能够让你对列表中的每一个元素采取一个或者是一系列相同的措施，从而高效的使用列表。

# 遍历整个列表

当我们需要遍历整个列表，并对列表元素执行相同的操作时，可以巧妙的使用**for**循环。

假设我们有一个由名字组成的列表，需要将这些名字都取出来。因此，我们可以分别获取列表中的每一个名字，但是，这种做法会引发一些问题，如果列表的长度太长，将包含大量的重复代码。另外，当列表的长度发生变化时，都必须修改代码。通过for循环可以轻松解决这个问题。

具体代码如下所示：

```python
magicains = ['alice', 'david', 'carolina']
for magicain in magicains:
	print(magicain)
```

先定义一个for循环，这行代码让Python从列表magicains中取出一个名字，并将其与变量magicain关联，最后，让Python打印前赋给变量magicain，这样，对于列表中的每一个名字，Python都将重复执行第二行和第三行的代码。直到处理最后一个元素，如果for循环后面没有代码行，则程序运行结束。

## 在for循环执行更多的操作

在for循环中，可对每个元素执行任何操作。具体代码如下所示：

```python
magicains = ['alice', 'david', 'carolina']
for magicain in magicains:
	print(f'{magicain.title()}, that was a great trick!')
```

运行结果如下所示：

```
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
```

这个循环第一次迭代时，变量magicain的值为'alice'，因此，Python打印第一条消息的抬头为'Alice'；第二次迭代时，抬头为：'David'，第三次抬头为：'Carolina'。

在for循环内，想包含多少行代码都是可以的，每个缩进的代码行都是循环的一部分，针对列表中的每一个元素都执行一次。因此，可以对列表中的每一个值执行任意操作。

```python
magicains = ['alice', 'david', 'carolina']
for magicain in magicains:
	print(f'{magicain.title()}, that was a great trick!')
	print(f"I can't wait to see your next trick, {magicain.title()}.\n")
```

在上面的for循环中，两个函数调用的print()都缩进了，因此他们都针对列表中的每一个元素执行一次。第二个print()函数写入了换行符，在每一次迭代结束之后插入一个换行符。

运行结果，如下所示：

```
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```

## 在循环结束后再执行一些操作

for循环结束之后，没有缩进的代码都只执行一次，不会重复执行。

具体代码，如下所示：

```python
magicains = ['alice', 'david', 'carolina']
for magicain in magicains:
	print(f'{magicain.title()}, that was a great trick!')
	print(f"I can't wait to see your next trick, {magicain.title()}.\n")
print('Thank you, everyone. That was a great magic show!')
```

从上面的代码可以看到，开头的两个print()函数是重复执行，然后第三个函数没有在for循环内缩进，因此，只执行一次。

运行结果，如下所示：

```
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!
```

# 避免缩进

Python根据缩进来判断代码行与前一个代码行之间的关系。Python通过缩进让代码更易读。简单的来说，它要求你使用缩进让代码让代码整洁而结构清晰。

# 创建数值列表

要存储一组数的原因有很多，在数据可视化中，处理的几乎是由数（如温度、距离、人口数量、经度和纬度）组成的集合。

列表非常适合用于存储数字的集合，而Python提供了很多工具，可以帮助你提高数据列表。

## 使用函数range()

python函数range()让你能够轻松地生成一系列数，使用range()函数打印一系列数。

具体代码，如下所示：

```python
for value in range(1, 5):
	print(value)
```

运行结果，如下所示：

```
1
2
3
4
```

在这个示例中，range ()函数只打印数1-4，这是编程语言中差一行的结果。函数range()让Python从指定的第一个值开始，并到达你指定的第二个数停止。因为它在第二个值处停止，所以输出不包含该值。

要打印数1-5，需要使用range(1, 6)

```python
for value in range(1, 6):
	print(value)
```

运行结果，如下所示：

```
1
2
3
4
5
```

## 使用range()函数创建数字列表

要创建数字列表，可以使用函数list()将range()的结果直接转换为列表。如果将range()作为list()的参数，输出将是一个数字列表。

具体代码，如下所示：

```python
numbers = list(range(1, 5))
print(numbers)
```

运行结果，如下所示：

```
[1, 2, 3, 4]
```

使用range()函数时，还可以指定步长。为此，可以给这个函数指定三个参数，Python将根据这个步长来生成数。

```python
numbers = list(range(2, 11, 2))
print(numbers)
```

运行结果，如下所示：

```
[2, 4, 6, 8, 10]
```

使用range()几乎可以创建任何需要的数集。例如，创建一个列表，其中包含前10个整数（1-10）的平方？在Python中，用两个(**)表示乘方运算。

具体代码，如下所示：

```python
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)
```

这段代码，首先创建一个空的列表，接下来使用range()函数，让Python遍历1-11的值。在循环中，计算当前值的平方，并将结果赋值给变量square，然后将计算得到的平方值，附加到列表squares中。

当然，上面的代码也可以这样写：

```python
squares = []
for value in range(1, 11):
	# square = value ** 2
	squares.append(value ** 2)
print(squares)
```

运行结果，如下所示：

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

运行上面的两段代码，你会发现它们的运行结果是相同的。

## 对数字列表执行简单的统计计算

有几个专门处理数字列表的函数。例如，你可以轻松的找出数字列表的最大值、最小值和总和。

具体代码，如下所示：

```python
digits = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

min_digit = min(digits)
max_digit = max(digits)
sum_digit = sum(digits)

print('min_digit：',min_digit, '\nmax_digit：',max_digit, '\nsum_digit：',sum_digit)
```

运行结果，如下所示：

```
min_digit： 1
max_digit： 100
sum_digit： 385
```

- min()函数：返回列表的最小值
- max()函数：返回列表的最大值
- sum()函数：返回列表的总和

# 使用列表的一部分

要处理列表的所有元素，可以使用for循环可以轻松解决。当然我们也可以处理列表的部分元素，Python称之为**切片**。

## 切片

要创建切片，可以指定第一个元素和最后一个元素的索引。与函数range()一样，Python到达第二个索引之前的元素就会停止。要输出列表中的前三个元素，只需要指定索引0和索引3，这样返回的元素有索引0、1和2

具体代码，如下所示：

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```

运行结果，如下所示：

```
['charles', 'martina', 'michael']
```

**注意**：

- 如果没有指定第一个索引，Python将自动从列表的开头开始
- 如果没有指定最后一个索引，Python将自动取到列表的末尾

具体代码，如下所示：

```python
player = ['charles', 'martina', 'michael', 'florence', 'eli']
print(player[:3])
print(player[2:])
```

运行结果，如下所示：

```
['charles', 'martina', 'michael']
['michael', 'florence', 'eli']
```

## 复制列表

我们经常需要根据既有的列表创建全新的列表。下面来介绍一下复制列表的工作原理。

要复制列表，可以创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。这让Python创建一个始于第一个元素，终于最后一个元素的切片，即整个列表的副本。

具体代码，如下所示：

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

print("\n my friend's favorite foods are:")
print(friend_foods)
```

首先创建了一个食品列表，名为my_food。然后创建一个名为friend_foods的新列表。在不指定任何索引的情况下，从列表my_foods中提取切片，从而创建这个列表的副本，并副本赋给变量friend_foods。

运行结果，如下所示：

```
['pizza', 'falafel', 'carrot cake']
['pizza', 'falafel', 'carrot cake']

 my friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']
```

从上面的运行结果可以看出，两个列表打印的内容是相同的。

为了核实有两个列表，下面在每个列表中都添加一种食品。

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)
```

运行结果，如下所示：

```
['pizza', 'falafel', 'carrot cake', 'cannoli']
['pizza', 'falafel', 'carrot cake', 'ice cream']
```

你会看到两个列表分别被添加了一种食品。

因此，很明确，这就是两个不同的列表。

如果只是将my_foods赋值给friend_foods，就不能得到两个列表。

具体代码，如下所示：

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)
```

运行结果，如下所示：

```
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
```

从上面的代码，你可以看出，我其实是两个列表分别添加一个元素，但是打印出来的结果却是两个列表都添加了两个元素。

这是因为，当我的复制方法不是切片，而是将变量直接赋值的时候，两个列表便都指向了相同的地址，因此，你也可以理解friend_foods与my_foods其实是同一个列表。

# 最后

没有什么事情是可以一蹴而就的，生活如此，学习亦是如此！

因此，哪里会有什么三天速成，七天速成的说法呢？

唯有坚持，方能成功！

**啃书君说**：

文章的每一个字都是我用心敲出来的，只希望对得起每一位关注我的人。在文章末尾点【**赞**】，让我知道，你们也在为自己的学习拼搏和努力。

**路漫漫其修远兮，吾将上下而求索**。

我是**啃书君**，一个专注于学习的人，**你懂的越多，你不懂的越多**。更多精彩内容，我们下期再见！

