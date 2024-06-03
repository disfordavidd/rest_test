"""
Importar el modelo Silla para serializarlo usando rest_framework serializers
"""

from rest_framework import serializers
from David.models import Silla

class SillaSerializer(serializers.ModelSerializer):
    """
    Usamos el ModelSerializer de Rest Framework
    """
    class Meta:
        """
        Modificamos el ModelSerializer con el modelo Silla y serializamos todos sus campos
        """
        model = Silla
        fields = '__all__'
