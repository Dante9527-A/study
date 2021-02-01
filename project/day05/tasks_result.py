from celery import Celery
import time

# 1 创建Celery对象
app = Celery('power',
             broker='redis://@127.0.0.1:6379/1',
             backend='redis://@127.0.0.1:6379/2',)

# 2 创建任务函数
@app.task
def task_test(a,b):
    print('task is runing...')
    time.sleep(5)
    return a + b
