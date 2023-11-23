from rest_framework import serializers
from .models import FoodCartModel


class FoodCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCartModel
        fields = ['id', 'total_price', 'quantity']