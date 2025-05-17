# myapp/views.py

from django.http import JsonResponse
from .tasks import sleepy_task

def run_task(request):
    sleepy_task.delay(10)  # runs in background
    return JsonResponse({"message": "Task started!"})
