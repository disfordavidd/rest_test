from django.urls import include, path
from rest_framework import routers
from .views import ProjectViewSetLampara

routerl = routers.DefaultRouter()

routerl.register('lampara', ProjectViewSetLampara, 'lamparas')

urlpatterns = [
    path('', include(routerl.urls)),
]