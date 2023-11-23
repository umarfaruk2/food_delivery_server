from django.db import models
from account.models import User
from food_item.models import FoodModel

class FoodReviewRatingModel(models.Model):
    food_item = models.ForeignKey(FoodModel, on_delete=models.CASCADE)
    review = models.CharField(max_length=255)
    rating = models.IntegerField()

    def __str__(self):
        return self.review