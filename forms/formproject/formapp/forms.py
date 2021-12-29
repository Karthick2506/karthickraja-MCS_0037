from django.forms import ModelForm
from .models import Employee,Student
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'address')

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'