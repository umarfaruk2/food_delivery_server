from rest_framework import serializers
from .models import FoodReviewRatingModel


class FoodReviewRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodReviewRatingModel
        fields = ['id', 'review', 'rating']