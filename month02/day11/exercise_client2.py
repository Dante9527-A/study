"""
tcp客户端 循环示例2
重点代码 ！！！
"""
from socket import *

#　服务器地址
ADDR = ("127.0.0.1",8883)

def chat(msg):
    # 重新创建套接字才能连接
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    tcp_socket.close()
    return data.decode()


def main():
    while True:
        msg = input("我：")
        #  输入空退出
        if not msg:
            break
        msg = chat(msg)

        print("sire:",msg)

if __name__ == '__main__':
    main()
