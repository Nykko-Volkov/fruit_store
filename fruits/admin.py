from django.contrib import admin

# Register your models here.
from .models import Fruit, Fruit_details, Cart, User

admin.site.register(Fruit)
admin.site.register(Fruit_details)
admin.site.register(Cart)
admin.site.register(User)
