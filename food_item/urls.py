from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'dish', views.FoodItemView, basename="dish")

urlpatterns = [
    path('', include(router.urls)) 
]
