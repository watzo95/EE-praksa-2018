from rest_framework import generics
from api.serializers.features_serializers import FeaturesSerializer
from api.models import Feature


class GetFeatures(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeaturesSerializer
