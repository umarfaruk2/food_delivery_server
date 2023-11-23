from django.contrib import admin
from .models import FoodOrderModel

@admin.register(FoodOrderModel)
class FoodOrderModel(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_status')