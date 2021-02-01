import multiprocessing
from time import sleep
import os

a = 1

def func01():
    print("开始任务1")
    global a
    print("a=",a)
    sleep(2)
    a = 10000
    print(os.getpid())
    print(os.getppid())
    print("任务结束1")


p = multiprocessing.Process(target=func01)

p.start()

print("start")
sleep(2)
print("success")


p.join()
print(a)