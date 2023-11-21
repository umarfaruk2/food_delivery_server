from rest_framework.response import Response
from rest_framework import status
from .serializers import FoodModelSerializer 
from .models import FoodModel
from rest_framework import viewsets

class FoodItemView(viewsets.ModelViewSet):
    queryset = FoodModel
    serializer_class = FoodModelSerializer 