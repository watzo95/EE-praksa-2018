from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GetFeatures, UserCreateAPIView, UserLoginAPIView, calculate
from rest_framework import generics

urlpatterns = [
    url(r'^getFeatures/', GetFeatures.as_view(), name='getFeatures'),
    url(r'^calculate/', calculate, name='calculate'),
    #  url('accounts/', include('rest_registration.api.urls')),
    url(r'^loginApi/$', UserLoginAPIView.as_view(), name="login"),
    url(r'^registerApi/$', UserCreateAPIView.as_view(), name="register"),
]
