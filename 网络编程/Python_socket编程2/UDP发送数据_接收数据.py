# 导入模块
from socket import *


# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 发送地址
ip_port = ('192.168.1.105', 8080)
# 绑定端口
udp_socket.bind(('', 8989)) # 绑定本地ip，端口是8989
# 键盘获取信息
data = input('请输入要发送的信息').encode('gb2312')
# 发送数据
udp_socket.sendto(data, ip_port)
# 接收数据
recv_data = udp_socket.recvfrom(1024) # 接收数据的最大字节数
# print(recv_data)
# (b'\xc4\xe3\xba\xc3\xa3\xac\xc7\xeb\xce\xca\xd3\xd0\xca\xb2\xc3\xb4\xce\xca\xcc\xe2', ('192.168.1.105', 8080))
print('接收到%s的信息是：%s' % (recv_data[1], recv_data[0].decode('gb2312')))
# 关闭套接字
udp_socket.close()