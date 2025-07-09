from django.db import models
from django.contrib.auth.models import User

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='fruits/')
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} @ {self.price_per_kg}/kg"

class FruitDetail(models.Model):
    fruit = models.OneToOneField(Fruit, on_delete=models.CASCADE, related_name='detail')
    description = models.TextField()

    def __str__(self):
        return f"{self.fruit.name} - {self.description[:50]}..."

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.fruit.name} - {self.quantity} pcs for {self.user.username}"