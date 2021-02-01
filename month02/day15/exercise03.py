from socket import *
from threading import Thread
import sys

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
    connfd.close()

def main():
    tcp_socket = socket()
    tcp_socket.bind(ADDR)
    tcp_socket.listen(5)

    while True:
        try:
            connfd,addr = tcp_socket.accept()
            print("Connect from",addr)
        except:
            tcp_socket.close()
            sys.exit("服务结束")

        t = Thread(target=handle,args=(connfd,),daemon=True)
        t.start()

if __name__ == '__main__':
    main()