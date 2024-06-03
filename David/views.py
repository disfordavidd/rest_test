"""
Importamos el modelo y el serializador
Importamos viewsets de rest_framework
"""
from rest_framework import viewsets, permissions
from David.models import Silla
from David.serializers import SillaSerializer


class ProjectViewSetSilla(viewsets.ModelViewSet):
    """
    Creamos un queryset con todos los campos del modelo Silla
    Damos todos los permisos con AllowAny
    Definimos el serializador que creamos (SillaSerializer)
    """
    queryset = Silla.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SillaSerializer
