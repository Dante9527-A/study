from socket import *

ADDR = ("176.17.12.168",8888)

def send_image(tcp_socket,filename):
    file = open(filename,'rb')
    while True:
        data = file.read(1024)
        if not data:
            break
        tcp_socket.send(data)
    file.close()
def main():
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    send_image(tcp_socket)
    tcp_socket.close()

if __name__ == '__main__':
        main('a.jpg')
