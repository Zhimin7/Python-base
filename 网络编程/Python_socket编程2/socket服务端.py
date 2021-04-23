from socket import *

# 创建socket对象
server_socket = socket(AF_INET, SOCK_STREAM)
# 绑定IP地址
ip_port = ('127.0.0.1', 8000)
server_socket.bind(ip_port)

# 监听端口
server_socket.listen(5)
# 等待连接
while True:
    conn, addr = server_socket.accept() # 建立连接
    # 接收数据
    recv_data = conn.recv(2048)
    # 返回数据
    conn.send(b'ok')
    conn.close()


