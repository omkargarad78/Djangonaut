from django.db import models

class Users(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title=models.CharField(max_length=200)
    is_completed=models.BooleanField(default=False)
    user=models.ForeignKey(Users, related_name="tasks", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
