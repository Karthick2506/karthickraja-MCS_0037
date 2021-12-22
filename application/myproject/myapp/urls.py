from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage),
    path('reg', regpage),
    path('register', addemp, name='ad'),
    path('reg/register/info', empinfo),
    path('reg/register/info/infoo', info, name='in'),
]