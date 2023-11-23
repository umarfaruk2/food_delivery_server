from django.db import models
from account.models import User
from food_item.models import FoodModel

class FoodOrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ManyToManyField(FoodModel)
    order_status = models.CharField(max_length=20)
    created_order = models.DateTimeField(auto_now_add=True)
    updated_order = models.DateTimeField(auto_now=True) 

    