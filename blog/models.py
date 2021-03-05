from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User



# Create your models here.


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.name
