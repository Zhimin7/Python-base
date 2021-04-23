# 导入模块

from socket import *
server_socket = socket(AF_INET, SOCK_STREAM)
# 绑定端口与IP地址
server_socket.bind(('', 9999))
# 监听端口
server_socket.listen(5)
# 等待客户端连接
client_socket, client_info = server_socket.accept()
# 获取客户端发送的数据
recv_data = client_socket.recv(1024)
print('%s :  %s' % (client_info, recv_data.decode('gb2312')))
client_socket.close()
server_socket.close()
