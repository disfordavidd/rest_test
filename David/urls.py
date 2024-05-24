from django.urls import path, include
from rest_framework import routers
from David.views import ProjectViewSetSilla

routerl = routers.DefaultRouter()

routerl.register('sillas', ProjectViewSetSilla, 'sillas')

urlpatterns = [
    path('', include(routerl.urls)),
]
