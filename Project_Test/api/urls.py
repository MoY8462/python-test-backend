from django.urls import path
from .views import RestauranteView, UserView

urlpatterns = [
    path('restaurant/', RestauranteView.as_view(), name='restaurant_list'),
    path('user/', UserView.as_view(), name='user_list'),
    path('restaurant/<int:id>', RestauranteView.as_view(), name='restaurant_process')
]