# 导入模块
from socket import *

# 创建socket套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 发送的地址
ip_port = ('192.168.2.212', 8080)
# 绑定IP地址与端口号
udp_socket.bind(('', 8989))
# 从键盘获取发送的信息
data = input('请输入你要发送的数据：').encode('gb2312')
# 发送数据
udp_socket.sendto(data, ip_port)
# 接收数据
recv_data = udp_socket.recvfrom(1024)   # 接收数据的最大字节数
print('%s : %s' % (recv_data[1], recv_data[0].decode('gb2312')))
udp_socket.close()
