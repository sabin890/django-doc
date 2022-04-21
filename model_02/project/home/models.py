from django.db import models
from django.forms import IntegerField,CharField

# Create your models here.
class Student(models.Model):
    student_id=models.IntegerField()
    student_name=models.CharField(max_length=40)
    student_email=models.CharField(max_length=40)
    student_password=models.CharField(max_length=40)
    def __str__(self):
        return self.student_name