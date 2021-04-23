from socket import *
from threading import Thread

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('', 8989))


# 接收数据
def recv():
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print('<<%s>>:%s' % (recv_data[1], recv_data[0].decode('gb2312')))


# 发送数据
def send():
    while True:
        data = input('>>: \n').encode('gb2312')
        ip_port = ('192.168.1.105', 8080)
        udp_socket.sendto(data, ip_port)


if __name__ == '__main__':
    t1 = Thread(target=send)
    t2 = Thread(target=recv)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
