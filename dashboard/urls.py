from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^', index, name = 'dashboard')
]
