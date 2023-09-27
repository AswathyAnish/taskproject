from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, "index.html")
#def formpage(request):
 #   return render(request, "formpage.html")


