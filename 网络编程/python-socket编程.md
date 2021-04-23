# Python socket编程

socket是应用层与TCP/IP协议簇通信的中间软件的抽象层，它是一组接口。在设计模式中，socket其实就是一个门面模式，它把复杂的TCP/IP协议簇隐藏在socket接口的后面，对于用户来说，一组接口就代表全部，让socket去组织数据，以符合指定的协议。

所以，我们可以无需深入了解TCP/IP协议，socket给我们封装好了，只需要按照socket规定去编写程序即可。

## socket 协议簇

* 基于同一台电脑的套接字家族；套接字家族名字：AF_UNIX
* 基于服务器与服务器的套接字家族；套接字家族的名字：AF_INIT

## socket套接字类型

**SOCK_STREAM**	基于TCP的流式socket通信

**SOCK_DGRAM**	基于UDP的流式socket通信

**SOCK_RAW**		原始套接字，普通套接字无法处理ICMP、IGMP的套接字	

**SOCK_SEQPACKET**	可靠的连续数据包服务

一般只用`SOCK_STREAM`和`SOCK_DGRAM`

`SCOK_STREAM`是基于TCP协议的套接字，而`SOCK_DGRAM`是基于UDP协议的套接字。

通过观察源码，可以发现socket是一个类，那么类里面就会有很多的方法和属性。截取一部分代码，如下所示：

```python
class socket(_socket.socket):

    """A subclass of _socket.socket adding the makefile() method."""

    __slots__ = ["__weakref__", "_io_refs", "_closed"]

    def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
        # For user code address family and type values are IntEnum members, but
        # for the underlying _socket.socket they're just integers. The
        # constructor of _socket.socket converts the given argument to an
        # integer automatically.
        if fileno is None:
            if family == -1:
                family = AF_INET
            if type == -1:
                type = SOCK_STREAM
            if proto == -1:
                proto = 0
        _socket.socket.__init__(self, family, type, proto, fileno)
        self._io_refs = 0
        self._closed = False
```

从上面的注释中可以看出，协议簇和套接字是必传的参数，因为这两个属于成员变量。

## socket层的位置

socket层是位于应用层和运输层之间的。

在真正学习socket编程之前，需要先了解网络编程的几个重要概念！

# IP地址与端口

## IP地址

ip地址是网络中通信实体的地址，通信实体可以时计算机、手机、路由器和服务器等等。比如说网络中每个服务器都有自己的ip地址，在局域网中每个电脑也要配置自己的ip地址，路由器是连接两个网络或者是多个网络的设备。

> **注意事项**
>
> 127.0.0.1 表示的是本机地址
>
> 192.168.0.0--192.168.255.255为私有地址，属于非注册地址，专门为组织机构内部使用。

## 端口

IP地址用来标识一台计算机，但是一台计算机可能提供多种网络应用程序，那么如何来区分不用的应用程序呢？这就要运用端口了。

端口是虚拟的概念，并不是说主机里真有这些端口。通过端口，一台主机可以运行不同的应用程序。端口的表示是一个十六位的二进制整数，对应十进制的0-65535

>**注意**
>
>端口号小于256的定义为常用端口，服务器一般都是通过常用端口来识别的。任何TCP/IP的实现所提供的服务都用1--1023之间的端口号。
>
>TCP/IP实现给临时端口号分配1024--5000之间的端口号，大于5000的端口被其他服务器使用

# 网络通信协议

通过计算机网络协议可以实现不同计算机之间的通信，但是在计算机网络中的通信必须要约定通信协议。对速率、传输代码、代码结构、传输控制步骤、出错控制等制定标准。就像两个人要顺利沟通，就必须使用相同的语言，假如一个只懂英语，另一个只懂中文，这样就会造成没有共同语言而无法沟通。

国际标准化组织（ISO）定义网络通信协议的基本框架，被称为OSI模型。OSI制定的七层标准模型，分别是：应用层、表示层、会话层、传输层、网络层、数据链路层、物理层。



虽然国际标准化组织制定了这样的一个网络协议的模型，但是实际上互联网使用最多的网络通信协议还是TCP/IP网络通信协议。

TCP/IP是一个协议族，也是按层次划分，共四层。应用层、传输层、互联网络层、网络接口层。

### TCP/IP协议与OSI模型的区别

OSI是网络通信模型，是一个参考模型，而TCP/IP协议是一个事实上的标准。TCP/IP协议是参考了OSI参考模型，但是却没有分成七层，只分了四层，这样会简单一点，当分太多层次时很难区分某个协议属于哪一层。TCP/IP协议与OSI参考模型并不冲突，TCP/IP协议中的应用层就相当于OSI参考模型中的应用层、表示层】、会话层。

### 网络协议的分层

由于网络节点非常复杂，在制定协议时把复杂的成分分解为一些简单的成分，再将它们复合起来，上一层可以调用下一层，在与下一层不发生关系。

# TCP/UDP

## 联系和区别

TCP协议和UDP协议是传输层的两种协议。Socket是传输层提供给应用层的编程接口，所以socket编程就分为TCP编程和UDP编程。

在网络通讯中，TCP方式就类似于拨打电话，使用该方式进行网络通讯时，需要建立专门的虚拟连接，然后进行可靠的数据传输，如果数据发送失败，则客户端会重发数据。而UDP就类似于发送短信，使用该方式进行网络通信时，不需要建立专门的连接，传输也不是很可靠，如果发送失败，则客户端无法获得。

