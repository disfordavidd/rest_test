"""
Modelos de la aplicación David
"""

from django.db import models

class Silla(models.Model):
    """
      Definición del modelo Silla
    """
    precio = models.BigIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)
    cantidad = models.BigIntegerField()

    def __str__(self):
        return str(self.tipo)
