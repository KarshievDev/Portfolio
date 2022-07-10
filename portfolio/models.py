import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    # img = models.ImageField()
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=2000)
    button = models.TextField(max_length=30)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)