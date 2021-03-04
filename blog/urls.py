from django.urls import path
from .views import home,register,login_,logout_,contact,panel
app_name = "Kazem"
urlpatterns = [
    path('',home,name="home"),
    path('register/', register, name='register'),
    path('login/', login_, name='login'),
    path('logout/', logout_),
    path("contact/", contact, name="contact"),
    path("panel/", panel, name="panel"),
]
