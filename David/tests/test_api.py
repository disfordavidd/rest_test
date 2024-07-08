from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from David.models import Silla
from David.serializers import SillaSerializer
from datetime import datetime

class SillaAPITests(APITestCase):
    """
    Clase para realizar pruebas a la API del modelo SILLAS.
    """
    def setUp(self):
        """
        Crear instancia del modelo Sillas para realizar las pruebas
        """
        self.instance = Silla.objects.create(precio = 1,
                                            fecha = datetime.now(),
                                            tipo = 'test',
                                            cantidad = 1,
                                            disponible = True,
                                            contador_vistas = 0)

    def test_create(self):
        url = reverse('silla-list')
        data = {'precio': 2,
                'datetime': datetime.now().isoformat(),
                'tipo':'test',
                'cantidad': 1,
                'disponible': True,
                'contador_vistas' : 0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Silla.objects.count(), 2)
        created_silla = Silla.objects.last()
        self.assertEqual(created_silla.precio, 2)
        self.assertEqual(created_silla.tipo, 'test')
        self.assertEqual(created_silla.cantidad, 1)
        self.assertEqual(created_silla.disponible, True)
        self.assertEqual(created_silla.contador_vistas, 0)



    def test_retrieve(self):
        url = reverse('silla-detail', args=[self.instance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['silla']['precio'], 1)
        self.assertEqual(response.data['silla']['tipo'], 'test')
        self.assertEqual(response.data['silla']['cantidad'], 1)
        self.assertEqual(response.data['silla']['disponible'], True)
        self.assertEqual(response.data['silla']['contador_vistas'], 1)

    def test_update(self):
        url = reverse('silla-detail', args=[self.instance.id])
        data = {
            'precio': 3,
            'fecha': self.instance.fecha.isoformat(),
            'tipo': 'updated',
            'cantidad': 2,
            'disponible': False,
            'contador_vistas': 0
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.precio, 3)
        self.assertEqual(self.instance.tipo, 'updated')
        self.assertEqual(self.instance.cantidad, 2)
        self.assertEqual(self.instance.disponible, False)

    def test_partial_update(self):
        url = reverse('silla-detail', args=[self.instance.id])
        data = {
            'precio': 4
        }
        response = self.client.patch(url, data, format='json')
        self.assertIn('silla', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.precio, 4)

    def test_delete(self):
        url = reverse('silla-detail', args=[self.instance.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Silla.objects.count(), 0)

class SillaTest(TestCase):
    """
    Evaluar el modelo Silla
    """
    def setUp(self):
        """
        Crear instancia del modelo Silla para realizar las pruebas.
        """
        self.silla = Silla.objects.create(
            precio=100,
            tipo='Oficina',
            cantidad=10,
            disponible=True,
            contador_vistas=0
        )

    def test_silla_creation(self):
        """
        Prueba que se pueda crear una silla y se guarde correctamente.
        """
        self.assertEqual(self.silla.precio, 100)
        self.assertEqual(self.silla.tipo, 'Oficina')
        self.assertEqual(self.silla.cantidad, 10)
        self.assertTrue(self.silla.disponible)
        self.assertEqual(self.silla.contador_vistas, 0)


    def test_silla_str_method(self):
        """
        Prueba el método __str__ del modelo Silla.
        """
        self.assertEqual(str(self.silla), 'Oficina')


class SillaSerializerTest(TestCase):
    """
    Evaluar el serializador SillaSerializer
    """
    def setUp(self):
        """
        Crear instancia del modelo Silla para realizar las pruebas.
        """
        self.silla_data = {
            'precio': 100,
            'tipo': 'Oficina',
            'cantidad': 10,
            'disponible': True,
            'contador_vistas': 0
        }
        self.silla = Silla.objects.create(**self.silla_data)
        self.serializer = SillaSerializer(instance=self.silla)

    def test_contains_expected_fields(self):
        """
        Prueba que el serializador contenga los campos esperados.
        """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'precio', 'fecha', 'tipo', 'cantidad', 'disponible', 'contador_vistas']))
