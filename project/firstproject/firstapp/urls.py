from django.urls import path
from .views import *

urlpatterns = [
    path('', first),
    path('data', operation, name="lf"),
]