from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from rest_framework import generics

urlpatterns = {
    url(r'^estimateApi/$', CreateView.as_view()),
    path('accounts/', include('rest_registration.api.urls')),
}

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
