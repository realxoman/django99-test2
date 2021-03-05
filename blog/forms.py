from django import forms
from .models import Products
from django.forms import ModelForm
from . import models

class productform(ModelForm):
    class Meta:
        model = models.Products
        fields = ('name','quantity','price')