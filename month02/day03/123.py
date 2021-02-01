import os

print("文件大小:",os.path.getsize("linus.png"))

print("文件列表:",os.listdir(".."))

print("是否存在:",os.path.exists("seek.py"))

print("文件类型:",os.path.isfile("."))

os.remove("linus_cp.png")