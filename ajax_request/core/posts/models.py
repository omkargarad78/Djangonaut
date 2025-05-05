from django.db import models

class Post(models.Model):
    post_heading=models.CharField(max_length=500)
    post_text=models.TextField()

    def __str__(self):
        return self.post_heading
    

class Likes(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)