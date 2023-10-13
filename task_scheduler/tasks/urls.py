from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('task/<str:pk>', views.delete, name='delete'),
    path('about/', views.about, name='about'),
]
