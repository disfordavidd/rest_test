from rest_framework import routers
from .views import ProjectViewSetLampara

routerl = routers.DefaultRouter()

routerl.register('lampara', ProjectViewSetLampara, 'lamparas')

#urlpatterns = []

urlpatterns = routerl.urls