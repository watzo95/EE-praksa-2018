from rest_framework import generics
from api.serializers.features_serializers import FeaturesSerializer, TemplateSerializer, SubFeaturesSerializer
from api.models import Feature, Template, Name
from rest_framework.decorators import api_view


@api_view(['POST'])
def retrieveString(request):
    context = {"options": ['Coinbase', 'Revolut', 'Snapchat']}
    serializer = TemplateSerializer(data=request.data, context=context)


class GetFeatures(generics.ListAPIView):
    queryset = Feature.objects.filter()
    serializer_class = FeaturesSerializer
