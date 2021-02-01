from socket import *

# 创建tcp套接字 默认就是tcp
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8887))

# 设置监听
tcp_socket.listen(5)
dict = {
    "多大":"只有两天大",
    "年龄":"只有两天大",
    "几岁":"只有两天大",
}
# 循环连接客户端
while True:
    connfd,addr = tcp_socket.accept()
    # 收发一次消息
    data = connfd.recv(1024).decode()
    print("从",addr,"收到:",data)
    for item in dict:
        if item in dict:
            connfd.send(dict[data].encode())
    connfd.send("小爱听不懂你在说什么".encode())

    connfd.close()

# 关闭套接字
    tcp_socket.close()