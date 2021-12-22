from django.shortcuts import render
from .models import *

def homepage(request):

    return render (request, "myapp/home.html")


def regpage(request):
    return render (request, "myapp/register.html")

def addemp(request):
    if request.method == "POST":
        n = request.POST['en']
        i = request.POST['eid']
        m = request.POST['em']
        num = request.POST['enum']
        l = request.POST['el']
        reg = Add(ename=n, eid=i, email=m, phno=num, Location=l)
        reg.save()  #saving data in the database
        result = "Your Details are Saved"
        return render(request, 'myapp/register.html', {'res':result})
    else:
        result = "Your Details are not Saved"
        return render(request, 'myapp/register.html', {'res': result})

def empinfo(request):
    return render(request, "myapp/info.html")

def info(request):
    if request.POST['en']:
        out = Add.objects.all()
    return render(request, "myapp/info1.html", {'r':out})