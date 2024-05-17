from rest_framework import routers
from .api import ProjectViewSetLampara

routerl = routers.DefaultRouter()

routerl.register('api/lampara', ProjectViewSetLampara, 'lamparas')

#urlpatterns = []

urlpatterns = routerl.urls