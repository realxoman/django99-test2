from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from .models import Products
from django.db.models import Q
from django.urls import reverse



# Create your views here.


def home(request):
    seller, created = Group.objects.get_or_create(name='seller')
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
    seller, created = Group.objects.get_or_create(name='seller')
    kazem = False
    if request.user.groups.filter(name = seller).exists():
        kazem = True
        print("++++++++++")
    else:
        kazem = False
        print("-------------")
    if request.method == 'POST':
        seller.user_set.add(request.user)
        return render(request, "blog/seller-done.html",{"kazem": kazem})
    return render(request, "blog/panel.html",{"kazem": kazem})
    


def addproduct(request):
    seller, created = Group.objects.get_or_create(name='seller')
    if request.method == 'POST':
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        product = Products(name=name,quantity=quantity,price=price,author=request.user)
        product.save()
        return render(request, "blog/product-success.html")
    return render(request, "blog/addproduct.html")


    
def productslistuser(request):
    user_products = Products.objects.filter(author=request.user)
    if request.method == "POST":
        query = request.POST.get("title")
        search_lists = Products.objects.filter(Q(name__icontains=query),author=request.user)
        return render(request, "blog/products.html", {"search_lists": search_lists })
    return render(request, "blog/userproducts.html",{"user_products":user_products})

def productslist(request):
    productslist = Products.objects.all()
    if request.method == "POST":
        query = request.POST.get("title")
        search_list = Products.objects.filter(Q(name__icontains=query))
        return render(request, "blog/search.html", {"search_list": search_list })
    return render(request, "blog/products.html",{"productslist":productslist})

from django.shortcuts import render , get_object_or_404
from .forms import productform

def editproduct(request , id=None):
    post = get_object_or_404(Products, id=id)

    editform = productform(request.POST or None , request.FILES or None, instance=post)
    if editform.is_valid():
        editform.save()
        return HttpResponseRedirect(reverse('blog:productslistuser'))
    context = {
        'form': editform,
    }
    return render(request, 'blog/editproduct.html',context)

def deleteproduct(request , id=None):
    post = get_object_or_404(Products, id=id)
    if post.delete():
        return HttpResponseRedirect(reverse('blog:productslistuser'))