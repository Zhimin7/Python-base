# 导入模块
from socket import *


# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 发送地址
ip_port = ('192.168.1.105', 8080)
# 键盘获取信息
data = input('请输入要发送的信息').encode('gb2312')
# 发送数据
udp_socket.sendto(data, ip_port)
# 关闭套接字
udp_socket.close()