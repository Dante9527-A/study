from socket import *
from threading import Thread

class Handle:
    def request(self,data):
        if data == "查看":
            pass
        elif data == "下载":
            pass
        elif data == "存放":
            pass
        elif data == "退出":
            pass

class ClientThread(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        self.handle = Handle(connfd)
        super().__init__(daemon=True)

class Baiduyun:
    def __init__(self,host = "",port = 0):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.sock = self.create_socket()

    def create_socket(self):
        udp_socket = socket(AF_INET,SOCK_DGRAM)
        udp_socket.bind(self.address)
        return udp_socket

    def server_forever(self):
        print("Listen the port %d"%self.port)
        self.sock.listen(5)
        while True:
            connfd,addr = self.sock.accept()
            print("Connect from",addr)

            thread = ClientThread(connfd)
            thread.start()

if __name__ == '__main__':
    server = Baiduyun(host="0.0.0.0", port=8888)
    server.serve_forever()