from rest_framework import generics
from api.serializers.features_serializers import FeaturesSerializer, TemplateSerializer, SubFeaturesSerializer
from api.models import Feature, Template, Name
from rest_framework.decorators import api_view

class GetFeatures(generics.ListAPIView):
    queryset = Feature.objects.filter(feature__template__template_name='coinbase')
    serializer_class = FeaturesSerializer
