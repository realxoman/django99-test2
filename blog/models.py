from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.


class Products(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.name