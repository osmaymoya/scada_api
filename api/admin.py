from django.contrib import admin

# Register your models here.

from .models import Magnitude
from .models import MeasureUnit

admin.site.register(Magnitude)
admin.site.register(MeasureUnit)
