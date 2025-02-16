from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    # image = models.ImageField(upload_to='uploads/')
