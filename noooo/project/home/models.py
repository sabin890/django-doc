from django.db import models
from django.forms import CharField

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
