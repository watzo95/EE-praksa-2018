from rest_framework import generics
from api.serializers.features_serializers import FeaturesSerializer, TemplateSerializer, SubFeaturesSerializer, CoinbaseFeaturesSerializer, SnapchatFeaturesSerializer, RevolutFeaturesSerializer, TemplateNamesSerializer
from api.models import Feature, Template, Name
from rest_framework.decorators import api_view


class GetFeatures(generics.ListAPIView):
    # queryset = Feature.objects.filter(feature__template__template_name='coinbase')
    queryset = Feature.objects.filter()
    serializer_class = FeaturesSerializer

class GetTemplates(generics.ListAPIView):
    queryset = Template.objects.filter(fk_template_id='1')
    serializer_class = TemplateNamesSerializer


class GetCoinbase(generics.ListAPIView):
    queryset = Feature.objects.filter(feature__template__template_name='coinbase')
    serializer_class = CoinbaseFeaturesSerializer


class GetRevolut(generics.ListAPIView):
    queryset = Feature.objects.filter(feature__template__template_name='revolut')
    serializer_class = RevolutFeaturesSerializer


class GetSnapchat(generics.ListAPIView):
    queryset = Feature.objects.filter(feature__template__template_name='snapchat')
    serializer_class = SnapchatFeaturesSerializer
