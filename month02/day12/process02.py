from multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working")

p = Process(target=worker,
            name="test",
            daemon=True,
            args=(2,),
            kwargs={"name":"V"})

p.start()
print(p.name)
print(p.pid)
print(p.is_alive())
