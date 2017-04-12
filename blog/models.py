from django.db import models
from django.contrib.auth.models import User
from .forms import UploadFileForm


# Create your models here.
class Text(models.Model):
    txt = models.TextField()
    mark_total = models.FloatField()

    def save_txt(self, f):
        file = open(f,'r')
        self.txt = file.read()


