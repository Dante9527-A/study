from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, song, times=0, sec=0):
        self.song = song
        self.times = times
        self.sec = sec
        super().__init__()

    def run(self):
        for i in range(3):
            sleep(5)
            print(f"播放：{self.song}")


t = MyThread("凉凉",2,3)

t.start()

t.join()
