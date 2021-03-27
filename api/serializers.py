# serializers.py

from rest_framework import serializers
from .models import Magnitude
from .models import MeasureUnit
from .models import Sensor


class MagnitudeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Magnitude
        fields = ('id', 'name')


class MeasureUnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MeasureUnit
        fields = ('id', 'name', 'symbol', 'magnitude')


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'name', 'code', 'magnitude', 'measure_unit')
