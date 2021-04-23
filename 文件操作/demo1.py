stream = open('./aa.txt')
# ss = stream.read()
# result = stream.readable()
# print(ss)
# print(result)
# line = stream.readline()
# print(line)
# while True:
#     if not line:
#         break
#     else:
#         print(line)
while True:
    line = stream.readline()
    print(line,end='')
    if not line:
        break
