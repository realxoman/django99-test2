from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import registerform 

# Create your views here.


def home(request):
    return render(request,"blog/home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = registerform()
    return render(request, "blog/register.html", {"form":form})