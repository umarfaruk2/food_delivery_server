from django.db import models
from account.models import User


class FoodModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
