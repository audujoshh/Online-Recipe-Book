from django.db import models

# Create your models here.

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    category = models.TextField()
    no_of_likes = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='recipe_uploads/', null=True, blank=True)
    # image = models.ImageField(upload_to='recipe_uploads/', default='Screenshot_9.png')

    def __str__(self):
        return self.name[:50]
