"""
Modelos de la app Juan
"""

from django.db import models

# Create your models here.

class Lampara(models.Model):
    """ Modelo Lampara y sus atributos """
    nombre = models.CharField(max_length=255)
    precio = models.FloatField(default=0)
    cantidad = models.IntegerField(default=0)
    fecha = models.DateTimeField()
