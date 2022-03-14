from platform import release
from django.db import models

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField()
    title = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)