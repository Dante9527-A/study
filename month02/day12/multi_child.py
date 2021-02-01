from multiprocessing import Process
from time import sleep
import os,sys

def th1():
    sleep(1)
    print("吃饭")
    print(os.getppid(),'--',os.getpid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(), '--', os.getpid())

def th3():
    sleep(3)
    print("打豆豆")
    sys.exit("打不过")
    print(os.getppid(), '--', os.getpid())

jobs = []
for th in [th1,th2,th3]:
    p = Process(target=th)
    jobs.append(p)
    p.start()

[i.join() for i in jobs]