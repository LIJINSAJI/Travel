from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        Username = request.POST['username']
        Password = request.POST['password']
        User=auth.authenticate(username=Username,password=Password)
        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            messages.info(request,"invalid Credentials")
            return redirect(request,'login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        Username = request.POST['username']
        FirstName = request.POST['first_name']
        LastName= request.POST['last_name']
        Email = request.POST['email']
        Password = request.POST['password']
        ConfirmPassword = request.POST['confirm_password']
        if Password==ConfirmPassword:
            if User.objects.filter(username=Username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=Username,password=Password,first_name=FirstName,last_name=LastName,email=Email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')