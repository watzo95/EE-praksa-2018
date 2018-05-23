from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from api.models import Name
from api.serializers.features_serializers import NameSerializer
from rest_framework.response import Response
from django.http import JsonResponse

@api_view(['POST'])
def CalculateView(request):
    if request.method == 'POST':
        array = request.GET.getlist('id')
        string = array[0]
        array = map(int, string.split(','))
        obj = Name.objects.filter(id__in=array)
        serializer = NameSerializer(obj, many=True)
        sum_total = sum_android = sum_ios = sum_backend = 0
        cost_dev_day = 300
        for item in serializer.data:
            sum_total += item['total_time']
            sum_android += item['android_developer']
            sum_ios += item['ios_developer']
            sum_backend += item['backend_developer']
        sum_total *= cost_dev_day
        sum_android *= cost_dev_day
        sum_ios *= cost_dev_day
        sum_backend *= cost_dev_day
        return JsonResponse({'total_cost': sum_total, 'android_cost': sum_android, 'ios_cost': sum_ios, 'backend_cost': sum_backend, 'hourly_rate_day': cost_dev_day})
    else:
        return Response(data=None, status=status.HTTP_400_BAD_REQUEST)