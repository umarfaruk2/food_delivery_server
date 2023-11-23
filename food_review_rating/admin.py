from django.contrib import admin
from .models import FoodReviewRatingModel

@admin.register(FoodReviewRatingModel)
class FoodReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'rating', 'food_item')