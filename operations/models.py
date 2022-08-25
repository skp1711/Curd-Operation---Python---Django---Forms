from turtle import title
from django.db import models

# Create your models here.


class Curd(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    city = models.CharField(max_length=70, blank=False, default='')
    published = models.BooleanField(default=False)