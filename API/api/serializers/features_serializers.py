from rest_framework import serializers
from api.models import Name, Feature, Template


class FilteredTemplateSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(template_name='coinbase')
        return super(FilteredTemplateSerializer, self).to_representation(data)


class TemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        list_serializer_class = FilteredTemplateSerializer
        fields = ('check', 'template_name')


class SubFeaturesSerializer(serializers.ModelSerializer):
    template = TemplateSerializer(many=True)

    class Meta:
        model = Name
        fields = ('name', 'template', 'time', 'platform')


class FeaturesSerializer(serializers.ModelSerializer):
    feature = SubFeaturesSerializer(many=True)

    class Meta:
        model = Feature
        fields = ('feature_name', 'feature')

