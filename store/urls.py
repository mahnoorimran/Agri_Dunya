from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name="home"),
       
    path('addproduct/', views.addproduct, name="addproduct"),
    path('categories/', views.all_categories, name="all-categories"),
    path('<slug:slug>/', views.category_products, name="category-products"),



    

]