from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Text(models.Model):
    txt = models.TextField()
    mark_total = models.IntegerField()


