from socket import *

class FTPhandle:
    server_address = ("127.0.0.1",8888)
    def __init__(self):
        self.sock = self.connect_server()

    def connect_server(self):
        sock = socket()
        sock.connect(FTPhandle.server_address)
        return sock

class FTPView:
    def __init__(self,ftp):
        self.__ftp = FTPhandle()

    def __display_menu(self):
        print("1) 查看文件")
        print("2) 下载文件")
        print("3) 上传文件")
        print("4) 退出")
        print(" ")

    def __select_meau(self):
        item = input("请输入选项:")
        if item == '1':
            self.__ftp = FTPhandle()
        elif item == '2':
            pass
        elif item == '3':
            pass
        elif item == '4':
            pass
        else:
            print("请输入正确选项")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_meau()

if __name__ == '__main__':
    ftpview = FTPView()
    ftpview.main()
