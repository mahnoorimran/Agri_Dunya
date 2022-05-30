from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    cat= Category.objects.all()
    context={
        'cat':cat
    }
    return render(request, 'products/home.html',context)

def nuterients(request):
    category=Category.objects.all()
    categoryId = request.GET.get('category')
    if categoryId:
        products=Products.objects.filter(subcategory=categoryId)
    else:
        products=Products.objects.all()
    context={
        'Category':category,
        'products':products,
    }
    return render(request, 'products/nutrients.html',context)
def seeds(request):
    return render(request, 'products/seeds.html')
def forage_food(request):
    return render(request, 'products/forage-food.html')