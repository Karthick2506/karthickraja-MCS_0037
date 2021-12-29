from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeForm, StudentForm
def home(request):
    form = EmployeeForm
    if request.method == 'POST':
        empform = EmployeeForm(request.POST)
        if empform.is_valid():
            empform.save()
            messages.success(request, 'Employee Data has been submitted')
            return redirect('/')
    return render(request, 'home.html', {'form': form})

def student(request):
    form = StudentForm
    if request.method == 'POST':
        studentform = StudentForm(request.POST)
        if studentform.is_valid():
            studentform.save()
            messages.success(request, 'Student Data has been submitted')
            return redirect('/student')
    return render(request, 'student.html', {'form': form})



