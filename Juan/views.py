"""
Vistas de la app Juan
"""

from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectSerializer
from .models import Lampara


# Create your views here.
class ProjectViewSetLampara(viewsets.ModelViewSet):
    """ Vista del modelo Lampara relacionado al Serializer Lampara """
    queryset = Lampara.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

class LamparasList(APIView):
    """Vista para listar las lamparas"""

    permission_classes = [permissions.AllowAny]
    
    def get(self, request, *args, **kwargs):
        """GET method personalizado"""
        queryset = Lampara.objects.all()
        #serializer = ProjectSerializer(queryset, many=True)
        #return Response(serializer.data, status=status.HTTP_200_OK)
        return render(request, 'listarlamparas.html', {
            'title' : "Listado",
            'lamps' : queryset,
        })
