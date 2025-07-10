from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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

@login_required
def add_to_cart(request, fruit_id):
    if request.method == 'POST':
        fruit = get_object_or_404(Fruit, id=fruit_id)
        quantity = float(request.POST.get('quantity', 1))
        
        # Check if item already exists in cart
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            fruit=fruit,
            defaults={'quantity': quantity}
        )
        
        if not created:
            # If item exists, update quantity
            cart_item.quantity += quantity
            cart_item.save()
            messages.success(request, f'Updated {fruit.name} quantity in cart!')
        else:
            messages.success(request, f'Added {fruit.name} to cart!')
        
        return redirect('index')
    
    # If GET request, show quantity selection form
    fruit = get_object_or_404(Fruit, id=fruit_id)
    return render(request, 'add_to_cart.html', {'fruit': fruit})

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    # Calculate total
    total = sum(item.get_total_price() for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'cart.html', context)

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    fruit_name = cart_item.fruit.name
    cart_item.delete()
    messages.success(request, f'Removed {fruit_name} from cart!')
    return redirect('view_cart')

@login_required
def update_cart_quantity(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        quantity = float(request.POST.get('quantity', 1))
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, f'Updated {cart_item.fruit.name} quantity!')
        else:
            cart_item.delete()
            messages.success(request, f'Removed {cart_item.fruit.name} from cart!')
    
    return redirect('view_cart')

