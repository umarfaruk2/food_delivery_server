from django.urls import path
from . import views

urlpatterns = [
    path('create_cart/<int:pk>/', views.CreateFoodCartView.as_view(), name = 'create_cart'),
    path('cart/', views.FoodCartView.as_view(), name = 'food_cart'),
    path('cart/<int:pk>/', views.FoodCartView.as_view(), name = 'update_delete_cart'),
]