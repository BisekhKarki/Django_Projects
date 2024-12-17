from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def login_user(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request,username=name,password=password)
        if user is None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid username or password")
    return render(request,'login.html') 


def Signup_user(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Password and confirm password do not match")
        else:
            user_details = User.objects.create_user(name,email, pass1)
            user_details.save()
            return redirect('login')
    return render(request,'Signup.html')


@login_required(login_url='login')
def home(request):
    return render(request,'Home.html')


def logout_user(request):
    logout(request)
    return render(request,'login.html')




