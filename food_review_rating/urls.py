from django.urls import path
from . import views

urlpatterns = [
    path('review_rating/<int:pk>/', views.ReviewRatingView.as_view(), name = 'review_rating'),
    path('get_all_review/<int:pk>/', views.AllReviewRatingView.as_view(), name = 'all_review_rating')    
]