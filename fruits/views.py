from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import Fruit, Fruit_details, Cart, User

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Here you would typically save the user to the database
        # For simplicity, we are just redirecting to the index page
        return redirect('index')
    return render(request, 'signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')# html 
        password = request.POST.get('password')
        users = User.objects.filter(username=username, password=password).first()
        if users.exists():
            # remove already logged in
            logout(request)
            login(request, users)
            return redirect('index')
    return render(request, 'login_page.html')