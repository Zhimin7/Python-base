from socket import *

clicent_socket = socket(AF_INET, SOCK_STREAM)
ip_port = ('192.168.66.32', 8888)
clicent_socket.connect(ip_port)
while True:
    msg = input('请你输入你要发送的信息：')
    clicent_socket.send(msg.encode('gb2312'))
    recv_data = clicent_socket.recv(1024)
    print('服务端：', recv_data.decode('gb2312'))