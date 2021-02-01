import os

dir = "/home/tarena/FTP"
res = 0

q1 = os.path.getsize("/home/tarena/FTP/exercise01.py")
q2 = os.path.getsize("/home/tarena/FTP/pool.py")
q3 = q1+q2
print(q3)

