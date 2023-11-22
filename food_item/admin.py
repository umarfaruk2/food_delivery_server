from django.contrib import admin
from .models import FoodModel

@admin.register(FoodModel)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'user')