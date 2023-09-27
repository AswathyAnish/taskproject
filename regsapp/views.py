from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['password']
        user = auth.authenticate(username=username, password=psw)
        if user is not None:
            auth.login(request, user)
            return redirect('newpage')
            #return render(request,"newpage.html")
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect('login')
    return render(request, "login.html")


# Create your views here.
def register(request):
    if request.method == 'POST':
        usname = request.POST['username']
        fsname = request.POST['fname']
        lsname = request.POST['lname']
        emailid = request.POST['email']
        psw1 = request.POST['psw1']
        psw2 = request.POST['psw2']
        if psw1 == psw2:
            if User.objects.filter(username=usname).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=emailid).exists():
                messages.info(request, "Email id already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=usname, password=psw1, first_name=fsname, last_name=lsname,
                                                email=emailid)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password not match")
            return redirect('register')

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def newpage(request):
    return render(request, "newpage.html",{})
    #return redirect('formpage')
def formpage(request):
    #return redirect('formpage')
    if request.method == 'POST':
        messages.info(request, "Order confirmed")
        return redirect('formpage')

    return render(request, "formpage.html",{})
