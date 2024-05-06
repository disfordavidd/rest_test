from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_models.models import Item
from rest_models.serializers import ItemSerializer
from django.http import Http404
from rest_framework import generics

#La raíz de la API será una vista que enliste los items existentes o cree nuevos items

#Usando generics para recortar código


class item_list(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class item_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



#Usando API basada en clases

"""class item_list(APIView):
    
    #List all snippets, or create a new snippet.
    
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 #Se requiere una vista individual para obtener, actualizar o borrar un item individual   
 """

"""
class item_detail(APIView):
    
    #Retrieve, update or delete a snippet instance.
    
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item_rest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        """