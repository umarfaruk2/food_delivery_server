from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .serializers import FoodModelSerializer 
from .models import FoodModel
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

class FoodItemView(viewsets.ModelViewSet):
    queryset = FoodModel
    serializer_class = FoodModelSerializer 

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
        
        
class AllFoodItem(ListAPIView):
    queryset = FoodModel.objects.all()
    serializer_class = FoodModelSerializer
    