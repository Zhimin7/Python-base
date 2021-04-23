# 导入模块
from socket import *
# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
ip_port = ('192.168.2.212', 8080)
# 键盘获取信息
data = input('请输入你要发送的数据：').encode('gb2312')
# 发送数据
udp_socket.sendto(data, ip_port)
udp_socket.close()