from rest_framework import serializers
from rest_models.models import Item

    #Se crea el serializador
    
class ItemSerializer(serializers.ModelSerializer):
    
    #Aquí se definen los campos que deben ser serializados/deserializados cuando se hereda de Serializer
    
    #id = serializers.IntegerField(read_only=True)
    #name = serializers.CharField(max_length=50)
    #new = serializers.BooleanField(default=False)
    #added = serializers.DateTimeField()
    
    #Al heredar de ModelSerializer, se añaden de la siguiente manera:
    
      class Meta:
        model = Item
        fields = ['id', 'name', 'new', 'added']
    
    #ModelSerializer ya incluye los métodos predefinidos de crear y editar
    
    
    #Se añaden los métodos para crear o editar en el caso de solo usar Serializer
    
    
    #def create(self, validated_data):
        """
        Create and return a new `Item_rest` instance, given the validated data.
        """
    #return Item_rest.objects.create(**validated_data)
    
    #def update(self, instance, validated_data):
        """
        Update and return an existing `Item_rest` instance, given the validated data.
        """
        #instance.name = validated_data.get('name', instance.name)
        #instance.new = validated_data.get('new', instance.new)
        #instance.added = validated_data.get('added', instance.added)
        #instance.save()
        
        #return instance