"""
Vistas de la app Juan
"""

from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from .models import Lampara


# Create your views here.
class ProjectViewSetLampara(viewsets.ModelViewSet):
    """ Vista del modelo Lampara relacionado al Serializer Lampara """
    queryset = Lampara.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
