> 在学习之前，需要各位小伙伴具有百度的搜索能力。本系列分享的每一章都是核心知识。在编程的过程当中遇到的问题可以自己百度可以解决的一定要自己解决，实在是不会再问问题。

# 前言

本次分享的知识是列表的知识，我会用三篇文章来告诉你什么是列表，以及如何使用列表。

列表能够让你在一个地方存储组成的信息，其中可以包含几个元素，也可以包含数百万的元素。列表是新手可以直接使用的强大Python功能之一。

# 列表是什么

列表是按照特定顺序排列的元素组成。你可以创建包含字符串、整型数字、浮点型数字等，也就是说可以将任何东西加入列表中，其中元素之间可以没有任何关系。列表通常包含多个元素，因此一般给列表命名的时候都是指定一个复数的名称。例如(names，letters，digits等)。

在Python中使用方括号（[]）表示列表，并用逗号分隔每一个元素。下面举一个简单的例子：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

如果让Python将列表打印出来，Python打印出的列表如下所示：

```
['trek', 'cannondale', 'redline', 'specialized']
```

## 访问列表元素

列表是一个有序的集合，因此要访问列表的任意元素，只需要将该元素的位置（索引）告诉Python即可。要访问列表元素，首先需要指出列表名称，再指出元素在列表中的位置。

例如，我想要从列表中提取第一辆自行车：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```

运行结果如下所示：

```
trek
```

注意这里只返回元素的值，不会包含方括号。

因为列表中的元素是字符串，因此将元素提取出来之后可以使用字符串的方法。例如可以使用title()方法。

具体代码如下所示：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
```

输出结果如下：

```
Trek
```

## 索引是从0开始而不是1

在Python中，第一个列表元素的索引是0。大多数编程语言都是如此规定的，这个与列表操作的底层相关。

第二个列表元素的索引值是1，根据这种访问的方式，要访问任何一个元素，只需要将其位置减1即可。，例如要访问第四个元素，可以使用索引3。

下面的例子是访问索引1和索引3：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1], bicycles[3])
```

运行结果如下：

```
cannondale specialized
```

代码返回的是二个元素和第四个元素。

Python访问最后一个元素，有特殊的方式。通过将索引指定为-1，可以让列表返回最后一个元素。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
```

运行结果如下：

```
specialized
```

这种语法还是非常不错的，因为你有可能不知道列表长度的情况下去访问列表的最后一个元素。这种约定也适用于其他负数的索引。例如：-2返回的是倒数第二个元素，-3返回倒数第三个元素，以此类推。

# 修改、添加和删除元素

在我们创建的大多数列表中，很多都是动态变化的，将随程序的运行增删元素。

## 修改列表元素

修改列表元素与访问列表元素类似，要修改元素的内容，可以先指定列表名和要修改元素的索引，再指定该元素的新值。

具体代码如下所示：

```python
motocycles = ['honda', 'yamada', 'suzuki']
print(motocycles)

motocycles[0] = 'ducati'
print(motocycles)
```

上面这段代码首先定义了一个摩托车列表，其中第一个元素是‘honda’，接下来，将第一个元素的值修改为'ducati'。

运行结果如下：

```
['honda', 'yamada', 'suzuki']
['ducati', 'yamada', 'suzuki']
```

从输出结果来看，第一个元素的值由'honda'修改成了'ducati'。

你可以修改任意位置的元素值，而不仅仅是第一个元素的值。

## 在列表中添加元素

- **1、在列表末尾添加元素**

在列表中添加新元素，最简单的方法就是将元素附加到列表中，给列表附加元素时，它将添加到列表末尾。

具体代码如下所示：

```python
motocycles = ['honda', 'yamada', 'suzuki']
print(motocycles)

motocycles.append('ducati')
print(motocycles)
```

运行结果，如下所示：

```
['honda', 'yamada', 'suzuki']
['honda', 'yamada', 'suzuki', 'ducati']
```

方法append()将元素添加到列表的末尾，不会影响到其他所有的元素。

方法append()可以让动态的创建列表变得易如反掌。例如：可以先创建一个空白列表，再一次次调用方法appen()。

具体代码如下所示：

```python
motocycles = []
motocycles.append('honda')
motocycles.append('yamada')
motocycles.append('suzuki')
print(motocycles)
```

