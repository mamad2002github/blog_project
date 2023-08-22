from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_in(request):
        if request.user.is_authenticated == True:
          return redirect('home_app:main')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        #
        if user is not None:
            login(request, user)
            return redirect('home_app:main')
        return render(request, 'Account/login.html', {})

def user_logout(request):
    logout(request)
    return redirect('home_app:main')

def user_register(request):
    if request.user.is_authenticated == True:
        return redirect ('home_app:main')
    contex = {'errors':[]}
    if request.method=='POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')



        user = User.objects.create_user(username=username,password=password1,email=email)
        login(request,user)
        return redirect('/')
    return render(request,'Account/register.html',{})
