from django.db import models

from django.utils import timezone

class todo(models.Model):
    title=models.CharField(("Enter your title"), max_length=50)
    details=models.TextField()
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title