from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageAPI.as_view()),
    path('shop/<int:pk>/', ShopPageAPI.as_view())
]