from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from .models import Products,UserProducts


# Create your views here.

seller, created = Group.objects.get_or_create(name='seller')

def home(request):
    return render(request,"blog/home.html")

def registers(request):
    error_pass = False
    error_user = False
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        password_repeat = request.POST.get("password2")
        if password != password_repeat :
            error_pass = True
            return render(request, "blog/register.html", {"error_pass": error_pass})

        if User.objects.filter(username=username).exists() :
            error_user = True
            return render(request, "blog/register.html", {"error_user": error_user})

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password)
        user.save()

        return HttpResponseRedirect("/")
    return render(request, "blog/register.html")

def login_(request):
    error = False
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        elif user is None:
            error = True
    return render(request, "blog/login.html", {
        "error": error
    })

def logout_(request):
    logout(request)
    return HttpResponseRedirect("/")

def contact(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        text = request.POST.get("text")
        email = request.POST.get("email")
        send_mail(
                title,
                f"{text}  {email}",
                'ssckiau.es@gmail.com',
                ["webe21lopers@gmail.com"],
            )
        return render(request, "blog/contact-success.html")
    return render(request, "blog/contact.html")


def panel(request):
    kazem = False
    if request.user.groups.filter(name = seller).exists():
        kazem = True
    else:
        kazem = False
    if request.method == 'POST':
        seller.user_set.add(request.user)
        return render(request, "blog/seller-done.html",{
        "kazem": kazem
    })
    return render(request, "blog/panel.html",{
        "kazem": kazem
    })
    


def addproduct(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        product = Products(name=name,quantity=quantity,price=price,author=request.user)
        product.save()
        return render(request, "blog/product-success.html")
    return render(request, "blog/addproduct.html")


    
def productslistuser(request):
    user_products = [c.products for c in UserProducts.objects.all()]
    productslists = Products.objects.all()
    return render(request, "blog/userproducts.html",{"user_products":user_products,"productslists":productslists})

def productslist(request):
    productslist = Products.objects.all()
    return render(request, "blog/products.html",{"productslist":productslist})
