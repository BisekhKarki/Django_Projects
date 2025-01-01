from home.views import index,people,login

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('index/', index),
    path('person/', people),
    path('login/', login),
]
