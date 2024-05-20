from django.shortcuts import render
from David.models import Silla
from David.serializers import SillaSerializer
from rest_framework import generics


class silla_list(generics.ListCreateAPIView):
    queryset = Silla.objects.all()
    serializer_class = SillaSerializer
    
class silla_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Silla.objects.all()
    serializer_class = SillaSerializer