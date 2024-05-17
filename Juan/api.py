from .models import Lampara
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSetLampara(viewsets.ModelViewSet):
    queryset = Lampara.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer