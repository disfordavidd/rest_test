from django.db import models

# Create your models here.


class Silla(models.Model):
    precio = models.BigIntegerField
    fecha = models.DateTimeField()
    tipo = models.CharField(max_length=50)
    cantidad = models.BigIntegerField
    
    def __str__(self):
        return str(self.tipo)