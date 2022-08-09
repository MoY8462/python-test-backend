from django.urls import path
from .views import RestauranteView

urlpatterns = [
    path('restaurant/', RestauranteView.as_view(), name='restaurant_list'),
    path('restaurant/<int:id>', RestauranteView.as_view(), name='restaurant_process')
]