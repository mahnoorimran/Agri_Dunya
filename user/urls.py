from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name="logout"),
    path('register',views.registerUser,name='register')
]