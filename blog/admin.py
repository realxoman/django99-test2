from django.contrib import admin
from .models import Products,UserProducts
# Register your models here.

admin.site.register(Products)
admin.site.register(UserProducts)