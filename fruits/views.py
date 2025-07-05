from django.shortcuts import render, redirect, get_object_or_404


from .models import Fruit

def index(request):
    data = Fruit.objects.all()
    context = {
        'fruits': data
    }
    return  render(request, "index.html", context)