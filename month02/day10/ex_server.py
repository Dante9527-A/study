"""
udp套接字服务端模型
重点代码！！！
"""
from socket import *
import pymysql

args = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"dict",
    "charset":"utf8"
}

db = pymysql.connect(**args)

cur = db.cursor()

# 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0", 9527))
while True:
    # 接收 发送消息 data-->bytes
    data, addr = udp_socket.recvfrom(1024)

    sql = f"select mean from words where word = %s;"
    cur.execute(sql,[data.decode()])
    one = cur.fetchone()[0]

    n = udp_socket.sendto(b"单词解释",one.encode(), addr)


# 关闭套接字
udp_socket.close()