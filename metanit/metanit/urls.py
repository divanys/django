
from django.urls import path, include
from hello.urls import *
from hello.views import pageNotFound
from django.contrib import admin

urlpatterns = [
    path('', include('hello.urls')),
    path('admin/', admin.site.urls)
]

handler404 = pageNotFound
