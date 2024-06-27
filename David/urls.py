"""
URLs de la aplicación David
"""

from django.urls import path, include
from rest_framework import routers
from David.views import ProjectViewSetSilla

router = routers.DefaultRouter()

router.register(r'sillas', ProjectViewSetSilla, basename='silla')


urlpatterns = [
    path('api/', include((router.urls))),

]
