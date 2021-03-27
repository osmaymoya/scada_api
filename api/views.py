from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from .serializers import MagnitudeSerializer
from .models import Magnitude
from .serializers import MeasureUnitSerializer
from .models import MeasureUnit
from .serializers import SensorSerializer
from .models import Sensor
from .serializers import ValueLogSerializer
from .models import ValueLog


class MagnitudeViewSet(viewsets.ModelViewSet):
    queryset = Magnitude.objects.all().order_by('name')
    serializer_class = MagnitudeSerializer


class MeasureUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasureUnit.objects.all().order_by('name')
    serializer_class = MeasureUnitSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all().order_by('name')
    serializer_class = SensorSerializer


class ValueLogViewSet(viewsets.ModelViewSet):
    queryset = ValueLog.objects.all().order_by('-time')
    serializer_class = ValueLogSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = ValueLog.objects.all().order_by('-time')
        sensor = self.request.query_params.get('sensor_id')
        if sensor is not None:
            queryset = queryset.filter(sensor__id=sensor)
        return queryset
