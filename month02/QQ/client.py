from socket import *
from multiprocessing import Process
import sys

SERVER_ADDR = ("176.17.12.168", 9896)


def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024 * 10)
        msg = "\n" + data.decode() + "\n"
        print(msg, end=" ")


def send_msg(sock, name):
    while True:
        try:
            content = input("发言:")
        except:
            content = "exit"
        if content == 'exit':
            msg = "EXIT" + name
            sock.sendto(msg.encode(), SERVER_ADDR)
            sys.exit("您已退出聊天")

        msg = "CHAT %s %s" % (name, content)
        sock.sendto(msg.encode(), SERVER_ADDR)


def do_chat(sock, name):
    p = Process(target=recv_msg, args=(sock,),daemon=True)
    p.start()
    send_msg(sock, name)


def do_login(sock):
    while True:
        name = input("请输入昵称:")
        msg = "LOGIN " + name
        sock.sendto(msg.encode(), SERVER_ADDR)
        result, addr = sock.recvfrom(128)
        if result == b'OK':
            print("您已进入聊天室")
            return name
        else:
            print("该昵称已存在")


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("176.17.12.168", 9897))

    name = do_login(sock)

    do_chat(sock, name)


if __name__ == '__main__':
    main()
