from rest_framework import serializers
from .models import Lampara

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lampara
        fields = ('id', 'nombre', 'precio', 'cantidad', 'fecha')
        #read_only_fields = ('fecha', )