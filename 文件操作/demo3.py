import os

# path = r'D:\github\Python_base\文件操作\demo1.py'
# result = os.path.split(path)
# print(result[0])
# size = os.path.getsize(path)    # 获取文件的大小，以字节表示
# result = os.path.join(os.getcwd(),'flie', 'a.jpg')
# print(size)
# print(result)
# dir = os.listdir('D://')
# print(dir)

# 创建文件夹
path = r'D:\github\Python_base\文件操作\新建文件夹1'
# os.mkdir(path)

if not os.path.exists(path):
    os.mkdir(path)


# os.rmdir(path)  # 只能删除空目录
os.remove(path+r'\\新建文本文档.txt')


