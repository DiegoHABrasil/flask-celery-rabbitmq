from celery import Celery
import time

app = Celery('tasks', broker='pyamqp://admin:admin@rabbit:5672//')

@app.task
def add(x, y):
    time.sleep(20)
    return x + y