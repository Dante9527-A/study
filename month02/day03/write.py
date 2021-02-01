"""
文件写方法 示例
"""
#打开一个文件
# file = open("file.txt","ab")
file = open("file.txt","w")
#写入内容
# file.write("hello world\n".encode())
# n = file.write("你好\n".encode())
# print("写入%d字节"%n)
#将列表写入文件
data = [
        "先帝创业未半\n",
        "而中道崩殂\n"
        ]
file.writelines(data)

#关闭
file.close()