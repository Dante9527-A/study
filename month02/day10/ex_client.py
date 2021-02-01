"""
udp 客户端示例
重点代码  ！！！
"""
from socket import *

# 记录服务端地址
ADDR = ("176.17.12.168", 9527)


# 与服务端相同套接字

udp_socket = socket(AF_INET, SOCK_DGRAM)



while True:
    # 将输入的内容发送给服务端
    msg = input(">>")
    if not msg:
        break
    udp_socket.sendto(msg.encode(), ADDR)
    if msg == "##":
        break
    data, addr = udp_socket.recvfrom(1024)
    print("From server:", data.decode())

udp_socket.close()
