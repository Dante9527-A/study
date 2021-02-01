from multiprocessing import Process
from socket import *

HOST = '0.0.0.0'
PORT = 9890
ADDR = (HOST,PORT)

user = {}

def do_login(sock,name,address):
    if name in user or "管理" in name:
        sock.sendto(b"FAIL",address)
    else:
        sock.sendto(b"OK", address)

        msg = "欢迎 %s 进入聊天室" % name
        for key,value in user.items():
            sock.sendto(msg.encode(),value)
        user[name] = address

def do_chat(sock,name,content):
    msg = "%s : %s" % (name, content)
    for key,value in user.items():
        if key != name:
            sock.sendto(msg.encode(),value)

def do_exit(sock,name):
    del user[name]
    msg = "%s 退出了聊天" % name
    for key,value in user.items():
        sock.sendto(msg.encode(),value)

def handle(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        tmp = data.decode().split(' ', 2)
        if tmp[0] == "LOGIN":
            do_login(sock, tmp[1], addr)
        elif tmp[0] == "CHAT":
            do_chat(sock, tmp[1], tmp[2])
        elif tmp[0] == "EXIT":
            do_exit(sock, tmp[1])

def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)

    p = Process(target=handle, args=(sock,),daemon=True)
    p.start()

    while True:
        content = input("管理员消息：")
        if content == "exit":
            break
        msg = "CHAT 管理员消息 "+content
        #　发送给子进程
        sock.sendto(msg.encode(),ADDR)

if __name__ == '__main__':
    main()

