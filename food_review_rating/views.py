from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .models import FoodReviewRatingModel
from .serializers import FoodReviewRatingSerializer
from rest_framework.views import APIView
from food_order.models import FoodOrderModel
from food_item.models import FoodModel
from rest_framework.permissions import IsAuthenticated

class ReviewRatingView(APIView):
    # add auth permission
    permission_classes = [IsAuthenticated]
    # This pk i got from which dish i order of that
    def get_order(self, pk):
        try:
            order = FoodOrderModel.objects.get(food_item__id = pk)
            return order
        except:
            return Http404

    def post(self, request, pk, format = None):
        order = self.get_order(pk)
        food_item = FoodModel.objects.get(pk = pk)
        
        if order:
            serializer = FoodReviewRatingSerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.validated_data['food_item'] = food_item
                serializer.save()

                return Response({'msg': 'Submit your review and rating'}, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format = None):
       review_rating_model = FoodReviewRatingModel.objects.get(pk = pk) 

       serializer = FoodReviewRatingSerializer(review_rating_model, data = request.data)
       if serializer.is_valid(raise_exception=True):
           serializer.save()

           return Response({'msg': 'Your review and rating updated successfully'}, status = status.HTTP_200_OK)  
       return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
       review_rating_model = FoodReviewRatingModel.objects.get(pk = pk) 
       review_rating_model.delete()

       return Response({'msg': 'Your review rating has been delete successfully'}, status = status.HTTP_406_NOT_ACCEPTABLE)
       

class AllReviewRatingView(APIView):
    def get(self, request, pk, format = None):
        food_item = FoodModel.objects.get(pk = pk)  
        review_model = FoodReviewRatingModel.objects.filter(food_item = food_item) 

        serializer = FoodReviewRatingSerializer(review_model, many=True)

        return Response(serializer.data, status = status.HTTP_200_OK)
