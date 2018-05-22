from rest_framework import serializers
from api.models import Calculate
from api.models import Name, Feature, Template


class CalculateSerializer(serializers.ModelSerializer):
    obj = serializers.SerializerMethodField('get_filtered')

    def get_filtered(self, pk):
        object = pk.obj.filter(id__in=[selected_features])
        return object

    class Meta:
        model = Calculate
        fields = ('id', 'days', 'ios', 'android', 'bknd')

