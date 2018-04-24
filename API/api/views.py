from django.shortcuts import render
from rest_framework import generics
from .serializers import VprasanjeSerializer, OdgovorSerializer
from .models import Odgovori, Vprasanja

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset = Vprasanja.objects.all()
    serializer_class = VprasanjeSerializer
