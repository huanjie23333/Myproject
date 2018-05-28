from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=20)
    writer = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    number = models.IntegerField(max_length=100)

class Writer(models.Model):
    name = models.CharField(max_length=20)
