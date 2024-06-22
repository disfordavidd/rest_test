"""
Rutas de de la app Juan
"""

from django.urls import include, path
from rest_framework import routers
from .views import ProjectViewSetLampara
from .views import LamparasList

routerl = routers.DefaultRouter()

routerl.register('lampara', ProjectViewSetLampara, 'lamparas')

urlpatterns = [
    path('', include(routerl.urls)),
    path('lamplist/', LamparasList.as_view(), name='lamplist'),
]
