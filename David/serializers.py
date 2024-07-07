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

        """
        Para probar el método PATCH, donde solo se actualiza un campo, quitamos los requerimientos del resto de los campos en la solicitud
        """
        extra_kwargs = {
            'tipo': {'required': False},
            'cantidad': {'required': False},
            'fecha': {'required': False},
            'disponible': {'required': False},
            'contador_vistas': {'required': False}
        }
