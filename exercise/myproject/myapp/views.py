from django.shortcuts import render

def load(request):
    return render(request, "myapp/index.html")

def load1(request,name):
    context = {'name':name}
    return render(request, "myapp/name.html", context)
def load2(request):
    names = ["Karthick", "Shiva", "Kumar", "Raja"]
    ids = [1, 2, 3, 4]
    context1 = {'names': names, 'ids': ids}
    return render(request, "myapp/detail.html", context1)

