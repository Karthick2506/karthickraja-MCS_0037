from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=500)

class Message(models.Model):
    value = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=500)
    room = models.CharField(max_length=500)
