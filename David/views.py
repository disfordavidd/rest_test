"""
Vistas de la aplicación David
"""
from rest_framework import viewsets, permissions
from David.models import Silla
from David.serializers import SillaSerializer


class ProjectViewSetSilla(viewsets.ModelViewSet):
    """
    Definición de la vista (vieewset)
    """
    queryset = Silla.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SillaSerializer
