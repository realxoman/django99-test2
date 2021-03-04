from django.urls import path
from .views import home,registers,login_,logout_,contact,panel,addproduct,productslist,productslistuser
app_name = "Kazem"
urlpatterns = [
    path('',home,name="home"),
    path('register/', registers, name='register'),
    path('login/', login_, name='login'),
    path('logout/', logout_),
    path("contact/", contact, name="contact"),
    path("panel/", panel, name="panel"),
    path("addproduct/", addproduct, name="addproduct"),
    path("products/", productslist, name="productslist"),
    path("myproducts/", productslistuser, name="productslistuser"),
]
