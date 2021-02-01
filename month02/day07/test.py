import time
tm = time.localtime()
print(tm[:6])

def func01(p1,p2,p3):
    print(p1)
    print(p2)
    print(p3)

dict01 = {"p2":20,"p3":30,"p1":10}
func01(**dict01)

def func02(**kwargs):
    print(kwargs)

func02(p1=1,p2=2)