from django.contrib import admin
from .models import FoodCartModel

@admin.register(FoodCartModel)
class FoodCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'total_price')