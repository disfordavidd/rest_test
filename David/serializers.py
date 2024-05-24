from rest_framework import serializers
from David.models import Silla

class SillaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Silla
        fields = '__all__'