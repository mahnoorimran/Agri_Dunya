from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def loginUser(request):
   

    if request.user.is_authenticated:
        return redirect('store:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'Username dosenot exit')
            
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('store:home')
        else:
            messages.error(request,'username or password is incorrect')



    return render(request,'user/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page='register'
    form=UserCreationForm()
    context={
        'page':page,
        'form':form
    }
    return render(request,'user/login_register.html',context)

