from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='fruits/')
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}  @ {self.price_per_kg}/kg"
    
