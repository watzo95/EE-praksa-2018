from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VprasanjeSerializer, OdgovorSerializer, IzracunSerializer
from .models import Odgovori, Vprasanja, izracun
from django.db.models import Sum

# Create your views here.
class CreateView(generics.ListAPIView):
    queryset = Vprasanja.objects.all()
    serializer_class = VprasanjeSerializer

@api_view(['GET', 'POST'])
def vpis_racunanje(request):
    if request.method == 'GET':
        racun = izracun.objects.all()
        serializer = IzracunSerializer(racun, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IzracunSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data=None, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def izbris(request):
    if request.method == 'DELETE':
        vsi = izracun.objects.all()
        vsi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def skupaj_cena(request):
    if request.method == 'GET':
        skupna_cena = izracun.objects.aggregate(Sum('cena'))
        return Response(skupna_cena)