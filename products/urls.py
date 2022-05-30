from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('home/',views.home, name='home' ),
    path('nuterients/',views.nuterients,name='nuterients'),
    path('seeds/',views.seeds,name='seeds'),
    path('forage_food/',views.forage_food,name='forage_food'),
    
]