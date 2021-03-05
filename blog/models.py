from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.


class Products(models.Model):
    author = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.name

class UserProducts(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)