"""
Serializers para el CRUD con REST_FRAMEWORK
"""

from rest_framework import serializers
from .models import Lampara

class ProjectSerializer(serializers.ModelSerializer):
    """ Serializer para el modelo Lampara """
    class Meta:
        """ Parámetros del serializer Lampara """
        model = Lampara
        fields = ('id', 'nombre', 'precio', 'cantidad', 'fecha')
        #read_only_fields = ('fecha', )
