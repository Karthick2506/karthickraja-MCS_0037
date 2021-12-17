from django.shortcuts import render

from django.http import *

def operation(request):
    return render(request, "home.html")

#def sample(request):
    #return HttpResponse ("This is not my Place")

#def samplee(request):
    #res = "<h1>I am From Bangalore</h1>"
    #return HttpResponse (res)
