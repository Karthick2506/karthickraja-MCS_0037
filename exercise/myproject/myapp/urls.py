from django.urls import path
from .views import *

urlpatterns = [
    path('', load),
    path('next/<str:name>', load1),
    path('load2/', load2),
]