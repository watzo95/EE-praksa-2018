from rest_framework import serializers
from collections import OrderedDict

from rest_framework.fields import SkipField

from .models import Vprasanja, Odgovori, izracun


class OdgovorSerializer(serializers.ModelSerializer):

   class Meta:
    model = Odgovori
    fields = ('odgovor1', 'odgovor2', 'odgovor3', 'odgovor4', 'odgovor5', 'odgovor6', 'odgovor7', 'odgovor8', 'odgovor9', 'odgovor10', 'platforma')


class VprasanjeSerializer(serializers.ModelSerializer):
    odg = OdgovorSerializer(many=True)

    class Meta:
        model = Vprasanja
        fields = ('vprasanje', 'odg')

class IzracunSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(IzracunSerializer, self).__init__(many=many, *args, **kwargs)
    class Meta:
        model = izracun
        fields = ('vpr', 'cena')