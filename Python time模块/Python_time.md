# Python3时间和日期

Python程序能用多种方式处理时间和日期，转化格式是一个常见的功能。

现在我就用time模块可以用于格式化时间和日期。

时间间隔是以秒为单位的浮点小数

每个时间戳都是1970年1月1日午夜经历了多长时间来表示。

Python的time模块下有很多函数可以转换常见的日期格式，time.time()用于获取当前时间戳

**实例**

```python
import time


# 每个时间戳都是自从1970年1月1日经历了多长时间来表示
ticks = time.time()
print('当前的时间戳是：', ticks)
```

## 获取当前时间

从返回浮点数的方式向时间元组转换，只要将浮点数传递个localtime()函数

```python
import time


local_time = time.loacaltime(time.time())
print('本地时间是：', local_time)
```

## 获取格式化的时间

你可以根据需要选取的格式，但是最简单的获取可读的时间模式的函数是asctime()

```python
import time


local_time = time.asctime(time.localtime(time.time()))
print('本地时间是', local_time)
```

## 格式化日期

