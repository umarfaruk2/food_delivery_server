from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.FoodOrderView.as_view(), name = 'food_order'),
    path('order/<int:pk>/', views.FoodOrderView.as_view(), name = 'order_cancel')
]
