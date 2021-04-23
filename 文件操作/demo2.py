'''
写文件
mode:w模式，表示写操作
方法：write
关闭资源再打开会先清空，在写入


'''
stream = open('./aa.txt',mode='w')
# stream.close()
# container = stream.read()
# print(container)
s = '''欢迎来到我的世界
'''
s1 = '古哥哥'
result = stream.write(s)
stream.write(s1)
print(result)
stream.close()

