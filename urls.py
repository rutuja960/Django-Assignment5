
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include("home.urls")),
    path('userlogin/', include("userlogin.urls")),
    path('registration/', include("registration.urls")),

   
]
