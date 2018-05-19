from rest_framework import serializers
from api.models import Name, Feature, Template


class TemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        fields = ('check', 'template_name')


class SubFeaturesSerializer(serializers.ModelSerializer):
    template = TemplateSerializer(many=True)

    class Meta:
        model = Name
        fields = ('name', 'template', 'time', 'platform')


class TemplateNamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        fields = ('template_name', 'url')

# FILTERING DATA


class CoinbaseSerializer(serializers.ModelSerializer):
    template = serializers.SerializerMethodField('get_coinbase')

    def get_coinbase(self, gettemplate):
        temp = gettemplate.template.filter(template_name='coinbase')
        return TemplateSerializer(instance=temp, many=True).data

    class Meta:
        model = Name
        fields = ('name', 'template', 'time', 'platform')


class RevolutSerializer(serializers.ModelSerializer):
    template = serializers.SerializerMethodField('get_revolut')

    def get_revolut(self, gettemplate):
        temp = gettemplate.template.filter(template_name='revolut')
        return TemplateSerializer(instance=temp, many=True).data

    class Meta:
        model = Name
        fields = ('name', 'template', 'time', 'platform')


class SnapchatSerializer(serializers.ModelSerializer):
    template = serializers.SerializerMethodField('get_snapchat')

    def get_snapchat(self, gettemplate):
        temp = gettemplate.template.filter(template_name='snapchat')
        return TemplateSerializer(instance=temp, many=True).data

    class Meta:
        model = Name
        fields = ('name', 'template', 'time', 'platform')


class FeaturesSerializer(serializers.ModelSerializer):
    feature = SubFeaturesSerializer(many=True)

    class Meta:
        model = Feature
        fields = ('feature_name', 'feature')


# FEATURE SERIALIZERS FOR COINBASE, REVOLUT AND SNAPCHAT

class CoinbaseFeaturesSerializer(serializers.ModelSerializer):
    feature = CoinbaseSerializer(many=True)

    class Meta:
        model = Feature
        fields = ('feature_name', 'feature')


class RevolutFeaturesSerializer(serializers.ModelSerializer):
    feature = RevolutSerializer(many=True)

    class Meta:
        model = Feature
        fields = ('feature_name', 'feature')


class SnapchatFeaturesSerializer(serializers.ModelSerializer):
    feature = SnapchatSerializer(many=True)

    class Meta:
        model = Feature
        fields = ('feature_name', 'feature')
