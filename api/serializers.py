# serializers.py

from rest_framework import serializers
from .models import Magnitude
from .models import MeasureUnit


class MagnitudeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Magnitude
        fields = ('id', 'name', 'symbol')


class MeasureUnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MeasureUnit
        fields = ('id', 'name', 'magnitude')
