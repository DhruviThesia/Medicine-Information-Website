from django.shortcuts import render, redirect
from .models import Emp

# Create your views here.

def insert(request):
    if request.POST:
        u= request.POST['uname']
        e=request.POST['email']
        p=request.POST['password']
        obj = Emp(uname=u,email=e,password=p)
        obj.save()
        return redirect('/login')
    return render(request,"insert.html")

def login(request):
    if request.POST:
        e=request.POST['email']
        p=request.POST['password']
        count= Emp.objects.filter(email=e,password=p).count()
        if count>0:
            return redirect('/home')
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")
