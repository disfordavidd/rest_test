from django.shortcuts import render
from David.models import Silla
from David.serializers import SillaSerializer
from rest_framework import viewsets, permissions


class ProjectViewSetSilla(viewsets.ModelViewSet):
    queryset = Silla.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SillaSerializer