from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'dish', views.FoodItemView, basename="dish")

urlpatterns = [
    # path('', include(router.urls)) 
    path('dish/', views.FoodItemView.as_view(), name='dish_create'),
    path('dish/all/', views.AllFoodItem.as_view(), name='all_food')
]
