from django.urls import path
from .views import home,register
app_name = "Kazem"
urlpatterns = [
    path('',home,name="home"),
    path('register/', register, name='register'),
]
