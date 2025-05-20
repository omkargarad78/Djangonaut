from django.db import models

class Notification(models.Model):
    user_email = models.EmailField()
    message = models.TextField()
    notification_type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.user_email} | {self.message[:20]}..."