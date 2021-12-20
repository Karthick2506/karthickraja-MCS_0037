from django.urls import path
from .views import *

urlpatterns = [
    path('', display),
    path('data', getdata, name='gt'),
]