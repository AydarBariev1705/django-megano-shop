from django.urls import path
from .views import BasketView

urlpatterns = [
    path('api/basket', BasketView.as_view(), name='basket'),
]
