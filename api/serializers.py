# serializers.py

from rest_framework import serializers
from .models import Magnitude
from .models import MeasureUnit
from .models import Sensor
from .models import ValueLog


class MagnitudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magnitude
        fields = ('id', 'name')


class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        fields = ('id', 'name', 'symbol', 'magnitude')


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'name', 'code', 'magnitude', 'measure_unit')


class ValueLogSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(many=False)
    measure_unit = MeasureUnitSerializer(many=False)

    class Meta:
        model = ValueLog
        fields = ('id', 'value', 'time', 'sensor', 'measure_unit')
        extra_kwargs = {"measure_unit": {"required": False, "allow_null": True}}


class ValueLogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValueLog
        fields = ('id', 'value', 'sensor')
