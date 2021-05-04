from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=70, default='')
    email = models.EmailField(max_length=70, default='')
    password = models.CharField(max_length=20, default='')