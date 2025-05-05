from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_description = models.TextField(max_length=500)
    recipe_ingre = models.CharField(max_length=500)

    def __str__(self):
        return self.receipe_name
