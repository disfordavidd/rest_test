from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from .models import Lampara


# Create your views here.
class ProjectViewSetLampara(viewsets.ModelViewSet):
    queryset = Lampara.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer