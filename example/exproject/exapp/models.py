from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Register(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    phno = PhoneNumberField()
