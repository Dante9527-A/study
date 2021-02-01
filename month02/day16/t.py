import sys

def myinput(info = " "):
    print(info,end="\n")
    data = sys.stdin.readline()
    return data.strip("\n")
