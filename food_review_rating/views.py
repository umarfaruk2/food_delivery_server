from rest_framework import status
from rest_framework.response import Response
from .models import FoodReviewRatingModel
from .serializers import FoodReviewRatingSerializer
from rest_framework.views import APIView

class ReviewRatingView(APIView):
    pass