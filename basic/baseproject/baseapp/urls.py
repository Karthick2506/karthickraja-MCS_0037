from django.urls import path
from .views import *

urlpatterns = [
    path('view/<str:sample>', test.as_view()),
]