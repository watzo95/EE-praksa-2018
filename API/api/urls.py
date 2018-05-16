from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.calculator_views import CalculateView
from api.views.features_views import GetFeatures
from api.views.user_views import UserCreateAPIView, UserLoginAPIView
from rest_framework import generics

urlpatterns = [
    path('features', GetFeatures.as_view(), name='getFeatures'),
    path('calculate', CalculateView, name='calculate'),
    path('login_api/', UserLoginAPIView.as_view(), name="login"),
    path('register_api/', UserCreateAPIView.as_view(), name="register"),
]
