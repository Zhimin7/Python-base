import os


path = r'D:\github\Python_base\文件操作\新建文件夹1'
filelist = os.listdir(path)
for file in filelist:
    path1 = os.path.join(path, file)
    os.remove(path1)
else:
    os.rmdir(path)
print('删除完成')