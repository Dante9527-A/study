import time

def timer():
    file = open("my.log", "a+")
    count = 0
    file.seek(0)
    for line in file:
        count += 1
    while True:
        count+=1
        file.write(str(count) + "." + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")
        file.flush()
        time.sleep(2)

timer()
