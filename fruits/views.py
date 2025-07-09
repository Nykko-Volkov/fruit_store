from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Fruit, FruitDetail, CartItem



def index(request):
    data = Fruit.objects.all()
    context = {
        'fruits': data
    }
    logged_in_user = request.user
    if logged_in_user.is_authenticated:
        context['logged_in_user'] = logged_in_user
    else:
        context['logged_in_user'] = None
    return  render(request, "index.html", context)


def signup(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pw = request.POST.get('password')
        user  = User.objects.create_user(username=un,password=pw)
        user.save()
        login(request,user)

        return redirect('index')
    return render(request, 'signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')# html 
        password = request.POST.get('password')
        
        user = authenticate(request, username=username,password=password)
        if user is not None:
            # remove already logged in
            print('~it came inside')
            logout(request)
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,'~invalid username or password')
    return render(request, 'login_page.html')



def logout_view(request):
    logout(request)
    return redirect('index')

