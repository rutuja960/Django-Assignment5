from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('loginpage/', views.loginpage,name="loginpage"),
    path('check', views.getdata,name="getdata"),
]