"""
Serializadores de la aplicación David
"""

from rest_framework import serializers
from David.models import Silla

class SillaSerializer(serializers.ModelSerializer):
    """
    Serializador del modelo silla
    """
    class Meta:
        """
        Clase meta
        """
        model = Silla
        fields = '__all__'
