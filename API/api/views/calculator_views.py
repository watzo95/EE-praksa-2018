from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from api.serializers.calculator_serializers import CalculateSerializer

from rest_framework.response import Response

@api_view(['POST'])
def CalculateView(request):
    if request.method == 'POST':
        serializer = CalculateSerializer(data=request.data)
        if serializer.is_valid():
            days = int(request.data['days'])
            ios = float(request.data['ios'])
            android = float(request.data['android'])
            bknd = float(request.data['bknd'])
            return Response(days*price)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data=None, status=status.HTTP_400_BAD_REQUEST)