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
