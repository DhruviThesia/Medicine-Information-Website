from django.shortcuts import render, redirect
from .models import Emp, Blog, Comment

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
    data=Blog.objects.all
    return render(request,"home.html",{"data":data})

def about(request):
    return render(request,"about.html")

def createPost(request):
    if request.POST:
        title=request.POST['title']
        desc=request.POST['desc']
        postby=request.POST['postby']
        image=request.FILES['image']
        obj = Blog(title=title,desc=desc,postby=postby,image=image)
        obj.save()
        return redirect('/home')
    return render(request,"createPost.html")

def service(request):
    return render(request,"service.html")

def company(request):
    return render(request,"company.html")

def readMore(request, id):
    data=Blog.objects.get(id=id)
    if request.POST:
        msg= request.POST['msg']
        obj= Comment(msg=msg)
        obj.pid_id=id
        obj.save()
    c=Comment.objects.filter(pid=id)
    return render(request,"readMore.html",{"data":data,"c":c})


