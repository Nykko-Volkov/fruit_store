from django.contrib import admin

# Register your models here.
from .models import Fruit, FruitDetail, CartItem

admin.site.register(Fruit)
admin.site.register(FruitDetail)
admin.site.register(CartItem)
