from django.db import models
from django.forms import CharField, IntegerField
# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.CharField(max_length=70)
    stupass=models.CharField(max_length=20)

    def __str__(self):
        return self.stuname


    