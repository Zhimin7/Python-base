from socket import *

# 创建套接字对象
server_socket = socket(AF_INET, SOCK_STREAM)
# 绑定端口
server_socket.bind(('', 8888))
# 监听端口
server_socket.listen()
# 等待客户端的连接
client_socket, client_info = server_socket.accept()
while True:
    recv_data = client_socket.recv(1024)
    print('客户端：', recv_data.decode('gb2312'))
    data = input('请输入你要发送的信息：')
    client_socket.send(data.encode('gb2312'))