from multiprocessing import Process
import os

size = os.path.getsize("dict.txt")
filename = "dict.txt"

def top():
    fr = open(filename, 'rb')
    fw = open("dict1.txt", 'wb')

    n = size // 2
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()


def bot():
    fr = open(filename, 'rb')
    fw = open("dict2.txt", 'wb')
    fr.seek(size//2)

    n = size // 2
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()

p = Process(target=top)
p.start()
bot()
p.join()