from django.shortcuts import render
from .models import Register

def display(request):
    return render(request, 'exapp/home.html')

def getdata(request):
    if request.method == "POST":
        n = request.POST['na']
        a = request.POST['ag']
        p = request.POST['ph']
        reg = Register(name=n, age=a,phno=p)
        reg.save()  #saving data in the database
        result = "Your Details are Saved"
        return render(request, 'exapp/home.html', {'out':result})
    else:
        result = "Your Details are not Saved"
        return render(request, 'exapp/home.html', {'out': result})