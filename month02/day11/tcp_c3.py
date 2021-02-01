from socket import *

#　服务器地址
ADDR = ("127.0.0.1",8886)

#　先发送再接收

while True:
    msg = input(">>")
    #  输入空退出
    if not msg:
        break
    # 重新创建套接字才能连接
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("From server:",data.decode())
    tcp_socket.close()