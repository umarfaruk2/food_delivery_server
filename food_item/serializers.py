from rest_framework import serializers
from .models import FoodModel

class FoodModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodModel
        fields = ['name', 'description', 'price']
        