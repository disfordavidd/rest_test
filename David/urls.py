"""
Importamos path e include de django urls
Importamos routers para configurar un router que organice las urls
Importamos el viewset para asociarlo con la url /sillas
"""

from django.urls import path, include
from rest_framework import routers
from David.views import ProjectViewSetSilla

routerl = routers.DefaultRouter()

routerl.register('sillas', ProjectViewSetSilla, 'sillas')

urlpatterns = [
    path('', include(routerl.urls)),
]
