from django.db import models

# Create your models here.

class Lampara(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField(default=0)
    cantidad = models.IntegerField(default=0)
    fecha = models.DateTimeField()
