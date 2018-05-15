from rest_framework import serializers
from api.models import Calculate

class CalculateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculate
        fields = ('days', 'price')

