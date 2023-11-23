from rest_framework import status
from rest_framework.response import Response
from .models import FoodOrderModel
from .serializers import FoodOrderSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class FoodOrderView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format = None):
        try:
            serializer = FoodOrderSerializer(data = request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.validated_data['user'] = request.user
                serializer.save()

                return Response({'msg': 'Food Order successfully'}, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'msg': 'something want wrong'}, status = status.HTTP_406_NOT_ACCEPTABLE)


    def get(self, request, format = None):
        food_order = FoodOrderModel.objects.filter(user = request.user)
        serializer = FoodOrderSerializer(food_order, many=True)

        return Response(serializer.data , status = status.HTTP_200_OK)
    
    
    def delete(self, request, pk, format = None):
        order_item = FoodOrderModel.objects.get(pk = pk) 
        order_item.delete()

        return Response({'msg': 'Order cancel successfully'}, status = status.HTTP_204_NO_CONTENT)
        

