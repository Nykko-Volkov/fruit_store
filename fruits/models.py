from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='fruits/')
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}  @ {self.price_per_kg}/kg"
    
class Fruit_details(models.Model):
    name = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    price_per_kg = models.ForeignKey(Fruit, on_delete=models.CASCADE, related_name='price_details')
    description = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.description[:50]}..."  # Display first 50 characters of description
    

class Cart(models.Model):
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.fruit.name} - {self.quantity} pcs"
    
    


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords in production

    def __str__(self):
        return self.username
    