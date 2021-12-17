from django.shortcuts import render
from django.http import *

def first(request):
    return render(request, "firstapp/home.html")

def operation(request):
    if request.method=="GET":
        username = request.GET['un']
        password = request.GET['up']
        if(username=="karthick" and password=="1234"):
            result = "Login Success"
            return render(request, "firstapp/home.html", {'res':result})
        else:
            result = "Invalid Username and Password"
            return render(request, "firstapp/home.html", {'res': result})