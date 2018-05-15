from rest_framework import serializers
from api.models import Name, Feature


class SubFeaturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Name
        fields = ('name', 'checked', 'time', 'platform')


class FeaturesSerializer(serializers.ModelSerializer):
    feature = SubFeaturesSerializer(many=True)

    class Meta:
        model = Feature
        fields = ('feature_name', 'feature')