"""
tcp服务端 循环示例1
重点代码 ！！！
"""
from time import localtime
from socket import *


def recv_image(connfd):
    filename = "%s-%s-%s" % localtime()[:3] + ".jpg"
    file = open(filename, "wb")
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        file.write(data)
    file.close()
    connfd.close()


def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(("0.0.0.0", 8888))

    tcp_socket.listen(5)
    while True:
        connfd, addr = tcp_socket.accept()
        print("连接:", addr)
        recv_image(connfd)


if __name__ == '__main__':
    main()