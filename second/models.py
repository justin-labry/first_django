from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField(max_length=3000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # num stars = models.IntegerField()
