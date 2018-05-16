from rest_framework import serializers
from api.models import Name, Feature, Template


class TemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        fields = ('check', 'template_name')

class SubFeaturesSerializer(serializers.ModelSerializer):
    template = serializers.SerializerMethodField('get_temp')

    def get_temp(self, templ):
        temp = templ.template.filter(template_name='coinbase')
        return TemplateSerializer(instance=temp, many=True).data

    class Meta:
        model = Name
        fields = ('name', 'template', 'time', 'platform')


class FeaturesSerializer(serializers.ModelSerializer):
    feature = SubFeaturesSerializer(many=True)

    class Meta:
        model = Feature
        fields = ('feature_name', 'feature')

