from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, vpis_racunanje, izbris, skupaj_cena, UserCreateAPIView, UserLoginAPIView
from rest_framework import generics

urlpatterns = {
    url(r'^estimateApi/$', CreateView.as_view()),
    #  url('accounts/', include('rest_registration.api.urls')),
    url(r'^racun_vpis/$', vpis_racunanje, name="vpis"),
    url(r'^izbris/$', izbris, name="izbris_vse"),
    url(r'^skupaj/$', skupaj_cena, name="dobi_ceno"),
    url(r'^loginApi/$', UserLoginAPIView.as_view(), name="login"),
    url(r'^registerApi/$', UserCreateAPIView.as_view(), name="register"),
}

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
