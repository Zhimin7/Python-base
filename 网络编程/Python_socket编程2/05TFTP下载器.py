import struct
from socket import *

filename = 'face.jpg'
server_ip = '127.0.0.1'
# 封装读请求
send_data = struct.pack('!H%dsb5sb' % len(filename), 1, filename.encode(), 0, 'octet'.encode(), 0)

# 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.sendto(send_data, (server_ip, 69))
# 本地创建一个文件
f = open(filename, 'ab')
while True:
    recv_data = udp_socket.recvfrom(1024)
    # print(recv_data)
    number, ack_num = struct.unpack('!HH', recv_data[0][:4])
    # 判断操作码是否是5
    # print('number', number)
    if number == 5:
        print('文件不存在')
        break
    f.write(recv_data[0][4:])
    if len(recv_data[0]) < 516: # 表示读完
        break
    else:
        ack_data = struct.pack('!HH',4, ack_num)
        rend_port = recv_data[1][1]
        udp_socket.sendto(ack_data, (server_ip, rend_port))