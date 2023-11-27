from django.db import models
from account.models import User


class FoodModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    restaurant_name = models.CharField(max_length=100, unique=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
