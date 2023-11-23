from django.db import models
from account.models import User
from food_item.models import FoodModel

class FoodCartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.OneToOneField(FoodModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)