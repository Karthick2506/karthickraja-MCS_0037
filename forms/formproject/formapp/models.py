from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.TextField(max_length=500)


class Student(models.Model):
    fname = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    rollno= models.CharField(max_length=50)
    address= models.TextField(max_length=500)

