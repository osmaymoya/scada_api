import django
from django.db import models

# Create your models here.


class Magnitude(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class MeasureUnit(models.Model):
    name = models.CharField(max_length=60)
    symbol = models.CharField(max_length=10)
    magnitude = models.ForeignKey(Magnitude, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=10)
    magnitude = models.ForeignKey(Magnitude, on_delete=models.RESTRICT)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class ValueLog(models.Model):
    value = models.FloatField()
    time = models.DateTimeField(default=django.utils.timezone.now)
    sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.sensor}-{self.value} {self.measure_unit}'
