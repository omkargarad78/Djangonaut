# myapp/tasks.py

from celery import shared_task
import time

@shared_task
def sleepy_task(duration):
    time.sleep(duration)
    return f"Task completed after {duration} seconds"
