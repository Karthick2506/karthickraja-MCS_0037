from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Add(models.Model):
    ename = models.CharField(max_length=50)
    eid = models.IntegerField()
    email = models.EmailField(max_length=254)
    phno = PhoneNumberField()
    Location = models.CharField(max_length=50)
