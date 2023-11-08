from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Catagory(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    des=models.TextField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
