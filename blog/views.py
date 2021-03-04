from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import EmailMessage
from django.db.models import Q


# Create your views here.


def home(request):
    return render(request,"blog/home.html")

def register(request):
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
        my_email = EmailMessage(
                title,
                f"{text}  {email}",
                'VcoChand' + '<ssckiau.es@gmail.com>',
                ["fromiran98@gmail.com"],
            )
        my_email.send()
        return render(request, "blog/contact-success.html")
    return render(request, "blog/contact.html")