from django.contrib import admin

# Register your models here.

from .models import Magnitude
from .models import MeasureUnit
from .models import Sensor
from .models import ValueLog

admin.site.register(Magnitude)
admin.site.register(MeasureUnit)
admin.site.register(Sensor)
admin.site.register(ValueLog)
