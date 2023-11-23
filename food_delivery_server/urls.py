from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('api/', include('food_item.urls')),
    path('api/', include('food_cart.urls')),
]
