from rest_framework import serializers
from .models import FoodOrderModel
from food_item.models import FoodModel

class FoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOrderModel
        fields = ['id', 'food_item', 'order_status', 'created_order', 'updated_order']
