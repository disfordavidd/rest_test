"""
Vistas de la aplicación David
"""
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework import viewsets, permissions, renderers, status
from rest_framework.response import Response
from David.models import Silla
from David.serializers import SillaSerializer


class ProjectViewSetSilla(viewsets.ModelViewSet):
    """
    Definición de la vista
    """
    queryset = Silla.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SillaSerializer
    renderer_classes = [renderers.TemplateHTMLRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(disponible=True) #Mostrar solo las sillas disponibles
        serializer = self.get_serializer(queryset, many=True)
        return Response({'sillas': serializer.data}, template_name='silla_list.html')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.contador_vistas = instance.contador_vistas + 1 #Añadir un contador de vistas y sumar 1 en cada request get
        instance.save()
        serializer = self.get_serializer(instance)
        return Response({'silla': serializer.data}, template_name='silla_detail.html')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        messages.success(request, 'La silla se ha creado correctamente.') # Agregar mensaje flash
        return Response({'silla': serializer.data}, status=status.HTTP_201_CREATED, template_name='silla_detail.html')


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'silla': serializer.data}, template_name='silla_detail.html')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        messages.success(request, 'La silla se ha eliminado correctamente.') # Agregar mensaje flash
        return redirect('silla-list')