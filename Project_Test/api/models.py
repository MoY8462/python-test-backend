from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    type_res = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    telephone= models.CharField(max_length=10)

class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)