这两种方式一般都在实际编程中使用，重要的数据一般使用TCP协议进行传输，而大量的非核心数据一般使用UDP方式进行传递，在一些程序中甚至结合使用这两种方式进行数据传递。

由于TCP需要建立专门的虚拟链接，以及确认传输是否正确，所以使用TCP方式的速度慢一些，而且传输时的数据量比UDP稍微大一些。

> 总结
>
> TCP是面向连接的，传输数据安全、稳定、效率相对较低的
>
> UDP是面向无连接的，传输数据不安全，效率较高

# UDP编程

TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议，使用UDP协议时不需要建立连接，只需要知道对方的IP号和端口号即可发送数据，能不能到达就不知道了。

下面，就是UDP实现发送数据的过程，以下编码过程都需要用到*网络调试助手*

```python
# 导入模块
from socket import *


# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 发送地址
ip_port = ('192.168.1.111', 8080)
# 键盘获取信息
data = input('请输入要发送的信息').encode('gb2312')
# 发送数据
udp_socket.sendto(data, ip_port)
# 关闭套接字
udp_socket.close()
```

每一次网络助手接收数据时，端口号都是随机分配的。如果网络助手要发送数据，那么就需要绑定端口，不然网络助手不知道发送到哪个端口上面。

```python
# 导入模块
from socket import *


# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 发送地址
ip_port = ('192.168.1.105', 8080)
# 绑定端口
udp_socket.bind(('', 8989)) # 绑定本地ip，端口是8989
# 键盘获取信息
data = input('请输入要发送的信息').encode('gb2312')
# 发送数据
udp_socket.sendto(data, ip_port)
# 接收数据
recv_data = udp_socket.recvfrom(1024) # 接收数据的最大字节数
# print(recv_data)
# (b'\xc4\xe3\xba\xc3\xa3\xac\xc7\xeb\xce\xca\xd3\xd0\xca\xb2\xc3\xb4\xce\xca\xcc\xe2', ('192.168.1.105', 8080))
print('接收到%s的信息是：%s' % (recv_data[1], recv_data[0].decode('gb2312')))
# 关闭套接字
udp_socket.close()
```

上面的程序只能做到收发一次的数据，这样的结果显然不是想要的，接下来可以开启多线程，无限接收和发送数据。

```python
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
```

#  TFTP文件下载器

## TFTP协议介绍

TFTP，是TCP/IP协议族中的一个用来在客户端与服务端之间进行文件传输的协议。

**特点**

> 简单，占用资源少
>
> 适合小文件传输
>
> 适合在局域网中传输
>
> 端口号为69
>
> 基于UDP实现



TFTP（简单的文件传输协议）使用这个协议，实现简单的文件下载，TFTP端口号69

下载：从服务器上将一个文件复制到本机。

下载过程：

在本地创建一个空文件（与要下载的文件名相同），向里面写数据，数据写完之后关闭链接。

当服务器找到需要现在的文件后，会立刻打开文件，把文件中的数据通过TFTP协议发送给客户端。如果文件总大小较大，那么服务器会分多次发送，每次从文件读取512个字节的数据发送过来。

那么什么时候认为数据已经发送完毕了呢？当客户端接收到的数据小于516（2个字节操作码+2个字节的序号+512字节数据）。

下面代码将实现简单的文件下载：

```python
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
```

# TCP编程

面向连接的socket使用的主要协议是传输控制协议，也就是常说的TCP,TCP的socket名称是SOCK_STREAM。

## 三次握手

第一步：客户端发送一个包含SYN即同步标志的TCP报文，SYN同步报文会指明客户端使用端口及TCP连接的初始序号

第二步：服务端接收到客户端的SYN报文之后，将返回一个SYN+ACK的报文，表示客户端的请求被接收，同时TCP序号加一，ACK确认

第三步：客户端也返回一个确认报文ACK给服务器，同样TCP序号被加一，此时TCP连接完成。然后才开始通信的第二步：数据处理。

这就是TCP的三次握手。

## 基于TCP编程的API概览

**listen**监听端口

**accept**等待客户端连接

**recv**接收客户端信息

## TCP服务端实现

根据上述所描述的基本信息，现在可以使用代码实现TCP服务端的编程

```python
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
```

# TCP:双向通信socket之服务端

双向通信，即读取客户端发送的数据，，将内容输出到控制台

将控制台输入的数据发送到客户端

**服务端**

```python
from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 8888))
server_socket.listen()
client_socket, client_info = server_socket.accept()
while True:
    recv_data = client_socket.recv(1024)
    print('客户端：', recv_data.decode('gb2312'))
    data = input('请输入你要发送的数据：')
    client_socket.send(data.encode('gb2312'))
```

**客户端**

```python
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
ip_port = ('192.168.2.212', 8888)
client_socket.connect(ip_port)
while True:
    msg = input('请输入你要发送的信息：').encode('gb2312')
    client_socket.send(msg)
    recv_data = client_socket.recv(1024)
    print('服务端：', recv_data.decode('gb2312'))

```

编写完上述代码之后打开两个终端，分别运行服务端与客户端，你就会发现这其实就是模拟QQ实现的结果。