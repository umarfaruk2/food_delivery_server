from .models import FoodCartModel
from django.http import Http404
from food_item.models import FoodModel
from .serializers import FoodCartSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class CreateFoodCartView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request, pk, format = None):
        food_item = FoodModel.objects.get(pk = pk) 
        serializer = FoodCartSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['user'] = request.user
            serializer.validated_data['food_item'] = food_item
            serializer.save()

            return Response({'msg': 'Add to cart successfully'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class FoodCartView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return FoodCartModel.objects.get(pk = pk)
        except:
            return Http404
    
    def get(self, request, format = None):
        cart_item = FoodCartModel.objects.filter(user = request.user)
        serializer = FoodCartSerializer(cart_item, many=True)

        return Response(serializer.data , status = status.HTTP_200_OK)
    
    def patch(self, request, pk, format = None):
        cart_item = self.get_object(pk)

        serializer = FoodCartSerializer(cart_item, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            return Response({'msg': 'Cart updated'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        cart_item = self.get_object(pk)
        cart_item.delete()

        return Response({'msg': 'Cart delete successfully'}, status = status.HTTP_204_NO_CONTENT)

        
        
