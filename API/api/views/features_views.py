from rest_framework import generics
from api.serializers.features_serializers import FeaturesSerializer, TemplateSerializer, SubFeaturesSerializer
from api.models import Feature, Template, Name


class GetFeatures(generics.ListAPIView):
    queryset = Feature.objects.filter()
    serializer_class = FeaturesSerializer



