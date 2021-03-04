from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.name
