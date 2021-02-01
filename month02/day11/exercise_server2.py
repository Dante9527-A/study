from socket import *

chat = {
    "你好":"Hello",
    "多大了":"两天大",
    "性别":"None",
    "你是谁":"sire"
}
def response(connfd):
    q = connfd.recv(1024).decode()
    for key in chat:
        if key in q:
            connfd.send(chat[key].encode())
            break
    else:
        connfd.send("我不懂你在说什么".encode())
    connfd.close()

def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(("0.0.0.0", 8883))
    tcp_socket.listen(5)
    while True:
        connfd,addr = tcp_socket.accept()
        response(connfd)

if __name__ == '__main__':
    main()