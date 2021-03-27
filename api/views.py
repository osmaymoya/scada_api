from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import MagnitudeSerializer
from .models import Magnitude
from .serializers import MeasureUnitSerializer
from .models import MeasureUnit
from .serializers import SensorSerializer
from .models import Sensor


class MagnitudeViewSet(viewsets.ModelViewSet):
    queryset = Magnitude.objects.all().order_by('name')
    serializer_class = MagnitudeSerializer


class MeasureUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasureUnit.objects.all().order_by('name')
    serializer_class = MeasureUnitSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all().order_by('name')
    serializer_class = SensorSerializer
