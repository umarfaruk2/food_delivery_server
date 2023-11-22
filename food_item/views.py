from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .serializers import FoodModelSerializer 
from .models import FoodModel
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class FoodItemView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return FoodModel.objects.get(pk = pk)
        except FoodModel.DoesNotExist():
            return Http404
            
    def post(self, request, format = None):
        serializer = FoodModelSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response({'msg': 'Create new dish successfully'}, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk, format = None):
        food = self.get_object(pk)
        
        serializer = FoodModelSerializer(food)
        return Response({"data": serializer.data})

    def patch(self, request, pk, format = None):
        food = self.get_object(pk)

        serializer = FoodModelSerializer(food, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Dish update successfully'}, status = status.HTTP_200_OK)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format= None):
        food = self.get_object(pk)
        food.delete()

        return Response({'msg': 'Dish Delete successfully'}, status = status.HTTP_204_NO_CONTENT)
        
        
        
class AllFoodWithSearchItem(ListAPIView):
    queryset = FoodModel.objects.all()
    serializer_class = FoodModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

class AllFoodWithFilterItem(ListAPIView):
    queryset = FoodModel.objects.all()
    serializer_class = FoodModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price']
    