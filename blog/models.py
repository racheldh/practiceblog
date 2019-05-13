from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(default="text")
    def __str__(self):
        return self.name