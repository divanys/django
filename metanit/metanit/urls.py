
from django.urls import path, include
from hello.urls import *
from hello.views import pageNotFound

urlpatterns = [
    path('', include('hello.urls')),
]

handler404 = pageNotFound