运行结果，如下所示：

```
['honda', 'yamada', 'suzuki']
```

- **2、在列表中插入元素**

使用方法insert()可以在列表中的任何一个位置添加新的元素，因此，我们需要指定新元素的索引和值。

具体代码如下所示：

```python
motocycles = ['honda', 'yamada', 'suzuki']
print(motocycles)


motocycles.insert(0, 'ducati')
print(motocycles)
```

运行结果，如下所示：

```
['honda', 'yamada', 'suzuki']
['ducati', 'honda', 'yamada', 'suzuki']
```

在这个例子中，值'ducati'被插入到了列表的开头。方法insert()在索引0处添加空间，并将值'ducati'存储到这个地方。这种操作将列表中既有的每个元素都向后移动一个位置。

## 从列表中删除元素

- **1、使用del语句删除元素**

如果知道要删除的元素的位置，可以使用del语句。

具体代码，如下所示：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print('删除前')
print(bicycles)

print('删除后')
del bicycles[1]
print(bicycles)
```

运行结果，如下所示：

```
删除前
['trek', 'cannondale', 'redline', 'specialized']
删除后
['trek', 'redline', 'specialized']
```

从上面的结果可以看出，del语句成功的把第二个元素删除。

- **2、使用方法pop()删除元素**

方法pop()删除列表末尾的元素，并返回被删除的元素。因此，该方法时候有返回值的，可以用变量来接收。

具体代码，如下所示：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print('删除前')
print(bicycles)


print('删除的元素')
pop_bicycle = bicycles.pop()
print(pop_bicycle)
print('删除后')
print(bicycles)
```

上面的代码使用方法pop()，删除最后一个元素，再将元素的值返回并赋值给了变量pop_bicycle。

运行结果，如下所示：

```
删除前
['trek', 'cannondale', 'redline', 'specialized']
删除的元素
specialized
删除后
['trek', 'cannondale', 'redline']
```

- **3、返回列表中任意位置的元素**

实际上，可以使用方法pop()删除任意位置上的元素，只需要在括号中，传入要删除元素的索引。

具体代码，如下所示：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

pop_bicycle = bicycles.pop(2)
print(pop_bicycle)
print(bicycles)
```

当指定了元素的位置之后，就不再是删除最后一个元素了，而是删除指定元素的位置。

运行结果，如下所示：

```
redline
['trek', 'cannondale', 'specialized']
```

每当你使用一次pop()函数，被删除的值就不会再出现在列表上了。

**下面关于使用pop()方法还是del语句做简单说明：**

如果你要从列表中删除元素，并且不再使用可以用del语句；如果你要在删除元素之后继续使用它，那么就选择使用pop()方法。

**4、根据值删除元素**

有时候，你会不知道列表中元素的索引，但是只要你知道值是什么，那么就可以根据值来删除元素。可以使用remove()方法。

具体代码，如下所示：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


bicycles.remove('cannondale')
print(bicycles)
```

运行结果，如下所示：

```
['trek', 'cannondale', 'redline', 'specialized']
['trek', 'redline', 'specialized']
```

remove()方法不会返回删除的值给我们，也就是说remove()方法是没有返回值的。

如果要使用删除后的值，可以使用变量来访问。

具体代码，如下所示：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

remove_bicycle = 'cannondale'
bicycles.remove(remove_bicycle)

print('删除值')
print(remove_bicycle.title())

print('删除后')
print(bicycles)
```

运行结果，如下所示：

```
删除值
Cannondale
删除后
['trek', 'redline', 'specialized']
```

>**注意**：方法remove()只删除第一个指定的值。如果要删除的值可能在列表中存在多次，可以使用循环解决。循环的知识在以后的分享中会教会大家。

# 最后

没有什么事情是可以一蹴而就的，生活如此，学习亦是如此！

因此，哪里会有什么三天速成，七天速成的说法呢？

唯有坚持，方能成功！

**啃书君说**：

文章的每一个字都是我用心敲出来的，只希望对得起每一位关注我的人。在文章末尾点【**赞**】，让我知道，你们也在为自己的学习拼搏和努力。

**路漫漫其修远兮，吾将上下而求索**。

我是**啃书君**，一个专注于学习的人，**你懂的越多，你不懂的越多**。更多精彩内容，我们下期再见！