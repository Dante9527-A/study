import time


def timer():
    file = open("my.log", "a+",buffering=1)
    file.seek(0, 0)
    count = len(file.readlines()) + 1
    while True:
        file.write(str(count) + "." + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")
        count += 1
        # file.flush()
        time.sleep(2)


timer()
