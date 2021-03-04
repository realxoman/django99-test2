from django.urls import path
from .views import home,register,login_,logout_
app_name = "Kazem"
urlpatterns = [
    path('',home,name="home"),
    path('register/', register, name='register'),
    path('login/', login_, name='login'),
    path('logout/', logout_),
]
