# 导入模块
from socket import *
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('192.168.2.212', 9999))
server_socket.listen()
client_socket, client_info = server_socket.accept()
recv_data = client_socket.recv(1024)
print('%s : %s' % (client_info, recv_data.decode('gb2312')))
client_socket.close()
server_socket.close()