"""
Vistas de la app Juan
"""

from django.shortcuts import render, redirect
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProjectSerializer
from .models import Lampara


# Create your views here.
class ProjectViewSetLampara(viewsets.ModelViewSet):
    """ Vista del modelo Lampara relacionado al Serializer Lampara """
    queryset = Lampara.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

    def post(self, request, pk):
        """DELETE method personalizado"""
        if request.POST["_method"] == "DELETE":
            lamp = Lampara.objects.get(id=pk)
            lamp.delete()
        return redirect('lamplist')

class LamparasList(generics.ListAPIView):
    """Vista para listar las lamparas con el template listarlamparas.html"""
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        """GET method personalizado"""
        queryset = Lampara.objects.all()
        global_stock = 0
        global_price_items = 0
        for item in queryset:
            total_price_item = item.cantidad * item.precio
            item.totalprice = total_price_item
            global_stock += item.cantidad
            global_price_items += total_price_item
        return render(request, 'listarlamparas.html', {
            'title' : "Listado",
            'lamps' : queryset,
            'global_stock' : global_stock,
            'global_price' : global_price_items
        })
