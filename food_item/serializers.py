from rest_framework import serializers
from .models import FoodModel

class FoodModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    restaurant_name = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    class Meta:
        model = FoodModel
        fields = ['id', 'name', 'description', 'restaurant_name', 'price']
        